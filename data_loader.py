import pandas as pd

def load_employee_logs():
    return pd.read_csv("employee_logs.csv")

def load_meeting_logs():
    return pd.read_csv("meeting_logs.csv")
