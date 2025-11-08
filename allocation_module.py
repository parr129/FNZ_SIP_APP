# allocation_module.py

def recommend_allocation(risk, years):
    """
    Simple rule-based allocation logic.
    Higher risk + longer duration => more Equity

    Returns:
        equity_percent (int), debt_percent (int)
    """
    # Ensure inputs are within expected ranges
    try:
        risk_val = int(risk)
    except Exception:
        risk_val = 5
    if risk_val < 1:
        risk_val = 1
    if risk_val > 10:
        risk_val = 10

    try:
        years_val = int(years)
    except Exception:
        years_val = 5
    if years_val < 0:
        years_val = 0

    # Base allocation formula: weight risk heavier, years slightly increases equity
    equity = min(90, (risk_val * 8) + (years_val * 1))
    debt = max(0, 100 - equity)

    return int(equity), int(debt)
