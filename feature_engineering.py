def create_burnout_features(df):
    df = df.sort_values(["employee_id", "date"])
    df["avg_work_hours_7d"] = (
        df.groupby("employee_id")["work_hours"]
        .rolling(7, min_periods=1)
        .mean()
        .reset_index(level=0, drop=True)
    )
    df["task_completion_rate"] = (
        df["tasks_completed"] / df["tasks_assigned"]
    ).fillna(0)
    df["stress_trend"] = df.groupby("employee_id")["stress_level"].diff().fillna(0)
    df["weekend_work_flag"] = df["weekend_work"].astype(int)
    return df
