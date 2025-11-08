# pages/2_goal_tracker.py
import streamlit as st
import numpy as np

st.title("Goal Tracker - Calculate required SIP for target corpus")

target = st.number_input("Target corpus (₹)", min_value=1000, value=1000000, step=1000)
years = st.slider("Years to achieve", 1, 40, 10)
expected_return = st.number_input("Expected annual return (%)", min_value=0.0, value=10.0, step=0.1)

if st.button("Calculate required SIP"):
    r = expected_return/100
    n = years*12
    # SIP future value formula: FV = P * [ ( (1+r/12)^n -1 ) / (r/12) ] * (1+r/12)
    mr = r/12
    if mr == 0:
        sip = target / n
    else:
        factor = ((1+mr)**n - 1) / mr
        sip = target / (factor * (1+mr))
    st.metric("Required Monthly SIP (₹)", f"{sip:,.0f}")
    # show shortfall if user already invests some SIP
    current_sip = st.number_input("Current monthly SIP (₹)", min_value=0, value=0, step=100)
    if current_sip>0:
        contribution = current_sip * factor * (1+mr)
        shortfall = max(0, target - contribution)
        st.write(f"If you continue with ₹{current_sip} per month, estimated corpus = ₹{contribution:,.0f}")
        if shortfall>0:
            st.warning(f"Shortfall: ₹{shortfall:,.0f}. Increase SIP or extend tenure.")
