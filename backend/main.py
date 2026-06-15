from extracting_tle import get_tle_debris,get_tle_iss
from EarthSatellite_objects import return_EarthSatellite_obj_iss,return_EarthSatellite_obj_debris
from get_apogee_perigee import calculate_apogee_perigee_iss,calculate_apogee_perigee_debris
from altitude_overlap_filter import altitude_filter
from eci_calculate import calculate_xyz
from visualization_data import calculate
from skyfield.api import load
from euclidDistance import distances_between
from datetime import datetime, timedelta, timezone
import json

urlsat = "https://celestrak.org/NORAD/elements/gp.php?CATNR=25544&FORMAT=TLE"
urlDebris = "https://celestrak.org/NORAD/elements/gp.php?GROUP=cosmos-2251-debris&FORMAT=TLE"


satName,catnr,line1,line2=get_tle_iss(urlsat)
iss_obj=return_EarthSatellite_obj_iss(satName,catnr,line1,line2)

satellites=get_tle_debris(urlDebris)
debris_obj=return_EarthSatellite_obj_debris(satellites)
ts=load.timescale()
t=ts.now()
iss_apogee_perigee=calculate_apogee_perigee_iss(iss_obj,t)

debris_apogee_perigee=calculate_apogee_perigee_debris(debris_obj,t)


close_debris=altitude_filter(iss_apogee_perigee,debris_apogee_perigee)


start = datetime.now(timezone.utc)

dist_prop = []

for i in range(0, 24*60, 5):
    t = ts.from_datetime(start + timedelta(minutes=i))

    x_y_z_coord = calculate_xyz(iss_apogee_perigee, close_debris, t)
    distancee = distances_between(x_y_z_coord)

    dist_prop.append({
        "time": t.utc_iso(),
        "distances": distancee
    })
minimums = {}

for result in dist_prop:

    current_time = result["time"]

    for debris in result["distances"]:

        catnr = debris["catnr"]
        distance = debris["distance"]

        if catnr not in minimums:

            minimums[catnr] = {
                "distance": distance,
                "time": current_time
            }

        elif distance < minimums[catnr]["distance"]:

            minimums[catnr] = {
                "distance": distance,
                "time": current_time
            }
result=[]
for catnr,data in minimums.items():
    distance=data["distance"]
    if distance<=1500:
        color="red"
    elif distance>1500 and distance<5000:
        color="yellow"
    else:
        color="green"    
    result.append({"catnr":catnr,"min_distance_km":round(data["distance"],2),"time":data["time"],"status":color})

with open("results1.json","w") as f:
    json.dump(result,f,indent=5)

coord_overtime=calculate(result)

with open("result2.json","w") as f:
    json.dump(coord_overtime,f,indent=4)


