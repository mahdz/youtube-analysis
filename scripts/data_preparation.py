import os
import json
import pandas as pd
from datetime import datetime

# Directory and output setup
input_dir = os.path.expanduser('~/Developer/youtube-analysis/data/UserData_YouTube')
output_file = os.path.expanduser('~/Developer/youtube-analysis/output/cleaned_watch_history.csv')

# Function to clean video titles
def clean_title(title):
    return (title.replace('\u0026#39;', "'")
                .replace('\u0026amp;', '&'))

# Load and process JSON files
def load_and_process_files(directory):
    all_data = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            try:
                with open(os.path.join(directory, filename), 'r') as file:
                    data = json.load(file)
                    # Data cleaning and parsing
                    for entry in data:
                        if 'title' in entry and 'date_watched' in entry:
                            entry['title'] = clean_title(entry['title'])
                            # Parse date_watched field instead of time
                            entry['timestamp'] = datetime.strptime(entry['date_watched'], '%Y-%m-%d %H:%M:%S')
                            all_data.append(entry)
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                print(f"Error processing {filename}: {e}")
    df = pd.DataFrame(all_data)
    df.drop_duplicates(subset=['title', 'timestamp'], inplace=True)
    return df

# Main script execution
def main():
    df = load_and_process_files(input_dir)
    # Save to CSV
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    main()
