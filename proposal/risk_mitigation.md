# Risk Mitigation — Startup-Specific

## Funding Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **Cannot raise seed funding** | Medium | Critical | Apply to 3-4 grants simultaneously; keep Phase 0 on personal savings; bootstrap with consulting if needed |
| **Burn rate exceeds runway** | Medium | High | 6-month runway minimum rule; don't hire ahead of need; phase everything |
| **18-month gap between pilot start and first revenue** | High | High | Plan for this in seed round; explore Encardio Rite revenue share for earlier cash flow |

## Credibility Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **Government won't engage unknown startup** | High | High | Lead with VNIT academic partnership; hire ex-CWC advisor; partner with Encardio Rite |
| **Competitors (L&T, TCS) enter the space** | Medium | Medium | Move fast; build data moat; they'll be slow with generic "smart city" solutions |
| **VIDC refuses site access** | Medium | High | Backup plan: try other states (Uttarakhand, Himachal); Encardio Rite can facilitate |

## Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **ML models need 2+ monsoon seasons** | High | Medium | Start with rule-based thresholds; ML is Phase 2, not MVP |
| **Sensor reliability in harsh conditions** | Medium | Medium | Use proven vendors (Encardio Rite, Geokon); plan for 10-15% failure rate; build redundancy |
| **LoRaWAN connectivity unreliable at dam** | Medium | Medium | Test gateway placement during dry season; data loggers store 30 days locally as buffer |
| **Small team can't build IoT + ML + dashboard** | Medium | High | Use managed services (AWS IoT Core); no Kafka/K8s for MVP; keep it simple |

## Market Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **Dam Safety Act enforcement stays weak** | Low-Medium | High | Focus on dams already under CWC/DRIP scrutiny (enforcement is strongest there) |
| **Government budget cuts** | Low | Medium | Diversify: irrigation optimization has private-sector value beyond compliance |
| **Long government sales cycle (12-18 months)** | High | High | Start with free pilot or academic route to bypass procurement |

## Operational Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **Missing monsoon installation window** | High | Very High (12-month delay!) | Start procurement 5 months before June; install above-water sensors first if delayed |
| **Key person leaves (CTO)** | Medium | High | Equity vesting; document everything; no single-person dependencies |
| **Nagpur talent shortage (IoT/ML roles)** | Medium | Medium | Allow remote for software roles; hire from Pune/Bangalore; Nagpur for field only |
| **Sensor theft/vandalism at dam** | Medium | Low | Tamper-proof enclosures; install in galleries where possible; insure equipment |

## Contingency Plans

| Scenario | Response |
|----------|----------|
| Can't get Gosikhurd access | Try Totladoh, or target a smaller dam in another state (Uttarakhand SDSO) |
| Seed round fails | Bootstrap: offer dam inspection consulting to generate cash while building product |
| VIDC won't pay after free pilot | Pivot to Encardio Rite partnership model (they sell, we provide software layer) |
| ML models underperform | Rule-based monitoring + compliance reports are valuable on their own; ML is additive, not core |
| COVID/monsoon disruption | Field tech stays local in Nagpur; software team works remote; 30-day data logger buffer |
