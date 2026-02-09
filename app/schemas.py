from pydantic import BaseModel, Field
from typing import List, Literal, Optional

Difficulty = Literal["Low", "Medium", "High"]
TaskType = Literal["Lab", "Assignment", "Project", "Quiz", "Exam"]

class TaskInput(BaseModel):
    academic_year: int = Field(..., ge=1, le=4)
    task_type: TaskType
    difficulty: Difficulty
    deadline_days: int = Field(..., ge=0)
    estimated_hours: float = Field(..., ge=0.5, le=200)

class PriorityOutput(BaseModel):
    priority_score: int
    priority_level: Literal["Low", "Medium", "High"]
    explanation: List[str]

class WorkloadInput(BaseModel):
    academic_year: int = Field(..., ge=1, le=4)
    tasks_this_week: int = Field(..., ge=0, le=50)
    high_difficulty_tasks: int = Field(..., ge=0, le=50)
    total_estimated_hours: float = Field(..., ge=0, le=300)

class WorkloadOutput(BaseModel):
    workload_level: Literal["Low", "Medium", "High"]
    workload_score: int
    warnings: List[str]

class RiskInput(BaseModel):
    productivity_score: int = Field(..., ge=0, le=100)
    workload_level: Literal["Low", "Medium", "High"]
    deadline_days: int = Field(..., ge=0)
    missed_deadlines_last_2_weeks: int = Field(..., ge=0, le=20)

class RiskOutput(BaseModel):
    risk_level: Literal["Low", "Medium", "High"]
    risk_score: int
    reasons: List[str]

class RecommendationInput(BaseModel):
    priority: PriorityOutput
    workload: WorkloadOutput
    risk: RiskOutput

class RecommendationOutput(BaseModel):
    recommendations: List[str]
