import streamlit as st
from allocation_module import recommend_allocation

# Page Setup
st.set_page_config(
    page_title="FNZ SIP Allocator",
    layout="centered"
)

# Sidebar
st.sidebar.title("⚙️ Controls")
st.sidebar.write("Select parameters to calculate recommended investment allocation.")

st.title("💰 FNZ SIP Allocation Advisor")
st.write("A simple wealth allocation recommendation engine for FNZ use-case")

# Inputs layout
col1, col2 = st.columns(2)

with col1:
    risk_score = st.slider("Risk Score (1 = very safe | 10 = high risk)", 1, 10, 5)

with col2:
    years = st.slider("Investment Duration (years)", 1, 30, 10)

monthly = st.number_input("Monthly SIP Amount (₹)", min_value=500, step=500)

# button
if st.button("Generate Allocation Recommendation"):
    equity, debt = recommend_allocation(risk_score, years)

    st.subheader("📊 Recommended Allocation")

    # result card
    st.markdown(
        f"""
        <div style="padding:20px;border-radius:15px;background-color:#1e1e1e20;">
        <h3 style="margin:0;">Equity: <span style="color:#27ae60;">{equity}%</span></h3>
        <h3 style="margin:0;">Debt: <span style="color:#c0392b;">{debt}%</span></h3>
        <br>
        <p><b>Total Monthly:</b> ₹{monthly}</p>
        <p><b>Equity Amount:</b> ₹{int(monthly * equity/100)}</p>
        <p><b>Debt Amount:</b> ₹{int(monthly * debt/100)}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

else:
    st.info("Click the button above to generate allocation recommendation.")
