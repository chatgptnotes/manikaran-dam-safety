# Budget — Lean Startup Phasing

## Overview

| Phase | Duration | Budget (INR) | Budget (USD) |
|-------|----------|------------:|------------:|
| Phase 0: Validate & Fundraise | 6 months | 15,00,000 | ~$18,000 |
| Phase 1: MVP (20 sensors, 1 dam section) | 12 months | 72,00,000 | ~$86,000 |
| Phase 2: Expand Gosikhurd + ML | 18 months | 2,00,00,000 | ~$240,000 |
| **Total to first paid contract** | **~30 months** | **~2,87,00,000** | **~$344,000** |

Compare to original Manikaran plan: INR 9.7 Cr. **This is ~30% of original cost, enabled by China-sourced sensors assembled in India.** See `research/china_sensor_sourcing.md` for full sourcing strategy.

---

## Phase 0: Validate & Fundraise (6 months) — INR 15 lakh

| Item | Amount (INR) |
|------|------------:|
| Founder salaries (2 people, 6 months) | 6,00,000 |
| Domain advisor retainer (6 months) | 1,50,000 |
| Travel (site visits, govt meetings, investor meetings) | 3,00,000 |
| Legal (incorporation, IP, MoU drafting) | 1,50,000 |
| Prototyping (cloud dev, sensor eval kits) | 2,00,000 |
| Co-working space | 1,00,000 |
| **Total Phase 0** | **15,00,000** |

**Funding:** Personal savings, friends & family, or small government grant.

---

## Phase 1: MVP Build & Deploy (12 months) — INR 82 lakh

### One-Time: Sensors & Hardware — INR 10 lakh (China-sourced + India-assembled)

| Item | Qty | Source | Unit Cost (INR) | Total (INR) |
|------|-----|--------|---------------:|------------:|
| VW Piezometer (China: BGT/Kingmach) | 10 | China import | 5,000-12,000 | 80,000 |
| Crack Meter (China: GeoSitter) | 5 | China import | 4,000-10,000 | 35,000 |
| MEMS Tiltmeter (China: Rion Technology) | 3 | China import | 3,000-15,000 | 25,000 |
| Seepage Flow Meter (India: Fluidyne) | 2 | India | 50,000 | 1,00,000 |
| Data Logger (China: CHCNAV H960) | 2 | China import | 25,000-65,000 | 80,000 |
| LoRaWAN Gateway + Solar (RAKwireless) | 1 | China import | 15,000-30,000 | 25,000 |
| Indian enclosures + cable assembly | — | India fabrication | — | 80,000 |
| Calibration equipment (one-time) | — | India/Import | — | 2,00,000 |
| Customs duty (~27% on imports) | — | — | — | 60,000 |
| Installation (own team + local contractor) | — | India | — | 2,00,000 |
| Contingency (25%) | — | — | — | 1,50,000 |
| **Subtotal Hardware** | | | | **10,35,000** |

**Savings vs. Encardio Rite sourcing: ~INR 8 lakh (45% reduction)**

*Note: Seepage flow meters kept Indian (Fluidyne) — need local calibration standards. Calibration equipment is a one-time investment that pays off across all future deployments.*

### Recurring: Team (12 months) — INR 50 lakh

| Role | Count | Annual CTC (INR) |
|------|-------|----------------:|
| Founder / CEO | 1 | 8,00,000 |
| CTO / Co-founder | 1 | 14,00,000 |
| IoT / Embedded Engineer | 1 | 10,00,000 |
| Full-Stack Developer | 1 | 12,00,000 |
| Field Technician (Nagpur) | 1 | 5,00,000 |
| Domain Advisor (part-time) | 1 | 3,00,000 |
| **Subtotal Team** | **6** | **52,00,000** |

### Recurring: Operations (12 months) — INR 14 lakh

| Item | Annual (INR) |
|------|------------:|
| Cloud infrastructure (AWS) | 2,10,000 |
| Nagpur office (co-working) | 3,00,000 |
| Travel & site visits | 4,00,000 |
| Software licenses & tools | 1,00,000 |
| InSAR monitoring (6 months trial) | 4,00,000 |
| **Subtotal Operations** | **14,10,000** |

### Phase 1 Total

| Category | Amount (INR) |
|----------|------------:|
| Sensors & Hardware (one-time) | 18,20,000 |
| Team (12 months) | 52,00,000 |
| Operations (12 months) | 14,10,000 |
| **Total Phase 1** | **84,30,000** |

**Funding:** Seed round (INR 1-2 Cr) from climate-tech VCs, impact investors, or government grants.

---

## Phase 2: Expand Gosikhurd + ML Models (18 months) — INR 2.24 Cr

| Item | Amount (INR) |
|------|------------:|
| Additional sensors (40-50 units, expanding to full dam) | 35,00,000 |
| Additional gateways (2-3 more) | 5,00,000 |
| Installation (expanded coverage) | 10,00,000 |
| Team expansion (add 2 data scientists + 1 BD manager, 18 months) | 60,00,000 |
| Existing team salaries (18 months) | 78,00,000 |
| Cloud scale-up (add Kafka, ML compute) | 8,00,000 |
| Operations (18 months) | 12,00,000 |
| Contingency (10%) | 16,00,000 |
| **Total Phase 2** | **2,24,00,000** |

**Funding:** Revenue from first paid contract + bridge round or pre-Series A.

---

## Phase 3: Second Dam + Scale (18 months+) — Series A Funded

| Item | Estimate (INR) |
|------|---------------:|
| Second dam sensor package (30-40 sensors) | 40,00,000 |
| Team scale to 15-20 people | 1,50,00,000 |
| Multi-state operations | 30,00,000 |
| Platform productization | 20,00,000 |
| **Total Phase 3** | **~2,40,00,000** |

**Funding:** Series A (INR 5-15 Cr).

---

## Unit Economics Target (At Scale)

| Metric | Value |
|--------|-------|
| Sensor CapEx per dam (50-80 sensors) | INR 40-60 lakh |
| Annual SaaS revenue per dam | INR 25-50 lakh |
| CapEx payback | 1-2 years (if customer funds sensors) |
| Gross margin at 50+ dams | 60-70% |
| Cloud cost per dam | ~INR 2-3 lakh/year |
