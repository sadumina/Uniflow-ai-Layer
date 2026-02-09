from app.schemas import WorkloadInput, WorkloadOutput

def analyze_workload(w: WorkloadInput) -> WorkloadOutput:
    warnings = []
    score = 0

    # Base score from total hours
    if w.total_estimated_hours >= 20:
        score += 40
        warnings.append("Total estimated study hours are high (≥ 20).")
    elif w.total_estimated_hours >= 12:
        score += 25
        warnings.append("Total estimated study hours are moderate (≥ 12).")
    else:
        score += 10

    # Task count contribution
    if w.tasks_this_week >= 7:
        score += 35
        warnings.append("Too many tasks scheduled this week (≥ 7).")
    elif w.tasks_this_week >= 4:
        score += 20
    else:
        score += 10

    # High difficulty tasks
    if w.high_difficulty_tasks >= 3:
        score += 25
        warnings.append("Multiple high-difficulty tasks in the same week (≥ 3).")
    elif w.high_difficulty_tasks >= 1:
        score += 15
    else:
        score += 5

    # Academic year adjustment
    if w.academic_year == 4:
        score += 5
        warnings.append("Final-year students should plan earlier due to higher workload.")

    score = max(0, min(100, score))

    if score >= 70:
        level = "High"
    elif score >= 40:
        level = "Medium"
    else:
        level = "Low"

    return WorkloadOutput(workload_level=level, workload_score=score, warnings=warnings)
