import streamlit as st
import requests

st.set_page_config(
    page_title="GridMind",
    layout="wide"
)

st.title("⚡ GridMind")
st.subheader("Hybrid-Intelligence Smart Grid Dashboard")

# ------------------------
# STATE MANAGEMENT
# ------------------------

if "emergency" not in st.session_state:
    st.session_state.emergency = False

# ------------------------
# BUTTON
# ------------------------

if st.button("🚨 Simulate Flood Emergency"):
    st.session_state.emergency = True

# ------------------------
# API CALL
# ------------------------

if st.session_state.emergency:

    response = requests.get(
        "http://localhost:8000/simulate_emergency"
    )

else:

    response = requests.get(
        "http://localhost:8000/grid_status"
    )

data = response.json()

# ------------------------
# MODE DISPLAY
# ------------------------

if data["mode"] == "NORMAL":
    st.success("🟢 NORMAL MODE")
else:
    st.error("🔴 EMERGENCY MODE")
st.divider()

st.subheader("⚙ GridMind Orchestration Engine")
if st.session_state.emergency:

    st.progress(100)

    st.write(
        "GridMind Emergency Response Workflow Completed"
    )
else:

    st.success(
        "Flood Emergency Detected"
    )

    st.success(
        "✓ Risk Prediction Completed"
    )

    st.success(
        "✓ Energy Negotiation Completed"
    )

    st.success(
        "✓ Self-Healing Actions Executed"
    )

    st.success(
        "✓ Explainable AI Generated"
    )

    st.success(
        "✓ Grid Stabilized"
    )
# ------------------------
# METRICS
# ------------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "🏥 Hospital Demand",
        f"{data['hospital_demand']} kWh"
    )

    st.metric(
        "🔋 Battery Reserve",
        f"{data['battery_reserve']} kWh"
    )

with col2:

    st.metric(
        "☀ Solar Generation",
        f"{data['solar_generation']} kWh"
    )

    st.metric(
        "🚗 EV Requests",
        data["ev_requests"]
    )

with col3:

    st.metric(
        "⚙ Transformer Load",
        f"{data['transformer_load']}%"
    )

    st.metric(
        "🌍 Resilience Score",
        data["resilience_score"]
    )

st.divider()

st.info(
    f"Carbon Intensity: {data['carbon_intensity']}"
)

st.divider()

st.subheader("📈 Risk Prediction Engine")

risk_response = requests.get(
    f"http://localhost:8000/predict_risk?emergency={st.session_state.emergency}"
)

risk_data = risk_response.json()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "⚠ Congestion Risk",
        risk_data["congestion_risk"]
    )

with col2:
    st.metric(
        "🏥 Hospital Risk",
        risk_data["hospital_risk"]
    )

with col3:
    st.metric(
        "⚡ Blackout Risk",
        risk_data["blackout_risk"]
    )

st.divider()

st.subheader("🤝 Energy Negotiation Engine")

if st.session_state.emergency:

    negotiation_response = requests.get(
        "http://localhost:8000/negotiate_energy"
    )

    negotiation = negotiation_response.json()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🔋 Battery Contribution",
            f"{negotiation['battery_contribution']} kWh"
        )

    with col2:
        st.metric(
            "☀ Solar Contribution",
            f"{negotiation['solar_contribution']} kWh"
        )

    with col3:
        st.metric(
            "🚗 EV Deferral",
            f"{negotiation['ev_deferral']} kWh"
        )

    st.success(
        f"🏥 Hospital Successfully Supplied "
        f"{negotiation['hospital_supplied']} kWh"
    )

    st.write("### Negotiation Outcome")

    st.write(
        "🔋 Battery → Hospital"
    )

    st.write(
        "☀ Solar → Hospital"
    )

    st.write(
        "🚗 EV Charging Deferred"
    )

st.divider()

st.subheader("🛠 Self-Healing Engine")

if st.session_state.emergency:

    heal_response = requests.get(
        "http://localhost:8000/self_heal"
    )

    heal_data = heal_response.json()

    st.warning(
        heal_data["status"]
    )

    st.write("### Automated Actions")

    for i, action in enumerate(
        heal_data["actions"],
        start=1
    ):
        st.write(
            f"{i}. {action}"
        )

st.divider()

st.subheader("🧠 Explainable AI Engine")

if st.session_state.emergency:

    explain_response = requests.get(
        "http://localhost:8000/explain_decision"
    )

    explain_data = explain_response.json()

    st.info(
        f"Decision: {explain_data['decision']}"
    )

    st.write("### Why was this decision taken?")

    for reason in explain_data["reasons"]:
        st.success(reason)

st.divider()

st.subheader("🌍 Grid Resilience Recovery")

if st.session_state.emergency:

    recovery_response = requests.get(
        "http://localhost:8000/resilience_recovery"
    )

    recovery_data = recovery_response.json()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Before GridMind",
            recovery_data["before_score"]
        )

    with col2:
        st.metric(
            "After GridMind",
            recovery_data["after_score"],
            delta=recovery_data["improvement"]
        )

    st.success(
        recovery_data["status"]
    )
    st.progress(
    recovery_data["after_score"] / 100
    )
    st.write(
    f"Grid resilience improved by "
    f"{recovery_data['improvement']} points."
    )

st.divider()

st.subheader("📜 Event Timeline & Audit Trail")

if st.session_state.emergency:

    log_response = requests.get(
        "http://localhost:8000/event_log"
    )

    log_data = log_response.json()


    for event in log_data["events"]:
        st.markdown(
            f"➡️ {event}"
        )
    
st.divider()

st.subheader("🎯 GridMind Impact Summary")

if st.session_state.emergency:

    st.metric(
        "Grid Status",
        "STABILIZED"
    )

    st.metric(
        "Hospital Power Restored",
        "100%"
    )

    st.metric(
        "Blackout Prevented",
        "YES"
    )

    st.metric(
        "Resilience Improvement",
        "+47"
    )