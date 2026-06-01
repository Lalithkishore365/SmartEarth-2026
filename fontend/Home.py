import streamlit as st
# Session State
if "emergency" not in st.session_state:
    st.session_state.emergency = False
st.set_page_config(
    page_title="GridMind",
    layout="wide"
)
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
st.title("⚡ GridMind")

st.markdown("""
### Autonomous Multi-Agent Smart Grid Platform

AI-Powered Energy Negotiation • Self-Healing Infrastructure • Disaster Resilience
# Hybrid Intelligence Smart Grid

GridMind autonomously:

- Predicts grid risks
- Negotiates energy allocation
- Performs self-healing
- Explains every decision
- Improves grid resilience

""")
