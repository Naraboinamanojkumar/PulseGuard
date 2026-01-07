def calculate_meeting_waste_score(row):
    score = 100
    if row["duration_min"] > 60:
        score -= 25
    elif row["duration_min"] > 45:
        score -= 15
    if row["participants"] > 8:
        score -= 25
    elif row["participants"] > 5:
        score -= 15
    if not row["has_agenda"]:
        score -= 20
    if row["action_items"] == 0:
        score -= 15
    return max(score, 0)

def add_meeting_scores(df):
    df["meeting_score"] = df.apply(calculate_meeting_waste_score, axis=1)
    df["waste_category"] = df["meeting_score"].apply(
        lambda x: "Efficient" if x >= 70 else "Neutral" if x >= 40 else "Wasteful"
    )
    return df
