from app.schemas import RecommendationInput, RecommendationOutput

def generate_recommendations(x: RecommendationInput) -> RecommendationOutput:
    recs = []

    # Priority-based guidance
    if x.priority.priority_level == "High":
        recs.append("Start the highest priority task today to reduce deadline risk.")
    elif x.priority.priority_level == "Medium":
        recs.append("Schedule focused time blocks this week to complete medium priority tasks.")

    # Workload-based guidance
    if x.workload.workload_level == "High":
        recs.append("Reduce parallel tasks this week and avoid adding new tasks.")
        recs.append("Split high-difficulty tasks into smaller milestones.")
    elif x.workload.workload_level == "Medium":
        recs.append("Maintain a balanced schedule and keep daily goals realistic.")

    # Risk-based guidance
    if x.risk.risk_level == "High":
        recs.append("High academic risk detected: begin tasks early and seek peer collaboration.")
    elif x.risk.risk_level == "Medium":
        recs.append("Monitor workload and ensure consistent progress to avoid last-minute stress.")

    # Always include an explainable habit tip
    recs.append("Tip: Use 60–90 minute focus sessions with short breaks to maintain consistency.")

    return RecommendationOutput(recommendations=recs)
