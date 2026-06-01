import streamlit as st
import requests
import pandas as pd
import pydeck as pdk
import streamlit as st

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

st.title("🛰 Grid Control Center")

if st.button("🚨 Simulate Flood Emergency"):
    st.session_state.emergency = True

if st.session_state.emergency:
    response = requests.get(
        "http://localhost:8000/simulate_emergency"
    )
else:
    response = requests.get(
        "http://localhost:8000/grid_status"
    )

data = response.json()

if data["mode"] == "NORMAL":
    st.success("🟢 NORMAL MODE")
else:
    st.error("🔴 EMERGENCY MODE")

col1,col2,col3=st.columns(3)

with col1:
    st.metric("Hospital",data["hospital_demand"])

with col2:
    st.metric("Battery",data["battery_reserve"])

with col3:
    st.metric("Resilience",data["resilience_score"])

st.subheader("📍 Grid Emergency Map")

map_data = pd.DataFrame([
    {
        "lat":12.97,
        "lon":77.59,
        "risk":90 if st.session_state.emergency else 20
    }
])

st.pydeck_chart(
    pdk.Deck(
        initial_view_state=pdk.ViewState(
            latitude=12.97,
            longitude=77.59,
            zoom=10
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=map_data,
                get_position='[lon, lat]',
                get_radius='risk * 100',
            )
        ]
    )
)