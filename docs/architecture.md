# Platform Architecture

## Dam Safety Compliance Platform — Standalone Architecture

---

## 1. Architecture Principles

- **Start simple, add complexity only when needed**
- **Managed services over self-hosted** (small team, minimize ops burden)
- **Designed for 20 sensors today, architected to handle 2,000 later**
- **India-hosted** (AWS Mumbai for data sovereignty)

---

## 2. System Architecture (MVP)

```
╔══════════════════════════════════════════════════════════════╗
║                  EDGE LAYER (Gosikhurd Dam, 2 km section)    ║
║  ┌──────────────┐ ┌──────────────┐ ┌──────────────────────┐ ║
║  │VW Piezometers│ │ Crack Meters │ │ Tiltmeters + Seepage │ ║
║  │   (10 nos)   │ │   (5 nos)    │ │  Meters (3+2 nos)    │ ║
║  └──────┬───────┘ └──────┬───────┘ └──────────┬───────────┘ ║
║         └────────────────┼────────────────────┘              ║
║                          ▼                                    ║
║              Modbus RTU / SDI-12 / Analog                     ║
║                          ▼                                    ║
║         ┌─────────────────────────────────┐                   ║
║         │  Encardio Rite Data Logger (x2) │                   ║
║         │  + LoRaWAN Radio                │                   ║
║         └──────────────┬──────────────────┘                   ║
╚════════════════════════┼═════════════════════════════════════╝
                         ▼
               LoRaWAN (868 MHz)
                         ▼
            ┌─────────────────────────┐
            │  LoRaWAN Gateway        │
            │  Solar + Battery        │
            │  4G Jio SIM backhaul    │
            └────────────┬────────────┘
                         ▼
               4G LTE to Internet
                         ▼
╔══════════════════════════════════════════════════════════════╗
║                CLOUD LAYER (AWS Mumbai)                       ║
║                                                               ║
║  ┌───────────┐    ┌──────────────┐    ┌──────────────────┐   ║
║  │ AWS IoT   │───→│ Lambda /     │───→│  TimescaleDB     │   ║
║  │ Core      │    │ Simple       │    │  (RDS Postgres)  │   ║
║  │ (MQTT)    │    │ Processing   │    │                  │   ║
║  └───────────┘    └──────┬───────┘    └────────┬─────────┘   ║
║                          │                     │              ║
║                          ▼                     ▼              ║
║                   ┌──────────────┐    ┌──────────────────┐   ║
║                   │ Alert Engine │    │  FastAPI Server   │   ║
║                   │ SNS (SMS)    │    │  (EC2 t3.medium)  │   ║
║                   │ SES (Email)  │    │  REST APIs        │   ║
║                   └──────────────┘    └────────┬─────────┘   ║
║                                                │              ║
║                                                ▼              ║
║                                       ┌──────────────────┐   ║
║                                       │  React Dashboard  │   ║
║                                       │  (S3+CloudFront)  │   ║
║                                       └──────────────────┘   ║
╚══════════════════════════════════════════════════════════════╝
```

**Key simplifications from original design:**
- No Kafka (20 sensors don't need stream processing)
- No Kubernetes (single EC2 instance is sufficient)
- No SageMaker (rule-based alerting first, ML later)
- AWS Lambda for lightweight data processing instead of dedicated consumers

---

## 3. Scale-Up Architecture (Phase 2+, 100+ Sensors)

When sensor count exceeds ~100, add:
- **Kafka** for reliable stream processing (replace Lambda)
- **SageMaker** for ML model inference
- **EKS** if multiple microservices needed
- **Additional gateways** (1 per 3 km of dam)

The MVP architecture is intentionally designed so each component can be swapped for its scaled equivalent without rewriting the application layer.

---

## 4. Data Flow

```
Sensor Reading (every 15 min)
    │
    ▼
Data Logger applies calibration → engineering units (kPa, mm, °C)
    │
    ▼
LoRaWAN uplink (encrypted payload, ~50 bytes per sensor)
    │
    ▼
Gateway forwards via MQTT to AWS IoT Core
    │
    ▼
IoT Rule triggers Lambda function:
  ├── Validate payload (checksum, range check)
  ├── Write to TimescaleDB (sensor_readings hypertable)
  ├── Check thresholds → trigger SNS alert if exceeded
  └── Archive raw payload to S3
    │
    ▼
Dashboard polls API every 30 seconds for latest readings
```

---

## 5. Database Design (TimescaleDB)

**Hypertable: sensor_readings**
```sql
CREATE TABLE sensor_readings (
    time         TIMESTAMPTZ NOT NULL,
    dam_id       INT NOT NULL,
    sensor_id    INT NOT NULL,
    sensor_type  TEXT NOT NULL,  -- 'piezometer', 'crack_meter', 'tiltmeter', 'seepage'
    value        FLOAT8 NOT NULL,
    unit         TEXT NOT NULL,  -- 'kPa', 'mm', 'degrees', 'm3/hr'
    quality      TEXT DEFAULT 'good',  -- 'good', 'suspect', 'bad'
    battery_v    FLOAT4,
    PRIMARY KEY (time, sensor_id)
);
SELECT create_hypertable('sensor_readings', 'time');
```

**Table: alert_events**
```sql
CREATE TABLE alert_events (
    id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at   TIMESTAMPTZ DEFAULT now(),
    dam_id       INT NOT NULL,
    sensor_id    INT NOT NULL,
    alert_type   TEXT NOT NULL,  -- 'threshold_high', 'threshold_low', 'trend', 'anomaly'
    severity     TEXT NOT NULL,  -- 'info', 'warning', 'critical'
    value        FLOAT8,
    threshold    FLOAT8,
    message      TEXT,
    acknowledged BOOLEAN DEFAULT false,
    ack_by       TEXT,
    ack_at       TIMESTAMPTZ
);
```

**Table: sensors (configuration)**
```sql
CREATE TABLE sensors (
    id              INT PRIMARY KEY,
    dam_id          INT NOT NULL,
    name            TEXT NOT NULL,
    type            TEXT NOT NULL,
    location_desc   TEXT,
    latitude        FLOAT8,
    longitude       FLOAT8,
    elevation_m     FLOAT4,
    unit            TEXT NOT NULL,
    threshold_low   FLOAT8,
    threshold_high  FLOAT8,
    installed_date  DATE,
    calibration     JSONB  -- calibration coefficients
);
```

---

## 6. Technology Choices

| Layer | MVP Choice | Why | Scale-Up Replacement |
|-------|-----------|-----|---------------------|
| IoT Broker | AWS IoT Core | Managed MQTT, no ops | Same (scales to millions) |
| Processing | AWS Lambda | Pay-per-invocation, zero ops | Kafka + consumers |
| Database | TimescaleDB (RDS) | SQL + time-series; team knows Postgres | Same (scales well) |
| App Server | FastAPI on EC2 | Simple, fast, Python (same as ML later) | EKS |
| Frontend | React on S3 | Static hosting, cheap, fast | Same |
| Alerting | AWS SNS + SES | Managed SMS/email | Same + PagerDuty |
| ML (Phase 2) | scikit-learn / PyTorch | Start simple, go deep later | SageMaker |

---

## 7. Security

| Layer | Measure |
|-------|---------|
| Edge | LoRaWAN AES-128 encryption; tamper-proof sensor enclosures |
| Transport | TLS 1.3 for all cloud communication |
| Cloud | IAM roles, VPC, encrypted-at-rest (RDS + S3) |
| Application | JWT auth, role-based access (admin, engineer, viewer) |
| Data | Government retains data ownership; we provide analytics |

---

## 8. Cost (Monthly, MVP)

| Service | Monthly (INR) |
|---------|-------------:|
| AWS IoT Core | 2,000 |
| Lambda | 500 |
| RDS (TimescaleDB, db.t3.medium) | 8,000 |
| EC2 (t3.medium, FastAPI) | 5,000 |
| S3 + CloudFront | 1,500 |
| SNS + SES | 500 |
| **Total** | **~17,500** |

**~INR 2.1 lakh/year.** This is affordable for a seed-stage startup.
