from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "GridMind Backend Connected"
    }


@app.get("/grid_status")
def grid_status():

    return {
        "mode": "NORMAL",
        "hospital_demand": 20,
        "battery_reserve": 120,
        "solar_generation": 50,
        "ev_requests": 200,
        "transformer_load": 80,
        "carbon_intensity": "Medium",
        "resilience_score": 78
    }


@app.get("/simulate_emergency")
def simulate_emergency():

    return {
        "mode": "EMERGENCY",
        "hospital_demand": 100,
        "battery_reserve": 120,
        "solar_generation": 30,
        "ev_requests": 250,
        "transformer_load": 88,
        "carbon_intensity": "High",
        "resilience_score": 42
    }

@app.get("/predict_risk")
def predict_risk(emergency: bool = False):

    if emergency:
        transformer_load = 88
        hospital_demand = 100
        resilience_score = 42

    else:
        transformer_load = 80
        hospital_demand = 20
        resilience_score = 78

    if transformer_load > 85:
        congestion_risk = "HIGH"
    elif transformer_load > 70:
        congestion_risk = "MEDIUM"
    else:
        congestion_risk = "LOW"

    if hospital_demand > 80:
        hospital_risk = "HIGH"
    elif hospital_demand > 50:
        hospital_risk = "MEDIUM"
    else:
        hospital_risk = "LOW"

    if resilience_score < 50:
        blackout_risk = "HIGH"
    elif resilience_score < 70:
        blackout_risk = "MEDIUM"
    else:
        blackout_risk = "LOW"

    return {
        "congestion_risk": congestion_risk,
        "hospital_risk": hospital_risk,
        "blackout_risk": blackout_risk
    }

@app.get("/negotiate_energy")
def negotiate_energy():

    hospital_need = 100

    battery_available = 60
    solar_available = 30

    supplied = battery_available + solar_available

    remaining = hospital_need - supplied

    if remaining < 0:
        remaining = 0

    ev_deferral = remaining

    supplied += ev_deferral

    return {
        "hospital_need": hospital_need,
        "battery_contribution": battery_available,
        "solar_contribution": solar_available,
        "ev_deferral": ev_deferral,
        "hospital_supplied": supplied
    }

@app.get("/self_heal")
def self_heal():

    actions = [
        "Pause EV Charging",
        "Activate Battery Reserve",
        "Redirect Solar Energy",
        "Prioritize Hospital Supply"
    ]

    return {
        "status": "SELF-HEALING ACTIVATED",
        "actions": actions
    }

@app.get("/explain_decision")
def explain_decision():

    return {
        "decision": "Pause EV Charging",
        "reasons": [
            "Flood Alert Active",
            "Hospital Demand Critical",
            "Transformer Load Above 85%",
            "Grid Resilience Score Below 50"
        ]
    }

@app.get("/resilience_recovery")
def resilience_recovery():

    return {
        "before_score": 42,
        "after_score": 89,
        "improvement": 47,
        "status": "GRID STABILIZED"
    }

@app.get("/event_log")
def event_log():

    return {
        "events": [
            "Flood Alert Triggered",
            "Risk Analysis Completed",
            "Energy Negotiation Started",
            "Battery Reserve Activated",
            "EV Charging Deferred",
            "Hospital Fully Powered",
            "Grid Stabilized"
        ]
    }