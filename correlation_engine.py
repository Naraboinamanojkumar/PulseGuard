def merge_burnout_meetings(burnout_df, meeting_df):
    meeting_daily = meeting_df.groupby("date").agg({"duration_min":"sum","meeting_score":"mean"}).reset_index()
    meeting_daily.rename(columns={"duration_min":"total_meeting_minutes","meeting_score":"avg_meeting_score"}, inplace=True)
    merged = burnout_df.merge(meeting_daily, on="date", how="left")
    merged.fillna({"total_meeting_minutes":0,"avg_meeting_score":100}, inplace=True)
    return merged

def calculate_meeting_overload(df):
    df["meeting_overload_index"] = df["total_meeting_minutes"] * (100 - df["avg_meeting_score"])/100
    return df
