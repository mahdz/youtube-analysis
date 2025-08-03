import pandas as pd
import os

# Input and output paths
input_file = os.path.expanduser('~/Developer/youtube-analysis/output/cleaned_watch_history.csv')
output_dir = os.path.expanduser('~/Developer/youtube-analysis/output/personalized_insights')

# Load the cleaned watch history data
def load_data():
    df = pd.read_csv(input_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

# Analyze patterns specific to interests
def analyze_interests(df):
    interests_patterns = {
        'Norwegian Pop': ['norwegian', 'pop'],
        'Drag Content': ['drag', 'rupaul', 'queen', 'lgbt'],
        'Podcasts': ['podcast', 'interview', 'episode'],
    }

    interests_results = {key: 0 for key in interests_patterns.keys()}

    for title in df['title']:
        title_lower = title.lower()
        for interest, keywords in interests_patterns.items():
            if any(keyword in title_lower for keyword in keywords):
                interests_results[interest] += 1

    return interests_results

# Generate personalized insights
def generate_insights(df):
    interests_results = analyze_interests(df)

    with open(os.path.join(output_dir, 'personalized_insights.txt'), 'w') as file:
        file.write("Personalized Insights based on Stated Interests:\n")
        for interest, count in interests_results.items():
            file.write(f"{interest}: {count} videos watched\n")

    print(f"Personalized insights generated. Results saved to {output_dir}")

# Main execution
def main():
    df = load_data()
    os.makedirs(output_dir, exist_ok=True)
    generate_insights(df)

if __name__ == "__main__":
    main()
