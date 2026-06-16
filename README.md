# Space Situational Awareness Dashboard for ISS and Cosmos 2251 Debris

A full-stack application for analyzing and visualizing potential close approaches between the International Space Station (ISS) and debris fragments from the Cosmos 2251 debris cloud.

The system retrieves live orbital data from CelesTrak, propagates satellite positions using Skyfield, performs proximity analysis, classifies potential risk levels, and visualizes the results on an interactive 3D globe using CesiumJS.

---

## Features

* Fetches live TLE data from CelesTrak
* Propagates ISS and Cosmos 2251 debris orbits using Skyfield
* Computes satellite positions over a prediction window
* Filters debris objects using altitude-overlap criteria
* Calculates closest-approach distances between the ISS and nearby debris fragments
* Classifies debris into risk categories (Green / Yellow / Red)
* Visualizes ISS and debris positions on a 3D globe using CesiumJS
* Displays the ISS orbit trail
* Interactive debris markers with metadata including:

  * NORAD Catalog Number
  * Minimum distance to ISS
  * Risk status
  * Current altitude
* Risk table sorted by closest-approach distance

---

## System Architecture

### Backend (FastAPI)

The backend is responsible for:

1. Retrieving TLE data for the ISS and Cosmos 2251 debris objects
2. Creating Skyfield satellite objects
3. Propagating orbital positions
4. Calculating orbital characteristics (apogee and perigee)
5. Filtering candidate debris based on altitude overlap
6. Computing distances between the ISS and nearby debris over time
7. Generating visualization-ready JSON data
8. Serving processed results through a FastAPI endpoint

### Frontend (React + CesiumJS)

The frontend:

1. Fetches processed data from the FastAPI API
2. Displays Earth using CesiumJS
3. Renders ISS and debris markers
4. Displays the ISS orbit trajectory
5. Provides interactive information popups
6. Shows a risk assessment table

---

## Technology Stack

### Frontend

* React
* Vite
* CesiumJS

### Backend

* FastAPI
* Python
* Skyfield

### Data Source

* CelesTrak TLE Data

---

## Project Structure

```text
SSA/
│
├── backend/
│   ├── api.py
│   ├── main.py
│   ├── extracting_tle.py
│   ├── EarthSatellite_objects.py
│   ├── get_apogee_perigee.py
│   ├── altitude_overlap_filter.py
│   ├── eci_calculate.py
│   ├── euclidDistance.py
│   ├── visualization_data.py
│   ├── requirements.txt
│   └── data/
│
├── ssa-dashboard/
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
│
└── venv/
```

---

## Risk Classification

| Minimum Distance to ISS | Status |
| ----------------------- | ------ |
| ≤ 1500 km               | Red    |
| 1500 – 5000 km          | Yellow |
| > 5000 km               | Green  |

---

## Running the Project

### Backend

```bash
cd backend

pip install -r requirements.txt

python -m uvicorn api:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

### Frontend

```bash
cd ssa-dashboard

npm install

npm run dev
```

Frontend runs at:

```text
http://localhost:5173
```

---

## Example Workflow

```text
CelesTrak TLE Data
        ↓
ISS + Cosmos 2251 Debris TLEs
        ↓
Skyfield Orbital Propagation
        ↓
Altitude Overlap Filtering
        ↓
Distance Computation
        ↓
Risk Classification
        ↓
FastAPI Backend
        ↓
React + CesiumJS Dashboard
```

---

## Screenshots

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/4e3230d3-e8b4-412f-a7fe-3298cbbae45d" />

---

## Future Improvements

* Visualization of debris orbit trails
* Time-based orbit animation
* Satellite search and filtering
* Historical close-approach analysis
* Real-time monitoring pipeline
* Support for additional debris catalogs
* Collision probability estimation
