from fastapi import FastAPI
from data_loader import load_employee_logs, load_meeting_logs
from feature_engineering import create_burnout_features
from burnout_model import load_model, predict_burnout_risk
from meeting_analyzer import add_meeting_scores
from correlation_engine import merge_burnout_meetings, calculate_meeting_overload

app = FastAPI(title="PulseGuard API")
model = load_model()

@app.get("/")
def health():
    return {"status":"PulseGuard API running"}

@app.get("/burnout-risk")
def burnout_risk():
    emp = load_employee_logs()
    meet = load_meeting_logs()
    emp = create_burnout_features(emp)
    meet = add_meeting_scores(meet)
    emp = predict_burnout_risk(model, emp)
    merged = merge_burnout_meetings(emp, meet)
    merged = calculate_meeting_overload(merged)
    return merged.to_dict(orient="records")
