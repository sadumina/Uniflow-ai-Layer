from app.schemas import TaskInput, PriorityOutput

def calculate_priority(task: TaskInput) -> PriorityOutput:
    score = 0
    reasons = []

    # Deadline impact
    if task.deadline_days <= 2:
        score += 40
        reasons.append("Deadline is very close (≤ 2 days).")
    elif task.deadline_days <= 7:
        score += 25
        reasons.append("Deadline is within a week (≤ 7 days).")
    else:
        score += 10
        reasons.append("Deadline is not immediate (> 7 days).")

    # Difficulty impact
    if task.difficulty == "High":
        score += 30
        reasons.append("High difficulty task.")
    elif task.difficulty == "Medium":
        score += 20
        reasons.append("Medium difficulty task.")
    else:
        score += 10
        reasons.append("Low difficulty task.")

    # Task type impact
    if task.task_type == "Project":
        score += 20
        reasons.append("Project tasks have higher academic impact.")
    elif task.task_type == "Exam":
        score += 25
        reasons.append("Exam preparation is high priority.")
    elif task.task_type == "Assignment":
        score += 15
        reasons.append("Assignment contributes to continuous assessment.")
    else:
        score += 5
        reasons.append("Standard task type.")

    # Academic year adjustment
    if task.academic_year == 4:
        score += 10
        reasons.append("Final-year workload is typically higher.")
    elif task.academic_year == 1:
        score -= 5
        reasons.append("Year 1 tasks usually have lower complexity.")

    score = max(0, min(100, score))

    if score >= 70:
        level = "High"
    elif score >= 40:
        level = "Medium"
    else:
        level = "Low"

    return PriorityOutput(priority_score=score, priority_level=level, explanation=reasons)
