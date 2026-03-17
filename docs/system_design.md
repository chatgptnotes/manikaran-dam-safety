# System Design — Lean MVP

## Design Principle: Simplest Thing That Works

For 20 sensors on one dam section, we don't need Kafka, Kubernetes, or microservices. We need a reliable pipeline from sensor to dashboard.

---

## 1. Edge Layer (At Dam Site)

### Sensor Protocols

| Protocol | Sensors | Notes |
|----------|---------|-------|
| Modbus RTU (RS-485) | VW Piezometers, Crack Meters, Tiltmeters | Standard for Encardio Rite sensors |
| Analog (4-20mA) | Seepage flow meters | ADC at data logger |

### Data Logger: Encardio Rite ESDL-30 (x2)

- 30 VW channels + 8 analog + RS-485 Modbus master
- Built-in LoRaWAN radio (Class A)
- 256 MB flash (30 days local buffer)
- Solar-powered with 12V battery backup

### LoRaWAN Network

- 1 gateway (Kerlink Wirnet iFemtoCell)
- 100W solar panel + battery
- 4G Jio SIM for backhaul
- Covers 2 km dam section with margin

---

## 2. Cloud Layer (AWS Mumbai)

### Data Pipeline

```
Sensor → Modbus RTU → Data Logger → LoRaWAN → Gateway → 4G
                                                           │
                                                           ▼
                                                    AWS IoT Core (MQTT)
                                                           │
                                                           ▼
                                                    Lambda Function
                                                    ├── Validate payload
                                                    ├── Write to TimescaleDB
                                                    ├── Check thresholds → SNS alert
                                                    └── Archive raw to S3
                                                           │
                                                           ▼
                                                    FastAPI (EC2)
                                                    ├── REST APIs
                                                    └── Report generator
                                                           │
                                                           ▼
                                                    React Dashboard (S3+CDN)
```

### Database: TimescaleDB (PostgreSQL Extension)

**Why TimescaleDB:** PostgreSQL-compatible (everyone knows it), excellent time-series performance, built-in compression, runs on standard RDS.

**Core tables:**

```sql
-- Sensor readings (hypertable, partitioned by time)
sensor_readings(time, dam_id, sensor_id, sensor_type, value, unit, quality, battery_v)

-- Alert events
alert_events(id, created_at, dam_id, sensor_id, alert_type, severity, value, threshold, acknowledged)

-- Sensor configuration
sensors(id, dam_id, name, type, location, unit, threshold_low, threshold_high, calibration)

-- Compliance reports
reports(id, dam_id, report_type, period_start, period_end, generated_at, pdf_url, status)
```

### Data Retention

| Tier | Resolution | Duration | Storage |
|------|-----------|----------|---------|
| Hot | Raw 15-min readings | 2 years | TimescaleDB |
| Warm | Hourly aggregated | 10 years | TimescaleDB (compressed) |
| Cold | Raw archive | Indefinite | S3 |

---

## 3. Application Layer

### Dashboard (React)

- **Home:** Dam overview — health status (green/yellow/red), last reading time, active alerts
- **Sensors:** Time-series plots for each sensor (1 day / 1 week / 1 month / custom range)
- **Alerts:** Active and historical alerts, acknowledge button, severity filter
- **Reports:** Generate compliance report, download PDF, view history
- **Map:** Sensor locations on dam schematic (GeoJSON overlay)

### API (FastAPI)

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/sensors` | GET | List all sensors with latest reading |
| `/api/sensors/{id}/readings` | GET | Time-series data (with date range params) |
| `/api/alerts` | GET/POST | List alerts, acknowledge an alert |
| `/api/reports/generate` | POST | Trigger compliance report generation |
| `/api/reports` | GET | List generated reports, download PDF |
| `/api/health` | GET | System health check |

### Report Generator

- Queries TimescaleDB for the reporting period
- Calculates: min/max/mean/trend for each sensor
- Flags any threshold exceedances
- Fills NDSA-format template (using reportlab or WeasyPrint for PDF)
- Stores PDF in S3, records in `reports` table

---

## 4. Alerting

### Threshold Alerts (MVP)

Each sensor has configurable `threshold_low` and `threshold_high` in the `sensors` table. Lambda checks every reading:

```
if reading > threshold_high → CRITICAL alert
if reading < threshold_low → WARNING alert
if no reading for 2 hours → SENSOR_OFFLINE alert
if battery < 3.0V → LOW_BATTERY alert
```

### Alert Delivery

- **SMS:** AWS SNS to 3-5 phone numbers (VIDC engineers + our field tech)
- **Email:** AWS SES to configured recipients
- **Dashboard:** Real-time alert banner + alert history page

### ML Alerts (Phase 2 — Add Later)

- Isolation Forest for multivariate anomaly detection
- LSTM autoencoder for seepage pattern anomaly
- These run as a separate service, writing to the same `alert_events` table

---

## 5. LoRaWAN Payload Format

```
Byte 0:     Message type (0x01=periodic, 0x02=alert)
Byte 1:     Sensor count
Byte 2-3:   Sensor ID (uint16)
Byte 4-7:   Value (float32, little-endian)
Byte 8:     Quality flag (0=good, 1=suspect, 2=bad)
Byte 9:     Battery voltage (uint8, value/10 = volts)
[Repeat bytes 2-9 for each sensor]
```

~10 bytes per sensor × 20 sensors = 200 bytes per uplink. Well within LoRaWAN SF7 limits.

---

## 6. Latency Budget

| Stage | Target |
|-------|--------|
| Sensor → Logger | <1 sec |
| Logger → Gateway (LoRaWAN) | <10 sec |
| Gateway → IoT Core (4G) | <5 sec |
| IoT Core → Lambda → TimescaleDB | <3 sec |
| Dashboard poll interval | 30 sec |
| **End-to-end (reading to screen)** | **<1 min** |

For 15-minute reading intervals, this latency is more than sufficient.

---

## 7. What Changes at Scale

| Trigger | Action |
|---------|--------|
| >100 sensors | Add Kafka between IoT Core and DB (replace Lambda for reliable ordering) |
| >3 dams | Multi-tenant schema (dam_id partitioning) |
| ML models operational | Add SageMaker endpoint; separate inference service |
| >20 concurrent dashboard users | Add Redis caching layer; WebSocket for real-time |
| >500 sensors | Consider EKS for microservices |

The MVP architecture is intentionally designed so each component can be upgraded independently.
