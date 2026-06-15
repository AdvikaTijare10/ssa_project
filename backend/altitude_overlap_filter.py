def altitude_filter(iss_apogee_perigee,debris_apogee_perigee):
    close_debris=[]
    iss_apogee=iss_apogee_perigee["apogee"]
    iss_perigee=iss_apogee_perigee["perigee"]
    margin=20
    for debris in debris_apogee_perigee:
        debris_apogee=debris["apogee"]
        debris_perigee=debris["perigee"]
        if iss_apogee+margin<=debris_perigee or debris_apogee+margin<=iss_perigee:
            continue
        else:
            close_debris.append({"name":debris["name"],"catnr":debris["catnr"],"EarthSatelliteObj":debris["EarthSatelliteObj"],"apogee":debris["apogee"],"perigee":debris["perigee"]})

    return close_debris
