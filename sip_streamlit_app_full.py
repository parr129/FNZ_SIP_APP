# sip_streamlit_app_full.py (v3 with CSV history + nicer pie)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from allocation_module import recommend_allocation
import os

st.set_page_config(page_title="Wealth Growth Analytics Dashboard", layout="centered")

def calculate_sip(monthly, annual_rate_percent, years):
    months = int(years * 12)
    monthly_rate = (annual_rate_percent / 100) / 12
    balance = 0.0
    balances = []
    for m in range(1, months+1):
        balance = (balance + monthly) * (1 + monthly_rate)
        balances.append((m, balance))
    total_invested = monthly * months
    profit = balance - total_invested
    return total_invested, balance, profit, balances

def calculate_cagr(initial, final, years):
    if initial <= 0 or years <= 0:
        return None
    return (final / initial) ** (1.0 / years) - 1.0

st.title("Wealth Growth Analytics Dashboard (FNZ Mini V3)")

mode = st.sidebar.radio("Mode", ["SIP"])
risk = st.sidebar.slider("Risk Score (1-10)", 1, 10, 5)
years = st.sidebar.slider("Duration (years)", 1, 30, 5)

monthly = st.number_input("Monthly Investment (₹)", min_value=0, value=2000, step=500)
rate = st.number_input("Expected Annual Return (%)", min_value=0.0, value=12.0, step=0.1)

if st.button("Calculate SIP"):
    invested, fv, profit, balances = calculate_sip(monthly, rate, years)
    st.metric("Total Invested (₹)", f"{invested:,.2f}")
    st.metric("Final Value (₹)", f"{fv:,.2f}")
    st.metric("Profit (₹)", f"{profit:,.2f}")
    cagr = calculate_cagr(invested, fv, years)
    if cagr is not None:
        st.metric("Approx CAGR (annual)", f"{cagr*100:.2f}%")

    df = pd.DataFrame(balances, columns=["Month", "Value"])
    fig, ax = plt.subplots(figsize=(8,3))
    ax.plot(df["Month"], df["Value"])
    st.pyplot(fig)

    equity, debt = recommend_allocation(risk, years)
    fig2, ax2 = plt.subplots(figsize=(4,3))
    ax2.pie([equity, debt], autopct='%1.1f%%', startangle=90, wedgeprops={"edgecolor":"black"})
    st.pyplot(fig2)

    # CSV logging history
    row = {"risk":risk,"years":years,"equity":equity,"debt":debt,"final_value":fv,"invested":invested}
    if os.path.exists("history.csv"):
        hist = pd.read_csv("history.csv")
        hist = pd.concat([hist, pd.DataFrame([row])], ignore_index=True)
    else:
        hist = pd.DataFrame([row])
    hist.to_csv("history.csv", index=False)
    st.dataframe(hist)

    st.download_button("Download Growth CSV", df.to_csv(index=False).encode("utf-8"), "sip_growth.csv")
