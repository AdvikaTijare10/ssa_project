from skyfield.api import load
from skyfield.elementslib import osculating_elements_of


def calculate_apogee_perigee_iss(iss_obj,t):
   
    earth_radius=6378.14
    position=iss_obj["EarthSatelliteObj"].at(t)
    elements=osculating_elements_of(position)
    semi_major_axis=elements.semi_major_axis.km
    eccentricity=elements.eccentricity
    apogee=semi_major_axis*(1+eccentricity)-earth_radius #-beocz we want from earth surface and not the center of earth
    perigee=semi_major_axis*(1-eccentricity)-earth_radius
    return {"apogee":apogee,"perigee":perigee,"EarthSatelliteObj":iss_obj["EarthSatelliteObj"]}
    
   

def calculate_apogee_perigee_debris(debris_obj,t):
    earth_radius=6378.14
    apogee_perigee_calc=[]
    for debris in debris_obj:
        position=debris["EarthSatelliteObj"].at(t)
        elements=osculating_elements_of(position)
        semi_major_axis=elements.semi_major_axis.km
        eccentricity=elements.eccentricity
        apogee=semi_major_axis*(1+eccentricity)-earth_radius
        perigee=semi_major_axis*(1-eccentricity)-earth_radius
        apogee_perigee_calc.append({
            "name":debris["name"],
            "catnr":debris["catnr"],
            "apogee":apogee,
            "perigee":perigee,
            "EarthSatelliteObj":debris["EarthSatelliteObj"]
        })
    return apogee_perigee_calc
