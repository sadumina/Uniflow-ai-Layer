from app.schemas import RiskInput, RiskOutput

def predict_risk(r: RiskInput) -> RiskOutput:
    score = 0
    reasons = []

    # Low productivity increases risk
    if r.productivity_score < 40:
        score += 35
        reasons.append("Low productivity score (< 40).")
    elif r.productivity_score < 70:
        score += 20
        reasons.append("Moderate productivity score (< 70).")
    else:
        score += 10

    # Workload impact
    if r.workload_level == "High":
        score += 35
        reasons.append("High workload level.")
    elif r.workload_level == "Medium":
        score += 20
        reasons.append("Medium workload level.")
    else:
        score += 10

    # Deadline closeness
    if r.deadline_days <= 2:
        score += 20
        reasons.append("Deadline is very close.")
    elif r.deadline_days <= 7:
        score += 10
        reasons.append("Deadline is within a week.")

    # Missed deadlines history
    if r.missed_deadlines_last_2_weeks >= 2:
        score += 20
        reasons.append("Multiple missed deadlines in the last 2 weeks.")
    elif r.missed_deadlines_last_2_weeks == 1:
        score += 10
        reasons.append("One missed deadline in the last 2 weeks.")

    score = max(0, min(100, score))

    if score >= 70:
        level = "High"
    elif score >= 40:
        level = "Medium"
    else:
        level = "Low"

    return RiskOutput(risk_level=level, risk_score=score, reasons=reasons)
