# allocation_module.py
def recommend_allocation(risk, years):
    """Return equity%, debt% based on simple rule."""
    try:
        risk_val = int(risk)
    except Exception:
        risk_val = 5
    risk_val = max(1, min(10, risk_val))
    try:
        years_val = int(years)
    except Exception:
        years_val = 5
    years_val = max(0, years_val)
    equity = min(90, (risk_val * 8) + (years_val * 1))
    debt = max(0, 100 - equity)
    return int(equity), int(debt)
