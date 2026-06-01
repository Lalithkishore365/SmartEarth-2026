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

