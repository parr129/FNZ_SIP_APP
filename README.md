# FNZ SIP App (Streamlit)

This is a Streamlit based SIP (Systematic Investment Plan) financial utility app.

It now supports:

| Feature | Description |
|--------|-------------|
| SIP Calculator | Calculates final maturity value for a given monthly SIP amount, time period and interest |
| Goal Tracking | Calculates how much monthly SIP is needed to reach a goal |
| Fund Comparison | Shows performance comparison of sample mutual funds |
| Backtest SIP | Simulated SIP backtesting on price series (dummy prices for now) |

---

## ✅ Live App

https://fnzsipapp-keshav.streamlit.app/

---

## Files in the Repo

| File | Description |
|------|-------------|
| `sip_streamlit_app_full.py` | Main Streamlit App |
| `requirements.txt` | Python dependencies |
| `README.md` | documentation (this file) |

---

## How To Run Locally

```bash
pip install -r requirements.txt
streamlit run sip_streamlit_app_full.py
