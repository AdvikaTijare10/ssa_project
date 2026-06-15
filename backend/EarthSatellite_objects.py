from skyfield.api import EarthSatellite


def get_EarthSatellite_obj(line1,line2,satName):
    return EarthSatellite(line1,line2,satName)

def return_EarthSatellite_obj_iss(satName,catnr,line1,line2):
    return {
        "name": satName,
        "catnr": catnr,
        "EarthSatelliteObj": get_EarthSatellite_obj(line1, line2, satName)
    }



def return_EarthSatellite_obj_debris(satellites):
    debris_obj=[]
    for sat in satellites:
        debris_obj.append({
            "name":sat["objName"],
            "catnr":sat["catnr"],
            "EarthSatelliteObj":get_EarthSatellite_obj(sat["line1"],sat["line2"],sat["objName"])
        })
    return debris_obj