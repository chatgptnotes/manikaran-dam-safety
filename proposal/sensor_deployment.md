# Sensor Deployment Plan

## Gosikhurd Dam — Sensor Package

| Category | Sensor Type | Product / Make | Qty | Purpose |
|----------|------------|---------------|-----|---------|
| **Seepage & Water Pressure** | VW Piezometer | Encardio Rite EPC-20V | 40 | Pore pressure along 11.35 km embankment |
| | Standpipe Piezometer | Encardio Rite (manual backup) | 20 | Cross-validation |
| | Seepage Weir + Flow Meter | Fluidyne India / Campbell Scientific | 8 | Seepage at toe drains |
| **Structural Movement** | Crack Meter / Joint Meter | Encardio Rite EJM-10V | 25 | Spillway-embankment interfaces |
| | MEMS Tiltmeter | Encardio Rite EAN-52M | 15 | Embankment slope rotation |
| | In-Place Inclinometer | Geokon 6150 | 8 | Deep subsurface lateral movement |
| | GNSS Receiver | Leica GR30 / Trimble NetR9 | 6 | 3D surface displacement |
| **Stress & Strain** | Earth Pressure Cell | Geokon 4800 | 12 | Stress in embankment core |
| | Thermistor String | Geokon 3800 | 10 | Temperature profile |
| **Seismic** | Accelerograph | GeoSIG GMSplus | 3 | Seismic event recording |
| **Advanced** | DFOS | Sensuron / AP Sensing | 2 lines (2 km each) | Continuous strain on critical sections |
| | InSAR | SkyGeo / DeepInSAR | 1 service | Sub-mm deformation from space |
| **Connectivity** | LoRaWAN Gateway + Solar | Kerlink / Tektelic | 4 | Wireless across 11.35 km |

## Totladoh Dam — Sensor Package

| Category | Sensor Type | Product / Make | Qty | Purpose |
|----------|------------|---------------|-----|---------|
| **Seepage & Uplift** | VW Piezometer | Encardio Rite EPC-20V | 30 | Uplift at concrete-foundation interface |
| | Uplift Pressure Cell | Geokon 4500 | 14 | One per monolith (14 bays) |
| **Structural Movement** | Crack / Joint Meter | Encardio Rite EJM-10V | 20 | Expansion joints |
| | Pendulum (Direct + Inverted) | Sisgeo / Huggenberger | 4 sets | Crest deflection |
| | Robotic Total Station | Leica TM50 | 1 | Automated 3D survey |
| | GNSS Receiver | Trimble NetR9 | 4 | Real-time crest displacement |
| **Strain** | VW Strain Gauge | Geokon 4200 | 16 | Strain in spillway piers |
| **Seismic** | Accelerograph | GeoSIG GMSplus | 3 | Crest, gallery, foundation |
| **Hydrology** | Radar Level Sensor | Endress+Hauser Micropilot | 2 | Reservoir + tailwater level |
| **Gate Monitoring** | Position Sensor + Load Cell | Custom / Encardio Rite | 14 sets | All 14 spillway gates |
| **Connectivity** | LoRaWAN Gateway + 4G | Kerlink + Jio SIM | 2 | Across 680 m dam |

## Canal Instrumentation (Both Command Areas)

| Sensor Type | Product / Make | Qty | Location |
|-------------|---------------|-----|----------|
| Ultrasonic Flow Meter | Endress+Hauser Prosonic Flow | 30 | Main canal heads, branch off-takes |
| Radar Water Level Sensor | Endress+Hauser FMR20 | 40 | Every 5 km on main canal |
| Soil Moisture Probe | Sentek EnviroSCAN / METER TEROS | 20 | Head, middle, tail reaches |
| Weather Station | Campbell Scientific / Onset HOBO | 6 | Microclimate stations |
| Motorized Gate Actuator | Rotork / AUMA | 15 | Critical canal regulators |

## Drone & Satellite Inspection

- **Quarterly drone surveys:** DJI Matrice 350 RTK + LiDAR (Zenmuse L2) for 3D models
- **Annual LiDAR bathymetric survey** for reservoir sedimentation mapping
- **Monthly InSAR processing:** Sentinel-1 SAR (free) + ICEYE commercial SAR
- **AI-powered crack detection** on drone imagery using CNN
