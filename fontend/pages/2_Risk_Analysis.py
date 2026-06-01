import streamlit as st
import requests
if "emergency" not in st.session_state:
    st.session_state.emergency = False
with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2942/2942789.png",
        width=80
    )

    st.title("GridMind")

    st.caption(
        "Hybrid Intelligence Smart Grid Platform"
    )

    st.divider()

    if st.session_state.emergency:
        st.error("🔴 EMERGENCY MODE")
    else:
        st.success("🟢 NORMAL MODE")

    st.divider()

    st.metric(
        "Grid Health",
        "89%"
        if st.session_state.emergency
        else "78%"
    )

    st.metric(
        "AI Confidence",
        "96%"
    )

    st.metric(
        "Active Agents",
        "124"
    )

    st.divider()

    st.write("### Features")

    st.write("✓ Risk Prediction")
    st.write("✓ Energy Negotiation")
    st.write("✓ Self-Healing")
    st.write("✓ Explainable AI")
    st.write("✓ Resilience Recovery")
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