from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/visualization")
def get_visualization():

    with open("results1.json", "r") as f:
        risk_data = json.load(f)

    with open("result2.json", "r") as f:
        visual_data = json.load(f)

    risk_lookup = {}

    for item in risk_data:
        risk_lookup[item["catnr"]] = item

    for debris in visual_data["debris"]:

        catnr = debris["catnr"]

        if catnr in risk_lookup:

            debris["status"] = risk_lookup[catnr]["status"]
            debris["min_distance_km"] = risk_lookup[catnr]["min_distance_km"]
            debris["closest_time"] = risk_lookup[catnr]["time"]

    return visual_data