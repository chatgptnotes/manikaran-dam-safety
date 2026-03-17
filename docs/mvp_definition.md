# MVP Definition

## What We Build First

**One sentence:** A real-time dashboard that ingests sensor data from a 2 km section of Gosikhurd Dam, detects anomalies via threshold rules, and generates Dam Safety Act-compliant inspection reports.

---

## Scope: In vs. Out

### IN (MVP)

| Component | Scope |
|-----------|-------|
| **Site** | 2 km critical section of Gosikhurd embankment (identified by CDSRP-2 review) |
| **Sensors** | 10 VW piezometers, 5 crack meters, 3 tiltmeters, 2 seepage flow meters = ~20 sensors |
| **Connectivity** | 1 LoRaWAN gateway + solar + 4G backhaul |
| **Data pipeline** | Sensor → data logger → LoRaWAN → AWS IoT Core (MQTT) → TimescaleDB |
| **Dashboard** | Web-based; real-time sensor readings, time-series plots, health status |
| **Alerting** | Threshold-based (upper/lower limits per sensor) via SMS + email |
| **Compliance** | Template-based PDF report generator (pre-monsoon/post-monsoon inspection format) |
| **Users** | 3-5 VIDC engineers, 1-2 CWC officials (view-only) |

### OUT (Later Phases)

| Component | Why Not Now |
|-----------|-----------|
| Totladoh Dam | Focus on one dam; add later |
| Full Gosikhurd (11.35 km) | Too expensive; expand incrementally after proving value |
| ML models (LSTM, anomaly detection) | Need 12+ months of data first; rule-based is sufficient for MVP |
| Canal instrumentation | Different product; Phase 3+ |
| Flood forecasting / gate advisory | Requires mature ML + reservoir data |
| Mobile app | Web dashboard is sufficient initially |
| Kafka / Kubernetes | Over-engineered for 20 sensors; simple MQTT + TimescaleDB is enough |
| DFOS (fiber optic) | INR 14 lakh for one system; add later |
| GNSS / robotic total station | Expensive; InSAR satellite monitoring is cheaper for surface deformation |
| Accelerographs | Gosikhurd is Seismic Zone II (low risk); not critical for MVP |

---

## MVP Sensor Package

| Sensor Type | Make | Qty | Unit Cost (INR) | Total (INR) | Purpose |
|-------------|------|-----|---------------:|------------:|---------|
| VW Piezometer | Encardio Rite EPC-20V | 10 | 25,000 | 2,50,000 | Pore pressure in embankment |
| Crack Meter | Encardio Rite EJM-10V | 5 | 20,000 | 1,00,000 | Joint movement at spillway interface |
| MEMS Tiltmeter | Encardio Rite EAN-52M | 3 | 40,000 | 1,20,000 | Embankment slope rotation |
| Seepage Flow Meter | Fluidyne India | 2 | 50,000 | 1,00,000 | Toe drain seepage volume |
| Data Logger (LoRaWAN) | Encardio Rite ESDL-30 | 2 | 1,50,000 | 3,00,000 | Aggregation + transmission |
| LoRaWAN Gateway + Solar | Kerlink + 100W panel | 1 | 1,50,000 | 1,50,000 | Wireless backhaul |
| **Total Hardware** | | **23** | | **10,20,000** | |
| Installation (Encardio Rite) | | | | 5,00,000 | Professional installation |
| **Total Deployed Cost** | | | | **15,20,000** | |

**~INR 15 lakh for sensors + installation.** Compare to INR 3.67 Cr in the original plan.

---

## MVP Tech Stack (Lightweight)

| Layer | Technology | Monthly Cost (INR) |
|-------|-----------|------------------:|
| IoT Ingestion | AWS IoT Core (MQTT) | 2,000 |
| Database | TimescaleDB on RDS (db.t3.medium) | 8,000 |
| App Server | EC2 (t3.medium) — FastAPI | 5,000 |
| Frontend | React SPA on S3 + CloudFront | 1,000 |
| Alerting | AWS SNS (SMS) + SES (email) | 500 |
| Storage | S3 (raw data archive) | 500 |
| **Total Cloud** | | **~17,000/month** |

**~INR 2 lakh/year for cloud.** No Kafka, no Kubernetes, no EKS cluster needed for 20 sensors.

---

## MVP Success Criteria

| Criteria | Metric |
|----------|--------|
| Sensor uptime | >90% of sensors reporting continuously for 3+ months |
| Data latency | <5 min from sensor reading to dashboard display |
| Alert delivery | <2 min from threshold breach to SMS |
| Monsoon capture | Full July-October data for all installed sensors |
| Compliance report | Generate 1 complete pre-monsoon or post-monsoon inspection report |
| User adoption | At least 2 VIDC engineers actively checking the dashboard weekly |
| Anomaly detection | Correctly flag at least 1 real threshold exceedance (or demonstrate on simulated data) |

---

## MVP Timeline

| Month | Milestone |
|-------|-----------|
| 1-2 | Sensor procurement (Encardio Rite, 8-12 week lead) |
| 1-3 | Cloud platform development (MQTT → TimescaleDB → Dashboard) |
| 3-4 | Sensor installation on 2 km section (must be pre-monsoon, before June) |
| 4-5 | Commission gateway, test end-to-end data flow |
| 5-6 | Implement alerting + report generator |
| 6 | Live demo to VIDC engineers |
| 6-10 | First monsoon data capture (July-October) |
| 10-11 | Generate first automated post-monsoon inspection report |
| 12 | Review: did it work? Expand or pivot. |

**Total MVP build time: ~6 months to first data, ~12 months to first compliance report.**

---

## What MVP Proves

1. **Technical viability** — we can ingest real dam sensor data reliably
2. **Value proposition** — automated monitoring is better than manual quarterly inspection
3. **Compliance gap** — the report we generate is what NDSA/SDSO requires, and VIDC can't produce it today
4. **Scalability thesis** — if 20 sensors work on 2 km, the platform can handle 200 sensors on 11 km
5. **Customer willingness** — VIDC engineers actually use the dashboard and find it valuable
