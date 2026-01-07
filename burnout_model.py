import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

def generate_burnout_label(df):
    conditions = (
        (df["avg_work_hours_7d"] > 9.5).astype(int) +
        (df["stress_level"] >= 7).astype(int) +
        (df["task_completion_rate"] < 0.7).astype(int) +
        (df["weekend_work_flag"] == 1).astype(int)
    )
    df["burnout_label"] = (conditions >= 2).astype(int)
    return df

def train_burnout_model(df):
    features = ["avg_work_hours_7d", "task_completion_rate", "stress_trend", "weekend_work_flag"]
    X = df[features]
    y = df["burnout_label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipeline = Pipeline([("scaler", StandardScaler()), ("model", LogisticRegression())])
    pipeline.fit(X_train, y_train)
    accuracy = pipeline.score(X_test, y_test)
    return pipeline, accuracy

def predict_burnout_risk(model, df):
    features = ["avg_work_hours_7d", "task_completion_rate", "stress_trend", "weekend_work_flag"]
    probabilities = model.predict_proba(df[features])[:, 1]
    df["burnout_risk_percent"] = (probabilities * 100).round(1)
    df["burnout_risk_level"] = df["burnout_risk_percent"].apply(
        lambda x: "Low" if x < 40 else "Medium" if x < 70 else "High"
    )
    return df

def save_model(model, path="burnout_model.pkl"):
    joblib.dump(model, path)

def load_model(path="burnout_model.pkl"):
    return joblib.load(path)
