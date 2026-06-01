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
