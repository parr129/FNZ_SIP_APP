# allocation_module.py

def recommend_allocation(risk, years):
    """
    Simple rule-based allocation logic.
    Higher risk + longer duration ⇒ more Equity

    Returns:
        equity_percent, debt_percent
    """

    # Base allocation formula
    equity = min(90, (risk * 8) + (years * 1))

    # Debt is always the complement
    debt = 100 - equity

    return equity, debt
