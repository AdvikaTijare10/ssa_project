
from datetime import datetime, timedelta, timezone
from skyfield.api import load, EarthSatellite,wgs84
import requests

start = datetime.now(timezone.utc)

urldebris = "https://celestrak.org/NORAD/elements/gp.php"

overtime_coord = {
    "generated_at": start.isoformat(),
    "iss": {},
    "debris": []
}


def get_tle(catnr):
    response = requests.get(
        urldebris,
        params={"CATNR": catnr, "FORMAT": "TLE"}
    )

    lines = response.text.strip().split("\n")

    return lines[0], lines[1], lines[2]


ts = load.timescale()

# ISS DATA
iss_trail = []

objName, line1, line2 = get_tle(25544)

iss_obj = EarthSatellite(line1, line2, objName, ts)

for i in range(0,93,1):

    t = ts.from_datetime(start + timedelta(minutes=i))

    pos = iss_obj.at(t)

    subpoint = wgs84.subpoint(pos)

    lat = subpoint.latitude.degrees
    lon = subpoint.longitude.degrees
    alt = subpoint.elevation.km

    iss_trail.append({
        "time": t.utc_iso(),
        "latitude": float(lat),
        "longitude": float(lon),
        "altitude_km": float(alt)
    })

pos = iss_obj.at(ts.from_datetime(start))

subpoint = wgs84.subpoint(pos)

lat = subpoint.latitude.degrees
lon = subpoint.longitude.degrees
alt = subpoint.elevation.km

overtime_coord["iss"] = {
    "current_position": {
        "latitude": float(lat),
        "longitude": float(lon),
        "altitude_km": float(alt)
    },
    "orbit_trail": iss_trail
}


def calculate(result):

    for debris in result:

        objName, line1, line2 = get_tle(debris["catnr"])

        sat = EarthSatellite(line1, line2, objName, ts)

        trail = []

        for i in range(0,93,1):

            t = ts.from_datetime(start + timedelta(minutes=i))

            pos = sat.at(t)

            subpoint = wgs84.subpoint(pos)

            lat = subpoint.latitude.degrees
            lon = subpoint.longitude.degrees
            alt = subpoint.elevation.km

            trail.append({
                "time": t.utc_iso(),
                "latitude": float(lat),
                "longitude": float(lon),
                "altitude_km": float(alt)
            })

        current_pos = sat.at(ts.from_datetime(start))

        subpoint = wgs84.subpoint(current_pos)

        lat = subpoint.latitude.degrees
        lon = subpoint.longitude.degrees
        alt = subpoint.elevation.km

        overtime_coord["debris"].append({

            "catnr": debris["catnr"],

            "min_distance": debris["min_distance_km"],

            "closest_time": debris["time"],

            "current_position": {
                "latitude": float(lat),
                "longitude": float(lon),
                "altitude_km": float(alt)
            },

            "orbit_trail": trail
        })

    return overtime_coord