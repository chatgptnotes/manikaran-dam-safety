# Task List & Implementation Phases

## Start Small, Build On It — One Dam at a Time

---

## Phase 0: Validate & Fundraise (Months 0-6)

### Company Setup
- [ ] Incorporate Private Limited company
- [ ] Open bank account, register for GST
- [ ] Set up basic website / landing page

### Team
- [ ] Recruit CTO / technical co-founder (IoT + ML skills)
- [ ] Engage domain advisor (ex-CWC or retired dam safety engineer, part-time)

### Validation
- [ ] Site visit to Gosikhurd Dam — assess existing Encardio Rite sensors
- [ ] Meet VNIT Nagpur Civil Engineering faculty — explore research partnership
- [ ] Meet Encardio Rite (Lucknow) — explore sensor supply + partnership
- [ ] Build prototype: ingest India-WRIS open reservoir data → display on dashboard → generate sample compliance report PDF

### Funding
- [ ] Apply to DST Water Technology Initiative (grant up to INR 50L)
- [ ] Apply to BIRAC BIG (INR 50L grant)
- [ ] Apply to 2-3 incubators (T-Hub, SINE IIT-B, NSRCEL IIM-B)
- [ ] Pitch to 5-10 seed-stage investors / angels
- [ ] Secure seed funding: INR 1-2 Cr (or grant of INR 30-50L minimum)

### Stakeholder Access
- [ ] Draft MoU with VNIT for joint research at Gosikhurd
- [ ] Introductory meeting with VIDC Executive Director (Nagpur)
- [ ] Obtain site access permission (via VNIT or VIDC directly)

### Decision Gate (Month 6)
**Proceed if:** Funding secured + at least one institutional relationship (VNIT MoU or VIDC letter). **If not:** Reassess. Consider consulting/services model to generate cash while building product.

---

## Phase 1: MVP — 20 Sensors on 2 km of Gosikhurd (Months 6-18)

### Hiring
- [ ] Hire IoT / embedded engineer (LoRaWAN, Modbus, data loggers)
- [ ] Hire full-stack developer (React + FastAPI)
- [ ] Hire field technician (Nagpur-based, sensor installation)
- [ ] Set up Nagpur office (co-working or small office near VIDC)

### Sensor Procurement & Installation

**CRITICAL: Installation must complete before monsoon (June). Plan procurement 4-5 months ahead.**

- [ ] Finalize sensor selection with CTO + domain advisor
- [ ] Issue PO to Encardio Rite: 10 VW piezometers, 5 crack meters, 3 tiltmeters, 2 data loggers
- [ ] Procure 2 seepage flow meters (Fluidyne India)
- [ ] Procure 1 LoRaWAN gateway + solar panel + 4G SIM
- [ ] Install sensors on 2 km critical section (Encardio Rite supervision)
- [ ] Commission gateway, test end-to-end: sensor → logger → LoRaWAN → cloud

### Platform Build
- [ ] Set up AWS infrastructure (IoT Core, RDS/TimescaleDB, EC2, S3)
- [ ] Build data ingestion: MQTT → Lambda → TimescaleDB
- [ ] Build dashboard: real-time sensor plots, health status, sensor map
- [ ] Implement threshold alerting (per-sensor upper/lower limits → SMS + email)
- [ ] Build compliance report generator (PDF, pre-monsoon/post-monsoon template)
- [ ] Implement data quality checks (range validation, gap detection, battery alerts)

### Validate
- [ ] Live demo to VIDC engineers (Month ~12)
- [ ] Capture first monsoon season data (Jul-Oct, if timing aligns)
- [ ] Generate first automated inspection report
- [ ] Collect feedback from VIDC + CWC

### Optional (If Budget Allows)
- [ ] Contract InSAR monitoring service (SkyGeo/DeepInSAR) for monthly deformation maps
- [ ] One drone survey (Skylark Drones) for 3D model of dam section

### Decision Gate (Month 18)
**Proceed if:** Sensors operational, dashboard working, VIDC engagement positive. **Expand to Phase 2.** **If not:** Debug technical issues; try different stakeholder approach; explore Encardio Rite partnership.

---

## Phase 2: Expand Gosikhurd + Add ML (Months 18-30)

### Expand Sensor Coverage
- [ ] Add 30-50 sensors incrementally along remaining 9 km of dam
- [ ] Add 2-3 more LoRaWAN gateways
- [ ] Install GNSS receivers (2-3) for surface displacement
- [ ] Consider DFOS on highest-risk section

### ML Models (Trained on Phase 1 Monsoon Data)
- [ ] Seepage anomaly detection (Isolation Forest → LSTM autoencoder)
- [ ] Inflow forecasting (LSTM + IMD weather data)
- [ ] Integrate ML predictions into dashboard + alerting

### Compliance Automation
- [ ] Automate annual Dam Safety Act report generation
- [ ] Automate CWC data sheet submission
- [ ] Add multi-user access with role-based permissions (Admin, Engineer, Viewer, Regulator)

### Revenue
- [ ] Convert VIDC free pilot to paid contract (target: INR 25-50 lakh/year)
- [ ] Register as DRIP technology vendor
- [ ] Begin BD with 2-3 other states (Uttarakhand, Gujarat, Jharkhand)

### Publish
- [ ] Co-author whitepaper with VNIT Nagpur
- [ ] Present at CWC Dam Safety Conference or similar forum

### Decision Gate (Month 30)
**Proceed to Phase 3 if:** Paid contract signed, ML models operational, pipeline of additional dams.

---

## Phase 3: Second Dam + Scale (Months 30-42+)

### Second Dam Deployment
- [ ] Select second dam: Totladoh (Nagpur) or DRIP-funded dam in another state
- [ ] Deploy 30-40 sensors (platform is now proven, faster deployment)
- [ ] Validate multi-dam platform operation

### Platform Productization
- [ ] Multi-tenant architecture (configurable per dam type: earthen vs. concrete)
- [ ] Self-service sensor onboarding workflow
- [ ] API for third-party integration (Encardio Rite Proqio, government portals)

### Canal Module (Optional, If Demand Exists)
- [ ] Deploy 10-15 canal flow meters at key off-takes
- [ ] Build crop water demand model (satellite NDVI + weather)
- [ ] Dynamic scheduling recommendations

### Scale
- [ ] Raise Series A (INR 5-15 Cr)
- [ ] Scale team to 15-20 people
- [ ] Target: 10+ dams under management by end of Phase 3
- [ ] Explore Encardio Rite formal partnership (bundled hardware + software)

---

## Critical Path

```
Incorporate → Co-founder → Funding → Sensor PO → Installation (before monsoon!)
                                                        │
                                                        ▼
                                               Monsoon Data (Jul-Oct)
                                                        │
                                                        ▼
                                               ML Model Training
                                                        │
                                                        ▼
                                               Paid Contract
```

**The single biggest schedule risk:** Missing the pre-monsoon installation window (June) delays everything by 12 months. Work backwards from June to plan procurement and site access.
