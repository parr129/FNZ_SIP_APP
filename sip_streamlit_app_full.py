import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.set_page_config(page_title="SIP Engine", layout="wide")

# ------------------- SIDE BAR -------------------
with st.sidebar:
    st.header("📌 Navigation")
    page = st.radio("Select Feature",
                    ["SIP Calculator",
                     "Goal Tracking",
                     "Fund Comparison",
                     "Backtest SIP"])

    st.markdown("---")
    st.caption("Built by Keshav")


# ------------------- feature functions -------------------
def calculate_final_value(monthly_invest, years, rate):
    n = years * 12
    r = rate / 12 / 100
    fv = monthly_invest * (((1 + r) ** n - 1) / r) * (1 + r)
    return fv


def backtest_sip(df_prices, monthly):
    units = 0
    total_invested = 0
    for px in df_prices["price"]:
        units += monthly / px
        total_invested += monthly
    final_value = units * df_prices["price"].iloc[-1]
    return final_value, total_invested


# ------------------- MAIN PAGES -------------------

if page == "SIP Calculator":
    st.title("SIP Calculator")

    m = st.number_input("Monthly SIP Amount", 500, 100000, 2000)
    y = st.slider("Duration (years)", 1, 40, 10)
    r = st.slider("Expected return % p.a", 5.0, 20.0, 12.0)

    fv = calculate_final_value(m, y, r)
    st.success(f"Final Value ≈ ₹{fv:,.0f}")

    st.metric("Total Invested", f"₹{m*12*y:,.0f}")
    st.metric("Profit", f"₹{fv - (m*12*y):,.0f}")


elif page == "Goal Tracking":
    st.title("🎯 Goal Tracking")

    goal = st.number_input("Goal Amount", 10000, 50000000, 1000000)
    years = st.slider("Years to Achieve Goal", 1, 30, 10)
    return_assumed = st.slider("Assumed Return %", 6.0, 18.0, 12.0)

    r = return_assumed/12/100
    n = years*12
    required_monthly = goal / (((1+r)**n -1)/r * (1+r))

    st.info(f"Required Monthly SIP → **₹{required_monthly:,.0f}**")


elif page == "Fund Comparison":
    st.title("📈 Fund Comparison")

    df = pd.DataFrame({
        "Fund": ["HDFC Growth", "Axis Bluechip", "ICICI Largecap"],
        "5Y Return%": [14.5, 12.8, 13.7],
        "Risk Score": ["Medium", "High", "Medium"]
    })

    st.dataframe(df)


elif page == "Backtest SIP":
    st.title("⏳ Backtest SIP Strategy")

    st.caption("Simplified – using dummy monthly price data")

    dfp = pd.DataFrame({"price": np.linspace(60, 120, 60)})  # 5 years

    monthly = st.number_input("Monthly SIP", 500, 100000, 2000)
    fv, inv = backtest_sip(dfp, monthly)

    st.metric("Final Value", f"₹{fv:,.0f}")
    st.metric("Invested", f"₹{inv:,.0f}")
    st.metric("Profit", f"₹{fv - inv:,.0f}")
