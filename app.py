import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="PulseGuard Dashboard", layout="wide")
st.title("PulseGuard – Burnout & Meeting Dashboard")

API_URL = "http://127.0.0.1:8000/burnout-risk"
response = requests.get(API_URL)
data = pd.DataFrame(response.json())

st.subheader("Team Burnout Overview")
st.dataframe(data[["employee_id","date","burnout_risk_percent","burnout_risk_level","meeting_overload_index"]])

emp_id = st.selectbox("Select Employee", data["employee_id"].unique())
emp_data = data[data["employee_id"]==emp_id].iloc[-1]

st.subheader(f"Employee {emp_id} Burnout Risk")
st.metric("Risk %", emp_data["burnout_risk_percent"], emp_data["burnout_risk_level"])
