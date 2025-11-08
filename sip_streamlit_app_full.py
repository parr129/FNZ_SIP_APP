# sip_streamlit_app_full.py

import streamlit as st
import pandas as pd
import numpy as np
from allocation_module import recommend_allocation

st.set_page_config(page_title="FNZ SIP App", layout="wide")

st.title("FNZ – Wealth Growth & SIP Analytics Platform")

st.markdown("""
This mini–project contains:
- SIP Future Value Calculator (Home Page)
- Risk Based Asset Allocation Recommendation
- Full Backtesting System
- Goal Calculator
- Fund Comparison


""")

st.subheader("1) SIP Calculator")

monthly = st.number_input("Monthly SIP Amount (₹)", min_value=100, value=2000, step=100)
years = st.slider("Investment Duration (years)", 1, 50, 10)
expected_return = st.number_input("Expected Annual Return (%)", min_value=1.0, value=12.0, step=0.1)

if st.button("Calculate Future Value"):
    r = expected_return/100
    n = years*12
    mr = r/12

    if mr == 0:
        fv = monthly * n
    else:
        fv = monthly * (((1+mr)**n - 1) / mr) * (1+mr)

    invested = monthly * n
    profit = fv - invested
    st.metric("Total Invested (₹)", f"{invested:,.2f}")
    st.metric("Estimated Corpus (₹)", f"{fv:,.2f}")
    st.metric("Gain / Profit (₹)", f"{profit:,.2f}")

    # graph
    values = []
    amt = 0
    for i in range(1, int(n)+1):
        amt = (amt + monthly)*(1+mr)
        values.append(amt)
    df = pd.DataFrame({"Month": range(1,int(n)+1), "Value": values})
    st.line_chart(df.set_index("Month")["Value"])


st.subheader("2) Risk Based Allocation Recommendation")

risk_score = st.slider("Risk score (1 = low risk, 10 = high risk)", 1, 10, 5)

if st.button("Recommend Allocation"):
    equity, debt = recommend_allocation(risk_score, years)
    gold = max(0, 100 - equity - debt)
    st.write("Recommended Portfolio Split:")
    st.metric("Equity", f"{equity}%")
    st.metric("Debt", f"{debt}%")
    st.metric("Gold", f"{gold}%")

st.info("Use the side menu (Pages) for Backtesting / Goal Tracking / Fund Comparison.")
