from fastapi import FastAPI
from app.schemas import (
    TaskInput, PriorityOutput,
    WorkloadInput, WorkloadOutput,
    RiskInput, RiskOutput,
    RecommendationInput, RecommendationOutput
)
from app.engine.task_priority import calculate_priority
from app.engine.workload import analyze_workload
from app.engine.risk import predict_risk
from app.engine.recommendations import generate_recommendations

app = FastAPI(title="UniFlow+ AI Layer", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": "uniflow-ai-layer"}

@app.post("/ai/task-priority", response_model=PriorityOutput)
def task_priority(payload: TaskInput):
    return calculate_priority(payload)

@app.post("/ai/workload", response_model=WorkloadOutput)
def workload(payload: WorkloadInput):
    return analyze_workload(payload)

@app.post("/ai/risk", response_model=RiskOutput)
def risk(payload: RiskInput):
    return predict_risk(payload)

@app.post("/ai/recommendations", response_model=RecommendationOutput)
def recommendations(payload: RecommendationInput):
    return generate_recommendations(payload)
