def calculate_reality(demand: str, competition: str, difficulty: str):

    score = 0

    # Demand (strong positive)
    if demand.lower() == "high":
        score += 3
    elif demand.lower() == "medium":
        score += 2
    else:
        score += 1

    # Competition (moderate negative)
    if competition.lower() == "high":
        score -= 2
    elif competition.lower() == "medium":
        score -= 1

    # Difficulty (moderate negative)
    if difficulty.lower() == "high":
        score -= 1
    elif difficulty.lower() == "medium":
        score -= 0.5

    # Final decision
    if score >= 2:
        return "High Feasibility"
    elif score >= 0:
        return "Moderate Feasibility"
    else:
        return "Low Feasibility"