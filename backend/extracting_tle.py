import requests
import json
from skyfield.api import wgs84,EarthSatellite,load 

def get_tle_iss(urlsat):
    response=requests.get(urlsat)
    lines=response.text.strip().split("\n")
    satName=lines[0]
    line1=lines[1]
    line2=lines[2]
    catnr=line2.split()[1]
    return satName,catnr,line1,line2

def get_tle_debris(urlDebris):
    response=requests.get(urlDebris)
    lines=response.text.strip().split("\n")
    debris_tle=[]
    for i in range(0,len(lines),3):
        debris_tle.append({
            "objName":lines[i],
            "catnr":lines[i+2].split()[1],
            "line1":lines[i+1],
            "line2":lines[i+2]
           })
        
    return debris_tle
    

