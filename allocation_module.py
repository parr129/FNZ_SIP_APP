# allocation_module.py
RISK_PROFILES = {
    "Conservative": {"Equity": 40, "Debt": 50, "Gold": 10},
    "Moderate": {"Equity": 60, "Debt": 35, "Gold": 5},
    "Aggressive": {"Equity": 80, "Debt": 15, "Gold": 5},
}

def recommend_allocation(profile: str):
    profile_cap = profile.capitalize()
    if profile_cap not in RISK_PROFILES:
        raise ValueError(f"Unknown profile: {profile}. Choose from {list(RISK_PROFILES.keys())}")
    return RISK_PROFILES[profile_cap]
