import pandas as pd
import random
from datetime import datetime, timedelta

# SETTINGS
NUM_EMPLOYEES = 50
DAYS = 60

start_date = datetime(2025, 11, 1)

employee_rows = []
meeting_rows = []
meeting_id = 1

for emp_id in range(1, NUM_EMPLOYEES + 1):
    stress_base = random.randint(3, 6)

    for day in range(DAYS):
        date = start_date + timedelta(days=day)

        work_hours = random.randint(7, 12)
        tasks_assigned = random.randint(6, 12)
        tasks_completed = random.randint(4, tasks_assigned)
        stress = min(10, stress_base + random.randint(-1, 3))
        weekend_work = 1 if date.weekday() >= 5 and random.random() < 0.3 else 0

        employee_rows.append([
            emp_id,
            date.strftime("%Y-%m-%d"),
            work_hours,
            tasks_assigned,
            tasks_completed,
            stress,
            weekend_work
        ])

        # Meetings (0–3 per day)
        for _ in range(random.randint(0, 3)):
            meeting_rows.append([
                meeting_id,
                date.strftime("%Y-%m-%d"),
                emp_id,
                random.choice([30, 45, 60, 90]),
                random.randint(3, 12),
                random.choice([True, False]),
                random.randint(0, 4)
            ])
            meeting_id += 1

# SAVE FILES
emp_df = pd.DataFrame(employee_rows, columns=[
    "employee_id", "date", "work_hours",
    "tasks_assigned", "tasks_completed",
    "stress_level", "weekend_work"
])

meet_df = pd.DataFrame(meeting_rows, columns=[
    "meeting_id", "date", "employee_id",
    "duration_min", "participants",
    "has_agenda", "action_items"
])

emp_df.to_csv("employee_logs.csv", index=False)
meet_df.to_csv("meeting_logs.csv", index=False)

print("Large dataset generated successfully!")
print("Employees:", NUM_EMPLOYEES)
print("Days:", DAYS)
print("Employee rows:", len(emp_df))
print("Meeting rows:", len(meet_df))
