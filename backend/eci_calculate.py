from skyfield.api import load

def calculate_xyz(iss_apogee_perigee, close_debris, t):
    issObj = iss_apogee_perigee["EarthSatelliteObj"].at(t)
    ix, iy, iz = issObj.position.km

    debris = []

    for debri in close_debris:
        debrisObj = debri["EarthSatelliteObj"].at(t)
        dx, dy, dz = debrisObj.position.km

        debris.append({
            "catnr": debri["catnr"],
            "x": dx,
            "y": dy,
            "z": dz
        })

    return {
        "time": t,
        "iss": {"x": ix, "y": iy, "z": iz},
        "debris": debris
    }