# Product Requirements Document (PRD)

## Dam Safety Compliance Platform — Independent Startup

**Version:** 2.0 | **Date:** March 2026

---

## 1. Vision

Build an affordable, end-to-end Dam Safety Act compliance platform — from IoT sensors to automated NDSA/SDSO reports — starting with one dam, one section, and scaling from there.

## 2. Problem Statement

- India has 5,334 large dams; 1,137 are >50 years old; <15% have adequate monitoring
- Dam Safety Act 2021 mandates real-time instrumentation — most states can't comply
- 36 dam failures reported 2017-2024; 90%+ had no real-time monitoring
- No company in India offers affordable compliance-as-a-service for dams

### Gosikhurd Dam Specifically

- INR 25,972 Cr invested, only 14% of command area irrigated
- 11.35 km earthen dam — highest risk profile, needs continuous monitoring
- Existing Encardio Rite sensors partially functional — upgrade opportunity
- Nationally monitored by CWC; politically visible

## 3. Target Users

| User | Need | Phase |
|------|------|-------|
| VIDC Engineers (Gosikhurd) | Real-time sensor dashboard, alert on anomalies | MVP |
| CWC Officials | Automated data sheets, safety status | MVP |
| SDSO/NDSA | Dam Safety Act-compliant inspection reports | MVP |
| VIDC Management | Health score overview, compliance status | Phase 1 |
| Irrigation Officers | Canal flow data, allocation tracking | Phase 3+ |

## 4. Requirements by Phase

### Phase 1: MVP (One Dam Section)

**P0 — Must Have:**
- [ ] Ingest data from 15-20 sensors (piezometers, crack meters, tiltmeters, seepage meters)
- [ ] 15-minute automated reading intervals via LoRaWAN
- [ ] Web dashboard: real-time sensor values, time-series plots, health status
- [ ] Threshold-based alerting: upper/lower limits per sensor, SMS + email
- [ ] Template-based compliance report generator (pre-monsoon/post-monsoon PDF)
- [ ] Data stored in time-series database with 10-year retention

**P1 — Should Have:**
- [ ] Trend analysis: 7-day/30-day moving averages with trend direction indicators
- [ ] InSAR satellite deformation monitoring (monthly, via service contract)
- [ ] Exportable CSV/Excel data for VIDC engineers

**P2 — Nice to Have:**
- [ ] Basic anomaly detection (statistical: >2σ from historical baseline)
- [ ] Quarterly drone survey integration (photos + crack measurements)

### Phase 2: Full Dam + ML (Expand Gosikhurd)

- [ ] Scale to 50-80 sensors covering full 11.35 km embankment
- [ ] ML-based seepage anomaly detection (LSTM autoencoder, trained on Phase 1 monsoon data)
- [ ] Inflow forecasting model (LSTM + IMD weather data)
- [ ] Automated annual Dam Safety Act report generation
- [ ] Multi-user access with role-based permissions

### Phase 3: Second Dam + Canal Module

- [ ] Deploy at second dam (Totladoh or DRIP-funded dam)
- [ ] Canal flow monitoring (ultrasonic meters at key off-takes)
- [ ] Crop water demand estimation (satellite NDVI + weather)
- [ ] Dynamic canal scheduling recommendations

## 5. Non-Functional Requirements

| Requirement | MVP Target | At Scale |
|-------------|-----------|----------|
| Sensor data latency | <5 min | <1 min |
| Platform uptime | 95% | 99.5% |
| Data retention | 10 years | 10 years |
| Alert delivery | <2 min | <1 min |
| Concurrent users | 5-10 | 50+ |
| Data sovereignty | AWS Mumbai | AWS Mumbai |

## 6. MVP Success Criteria

| Criteria | Target |
|----------|--------|
| Sensor uptime | >90% for 3+ continuous months |
| Monsoon data capture | Full July-October dataset |
| Compliance report | 1 complete inspection report generated |
| User adoption | 2+ VIDC engineers checking dashboard weekly |
| Stakeholder feedback | Positive validation from VIDC or CWC |

## 7. Out of Scope (Entire Startup)

- Environmental compliance (CEMS/OCEMS) — different market
- Energy sector forecasting — that's Manikaran's business
- Dam construction or physical repair
- Sensor manufacturing — we integrate, not manufacture
