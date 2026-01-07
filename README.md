PULSEGUARD - BURNOUT PREDICTOR & MEETING WASTE DETECTOR

PulseGuard is an industry-ready, real-time analytics system designed to help organizations proactively identify employee burnout risk and meeting inefficiencies using data-driven insights.

This project combines machine learning, backend APIs, and an interactive dashboard to simulate how modern IT companies can improve productivity and employee well-being.

 KEY FEATURES

--> Burnout Prediction Engine

Machine Learning–based burnout risk scoring

Uses workload, stress level, task completion, and weekend work

Classifies employees into Low / Medium / High burnout risk

--> Meeting Waste Detector

Analyzes meeting duration, participants, agenda presence, and action items

Calculates Meeting Overload Index

Detects unnecessary or inefficient meetings

--> Correlation Engine

Links meeting overload with burnout risk

Identifies patterns where meetings contribute to employee stress

-->Interactive Dashboard (Streamlit)

Real-time burnout risk visualization

Employee-wise analysis

Easy-to-use web interface

--> Backend API (FastAPI)

REST APIs for burnout prediction

Scalable, modular backend architecture

-->System Architecture

CSV Data (Employee + Meetings)
        ↓
Feature Engineering
        ↓
ML Burnout Model
        ↓
FastAPI Backend
        ↓
Streamlit Dashboard

-->Technologies Used

Python 3.13

Pandas, NumPy

Scikit-learn

FastAPI

Streamlit

Uvicorn

Git & GitHub

--->How to Run the Project

1)Clone the Repository

git clone https://github.com/Naraboinamanojkumar/PulseGuard.git
cd PulseGuard


2)Create Virtual Environment

python -m venv venv
venv\Scripts\activate


3)Install Dependencies

pip install -r requirements.txt

4)Train the Burnout Model

python


from data_loader import load_employee_logs
from feature_engineering import create_burnout_features
from burnout_model import generate_burnout_label, train_burnout_model, save_model

df = load_employee_logs()
df = create_burnout_features(df)
df = generate_burnout_label(df)

model, acc = train_burnout_model(df)
save_model(model)

print("Model accuracy:", acc)
exit()



5)Start Backend (FastAPI)

uvicorn main:app --reload

API docs available at....

http://127.0.0.1:8000/docs



6)Start Dashboard (Streamlit)

streamlit run app.py


Open in browser:

http://localhost:8501


-->Real-World Use Cases

IT companies monitoring employee well-being

HR analytics platforms

Productivity optimization tools

Workforce management systems


-->Why This Project Is Industry-Ready


End-to-end system (Data → ML → API → UI)

Real-time analytics mindset

Scalable backend architecture

Clean GitHub version control

Tested with large datasets


-->Author

Naraboinamanojkumar

GitHub: https://github.com/Naraboinamanojkumar

