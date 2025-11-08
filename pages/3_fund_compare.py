# pages/3_fund_compare.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Fund Comparison (sample)")

# sample fund dataset
funds = pd.DataFrame([
    {'symbol':'FUND_A','name':'Alpha Growth Fund','1y':0.12,'3y':0.35,'5y':0.60,'expense_ratio':0.01},
    {'symbol':'FUND_B','name':'Beta Equity Fund','1y':0.08,'3y':0.25,'5y':0.50,'expense_ratio':0.015},
    {'symbol':'FUND_C','name':'Gamma Balanced Fund','1y':0.10,'3y':0.30,'5y':0.55,'expense_ratio':0.012},
])
st.write('Available funds:')
st.dataframe(funds[['symbol','name','1y','3y','5y','expense_ratio']])

left, right = st.columns(2)
with left:
    f1 = st.selectbox("Select Fund 1", funds['symbol'])
with right:
    f2 = st.selectbox("Select Fund 2", funds['symbol'], index=1)

if st.button("Compare"):
    a = funds[funds['symbol']==f1].iloc[0]
    b = funds[funds['symbol']==f2].iloc[0]
    comp = pd.DataFrame({
        'metric':['1y','3y','5y','expense_ratio'],
        f1:[a['1y'],a['3y'],a['5y'],a['expense_ratio']],
        f2:[b['1y'],b['3y'],b['5y'],b['expense_ratio']]
    })
    st.table(comp)
    # simple bar chart for returns
    fig, ax = plt.subplots()
    ind = range(3)
    ax.bar([x-0.15 for x in ind],[a['1y'],a['3y'],a['5y']],width=0.3,label=f1)
    ax.bar([x+0.15 for x in ind],[b['1y'],b['3y'],b['5y']],width=0.3,label=f2)
    ax.set_xticks(ind)
    ax.set_xticklabels(['1y','3y','5y'])
    ax.set_ylabel('Return (decimal)')
    ax.legend()
    st.pyplot(fig)
