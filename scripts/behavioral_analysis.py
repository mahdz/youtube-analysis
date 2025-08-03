import pandas as pd
import os
from datetime import timedelta

# Input and output paths
input_file = os.path.expanduser('~/Developer/youtube-analysis/output/cleaned_watch_history.csv')
output_dir = os.path.expanduser('~/Developer/youtube-analysis/output/behavioral_insights')

# Load the cleaned watch history data
def load_data():
    df = pd.read_csv(input_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

# Detect binge-watching sessions
def detect_binge_watching(df):
    sessions = []
    df = df.sort_values(by='timestamp')
    current_session = [df.iloc[0]]

    for i in range(1, len(df)):
        if df.iloc[i]['timestamp'] - current_session[-1]['timestamp'] <= timedelta(hours=2):
            current_session.append(df.iloc[i])
        else:
            sessions.append(current_session)
            current_session = [df.iloc[i]]

    if current_session:
        sessions.append(current_session)

    return sessions

# Calculate average videos watched per day/week/month
def calculate_averages(df):
    daily_avg = df.groupby(df['timestamp'].dt.date)['title'].count().mean()
    weekly_avg = df.groupby(df['timestamp'].dt.to_period('W'))['title'].count().mean()
    monthly_avg = df.groupby(df['timestamp'].dt.to_period('M'))['title'].count().mean()
    return daily_avg, weekly_avg, monthly_avg

# Main function to perform analysis
def main():
    df = load_data()

    # Calculate averages
    daily_avg, weekly_avg, monthly_avg = calculate_averages(df)

    # Detect binge-watching sessions
    binge_sessions = detect_binge_watching(df)

    results = {
        "daily_avg": daily_avg,
        "weekly_avg": weekly_avg,
        "monthly_avg": monthly_avg,
        "binge_sessions_count": len(binge_sessions),
    }

    # Save results to output directory
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, 'behavioral_insights.txt'), 'w') as file:
        for key, value in results.items():
            file.write(f"{key}: {value}\n")

    print(f"Behavioral analysis completed. Results saved to {output_dir}")

if __name__ == "__main__":
    main()
