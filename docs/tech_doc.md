# Technical Documentation — Lean Stack

## 1. Technology Stack

### Backend

| Component | Technology | Why |
|-----------|-----------|-----|
| API Server | Python (FastAPI) | Async, fast, same language as ML later |
| Database | TimescaleDB (on RDS PostgreSQL) | SQL + time-series; team knows Postgres |
| IoT Ingestion | AWS IoT Core (MQTT) | Managed, zero ops, scales to millions |
| Processing | AWS Lambda | Pay-per-invocation; no servers to manage |
| Object Storage | AWS S3 | Reports, raw data archive |
| Alerting | AWS SNS (SMS) + SES (email) | Managed, cheap |

### Frontend

| Component | Technology | Why |
|-----------|-----------|-----|
| Dashboard | React + TypeScript | Standard, rich ecosystem |
| Charts | Recharts or Chart.js | Simple time-series visualization |
| Maps | Leaflet (open source) | Sensor location overlay on dam schematic |
| Hosting | S3 + CloudFront | Static, cheap, fast |

### Infrastructure

| Component | Technology |
|-----------|-----------|
| Deployment | Docker Compose (dev) → EC2 (prod) |
| CI/CD | GitHub Actions |
| Monitoring | CloudWatch (basic) |
| Domain/SSL | Route53 + ACM |

**What we deliberately skip:** Kafka, Kubernetes, EKS, SageMaker, ELK stack, Terraform. All can be added later when complexity warrants it.

---

## 2. Sensor Integration

### Modbus RTU Register Map (VW Piezometer Example)

| Register | Data | Type |
|----------|------|------|
| 40001-40002 | Frequency (Hz) | Float32 |
| 40003-40004 | Temperature (°C) | Float32 |
| 40005-40006 | Pressure (kPa) | Float32 |
| 40007 | Status flags | UInt16 |

### Data Logger Poll Cycle

1. Logger polls each sensor every 15 minutes via RS-485 bus
2. Applies calibration coefficients (stored in logger configuration)
3. Converts raw frequency → engineering units (kPa, mm, degrees)
4. Buffers in local flash memory (30-day capacity)
5. Transmits via LoRaWAN at next uplink window

### Calibration

Each sensor has calibration coefficients provided by Encardio Rite at installation:
- Stored in data logger configuration AND in our `sensors.calibration` JSONB field
- Engineering value = f(raw_frequency, temperature, calibration_coefficients)
- Recalibration recommended annually

---

## 3. Data Pipeline Details

### Sensor → Dashboard Flow

```
1. Sensor reading (Modbus RTU) → Data Logger
2. Data Logger → LoRaWAN uplink (encrypted, ~200 bytes for 20 sensors)
3. Gateway → AWS IoT Core (MQTT over TLS, topic: dam/{dam_id}/readings)
4. IoT Rule → Lambda function:
   a. Parse LoRaWAN payload (decode binary → JSON)
   b. Validate: range check, checksum
   c. Write batch INSERT to TimescaleDB
   d. For each reading: check against sensor thresholds
   e. If threshold exceeded → publish to SNS topic → SMS + email
   f. Write raw payload to S3 (archive)
5. Dashboard (React):
   a. Polls /api/sensors every 30 seconds
   b. Renders time-series charts and health indicators
```

---

## 4. Compliance Report Generation

### Report Types

| Report | Frequency | Automation Level |
|--------|-----------|-----------------|
| Pre-Monsoon Inspection | Annual (May) | 70% automated (sensor data + stats), 30% manual (field observations) |
| Post-Monsoon Inspection | Annual (Nov) | 70% automated |
| Dam Safety Act Annual Report | Annual | 60% automated |
| Emergency Report | Event-triggered | Alert auto-generated; narrative manual |

### Generation Pipeline

1. User clicks "Generate Report" in dashboard (or scheduled trigger)
2. FastAPI queries TimescaleDB for reporting period
3. Calculates statistics: min, max, mean, trend direction, exceedance count
4. Generates charts using matplotlib (sensor trends, rainfall correlation)
5. Fills NDSA template sections with data and charts
6. Generates PDF using WeasyPrint (HTML → PDF)
7. Uploads to S3, records in `reports` table
8. User downloads from dashboard

### Template Structure (NDSA Format)

```
1. Dam Identification (static: name, type, location, capacity)
2. Instrumentation Status (from sensors table: count, types, health)
3. Monitoring Data Summary (from readings: period stats per sensor)
4. Anomalies & Exceedances (from alerts: list of threshold breaches)
5. Trend Analysis (computed: 30/90/365-day trends per sensor)
6. Recommendations (semi-manual: template prompts + engineer input)
7. Attachments (auto: time-series charts, sensor map)
```

---

## 5. External Data Sources

| Source | Data | Access | Cost | Phase |
|--------|------|--------|------|-------|
| India-WRIS | Reservoir levels, river discharge | HTTP API (free) | Free | MVP |
| IMD Open Data | Gridded rainfall, temperature | HTTP/FTP | Free | MVP |
| IMD Commercial | High-res forecasts | API (licensed) | ~INR 2-5L/yr | Phase 2 |
| Sentinel-2 (ESA) | NDVI for crop mapping | Copernicus API | Free | Phase 3 |
| Sentinel-1 (ESA) | SAR for InSAR | Copernicus API | Free | Phase 2 (via SkyGeo) |

---

## 6. Security

| Layer | Measure |
|-------|---------|
| LoRaWAN | AES-128 encryption (built into protocol) |
| Transport | TLS 1.3 for all MQTT and HTTPS |
| AWS | IAM roles, VPC, security groups, encrypted-at-rest |
| Application | JWT authentication, role-based access (admin/engineer/viewer) |
| Data policy | Government retains data ownership; we provide analytics-as-a-service |

---

## 7. Development Setup

### Local Development

```bash
# Prerequisites: Docker, Node.js 20+, Python 3.11+

# Backend
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm run dev

# Database (local TimescaleDB)
docker run -d --name timescaledb -p 5432:5432 \
  -e POSTGRES_PASSWORD=dev \
  timescale/timescaledb:latest-pg16

# Simulated sensor data (for development without real sensors)
python scripts/simulate_sensors.py
```

### Deployment (Production)

```bash
# EC2 instance (t3.medium)
docker-compose up -d  # FastAPI + Nginx

# RDS (TimescaleDB)
# Configured via AWS console / Terraform (later)

# Frontend
npm run build
aws s3 sync dist/ s3://dashboard-bucket/
```
