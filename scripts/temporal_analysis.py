import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# Input and output paths
input_file = os.path.expanduser('~/Developer/youtube-analysis/output/cleaned_watch_history.csv')
output_dir = os.path.expanduser('~/Developer/youtube-analysis/output/temporal_analysis')

def load_data():
    """Load the cleaned watch history data."""
    df = pd.read_csv(input_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Extract temporal features
    df['year'] = df['timestamp'].dt.year
    df['month'] = df['timestamp'].dt.month
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    df['hour'] = df['timestamp'].dt.hour
    df['date'] = df['timestamp'].dt.date
    
    return df

def analyze_viewing_patterns(df):
    """Analyze viewing patterns across different time dimensions."""
    results = {}
    
    # Viewing frequency by year
    results['yearly'] = df.groupby('year').size().reset_index(name='video_count')
    
    # Viewing frequency by month
    results['monthly'] = df.groupby('month').size().reset_index(name='video_count')
    
    # Viewing frequency by day of week
    results['day_of_week'] = df.groupby('day_of_week').size().reset_index(name='video_count')
    
    # Viewing frequency by hour
    results['hourly'] = df.groupby('hour').size().reset_index(name='video_count')
    
    # Peak viewing times
    results['peak_hour'] = results['hourly'].loc[results['hourly']['video_count'].idxmax()]
    results['peak_day'] = results['day_of_week'].loc[results['day_of_week']['video_count'].idxmax()]
    
    return results

def create_visualizations(df, results):
    """Create visualizations for temporal patterns."""
    
    # Set up the plotting style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Create subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('YouTube Viewing Temporal Patterns', fontsize=16)
    
    # Yearly viewing pattern
    axes[0, 0].bar(results['yearly']['year'], results['yearly']['video_count'])
    axes[0, 0].set_title('Videos Watched Per Year')
    axes[0, 0].set_xlabel('Year')
    axes[0, 0].set_ylabel('Video Count')
    
    # Monthly viewing pattern
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    axes[0, 1].bar(results['monthly']['month'], results['monthly']['video_count'])
    axes[0, 1].set_title('Videos Watched Per Month')
    axes[0, 1].set_xlabel('Month')
    axes[0, 1].set_ylabel('Video Count')
    axes[0, 1].set_xticks(range(1, 13))
    axes[0, 1].set_xticklabels(month_names)
    
    # Day of week viewing pattern
    day_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    axes[1, 0].bar(results['day_of_week']['day_of_week'], results['day_of_week']['video_count'])
    axes[1, 0].set_title('Videos Watched Per Day of Week')
    axes[1, 0].set_xlabel('Day of Week')
    axes[1, 0].set_ylabel('Video Count')
    axes[1, 0].set_xticks(range(7))
    axes[1, 0].set_xticklabels(day_names)
    
    # Hourly viewing pattern
    axes[1, 1].bar(results['hourly']['hour'], results['hourly']['video_count'])
    axes[1, 1].set_title('Videos Watched Per Hour')
    axes[1, 1].set_xlabel('Hour of Day')
    axes[1, 1].set_ylabel('Video Count')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'temporal_patterns.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    # Create heatmap for hour-by-day viewing patterns
    pivot_table = df.groupby(['day_of_week', 'hour']).size().unstack(fill_value=0)
    
    plt.figure(figsize=(12, 6))
    sns.heatmap(pivot_table, annot=False, cmap='YlOrRd', cbar_kws={'label': 'Video Count'})
    plt.title('Viewing Heatmap: Hour by Day of Week')
    plt.xlabel('Hour of Day')
    plt.ylabel('Day of Week')
    plt.yticks(range(7), ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], rotation=0)
    plt.savefig(os.path.join(output_dir, 'viewing_heatmap.png'), dpi=300, bbox_inches='tight')
    plt.close()

def save_results(results):
    """Save temporal analysis results to CSV files."""
    for key, data in results.items():
        if isinstance(data, pd.DataFrame):
            data.to_csv(os.path.join(output_dir, f'{key}_analysis.csv'), index=False)
        else:
            # Handle non-DataFrame results (like peak times)
            with open(os.path.join(output_dir, f'{key}_result.txt'), 'w') as f:
                f.write(str(data))

def main():
    """Main execution function."""
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Load and analyze data
    df = load_data()
    results = analyze_viewing_patterns(df)
    
    # Create visualizations
    create_visualizations(df, results)
    
    # Save results
    save_results(results)
    
    print(f"Temporal analysis completed. Results saved to {output_dir}")
    print(f"Peak viewing hour: {results['peak_hour']['hour']}:00")
    print(f"Peak viewing day: {['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][results['peak_day']['day_of_week']]}")

if __name__ == "__main__":
    main()
