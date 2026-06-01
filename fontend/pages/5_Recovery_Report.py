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