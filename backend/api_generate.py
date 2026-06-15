import json
from fastapi import FastAPI
app=FastAPI()

@app.get("/visualization")
def get_visualization():
    with open("visualization_data.json", "r") as f:
        data = json.load(f)

    return data

