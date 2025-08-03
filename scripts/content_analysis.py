import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re
from collections import Counter
import os

# Input and output paths
input_file = os.path.expanduser('~/Developer/youtube-analysis/output/cleaned_watch_history.csv')
output_dir = os.path.expanduser('~/Developer/youtube-analysis/output/content_analysis')

def load_data():
    """Load the cleaned watch history data."""
    df = pd.read_csv(input_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['year'] = df['timestamp'].dt.year
    return df

def extract_channel_names(df):
    """Extract channel names from video titles using common patterns."""
    channels = []
    
    for title in df['title']:
        # Common patterns for channel extraction
        # Pattern 1: "Channel Name - Video Title"
        if ' - ' in title:
            potential_channel = title.split(' - ')[0]
            channels.append(potential_channel)
        # Pattern 2: "Video Title | Channel Name"
        elif ' | ' in title:
            potential_channel = title.split(' | ')[-1]
            channels.append(potential_channel)
        # Pattern 3: "Channel Name: Video Title"
        elif ': ' in title and len(title.split(': ')[0]) < 50:
            potential_channel = title.split(': ')[0]
            channels.append(potential_channel)
        else:
            # Extract first few words as potential channel
            words = title.split()[:3]
            channels.append(' '.join(words))
    
    df['extracted_channel'] = channels
    return df

def categorize_content(df):
    """Categorize content based on video titles using keyword matching."""
    categories = {
        'Drag/LGBTQ+': ['drag', 'rupaul', 'queen', 'lgbt', 'gay', 'pride', 'queer'],
        'Music': ['music', 'song', 'album', 'artist', 'concert', 'live', 'performance'],
        'Podcast': ['podcast', 'interview', 'talk', 'discussion', 'episode'],
        'Comedy': ['comedy', 'funny', 'humor', 'laugh', 'joke', 'comedian'],
        'Tutorial/Educational': ['how to', 'tutorial', 'learn', 'guide', 'tips', 'education'],
        'News/Politics': ['news', 'politics', 'election', 'government', 'policy'],
        'Gaming': ['game', 'gaming', 'play', 'gameplay', 'streamer'],
        'Travel': ['travel', 'trip', 'vacation', 'destination', 'tourism'],
        'Food': ['recipe', 'cooking', 'food', 'chef', 'kitchen', 'meal'],
        'Technology': ['tech', 'technology', 'gadget', 'app', 'software', 'review']
    }
    
    def categorize_title(title):
        title_lower = title.lower()
        matched_categories = []
        
        for category, keywords in categories.items():
            if any(keyword in title_lower for keyword in keywords):
                matched_categories.append(category)
        
        return matched_categories if matched_categories else ['Other']
    
    df['categories'] = df['title'].apply(categorize_title)
    return df

def analyze_top_channels(df):
    """Analyze top channels/creators by view count."""
    channel_counts = df['extracted_channel'].value_counts()
    
    # Overall top channels
    top_channels_overall = channel_counts.head(20)
    
    # Top channels by year
    top_channels_by_year = {}
    for year in df['year'].unique():
        year_data = df[df['year'] == year]
        top_channels_by_year[year] = year_data['extracted_channel'].value_counts().head(10)
    
    return top_channels_overall, top_channels_by_year

def analyze_content_categories(df):
    """Analyze content category preferences."""
    # Flatten categories list
    all_categories = []
    for cat_list in df['categories']:
        all_categories.extend(cat_list)
    
    category_counts = Counter(all_categories)
    
    # Category evolution over time
    category_by_year = {}
    for year in df['year'].unique():
        year_data = df[df['year'] == year]
        year_categories = []
        for cat_list in year_data['categories']:
            year_categories.extend(cat_list)
        category_by_year[year] = Counter(year_categories)
    
    return category_counts, category_by_year

def create_word_cloud(df):
    """Create word cloud from video titles."""
    # Combine all titles
    all_titles = ' '.join(df['title'].tolist())
    
    # Remove common stop words and clean text
    stop_words = {'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'shall', 'can', 'a', 'an', 'this', 'that', 'these', 'those'}
    
    wordcloud = WordCloud(
        width=1200, 
        height=600, 
        background_color='white',
        stopwords=stop_words,
        max_words=100,
        relative_scaling=0.5,
        colormap='viridis'
    ).generate(all_titles)
    
    return wordcloud

def create_visualizations(df, top_channels_overall, category_counts, wordcloud):
    """Create visualizations for content analysis."""
    
    # Set up the plotting style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Top 15 channels bar chart
    plt.figure(figsize=(12, 8))
    top_15_channels = top_channels_overall.head(15)
    plt.barh(range(len(top_15_channels)), top_15_channels.values)
    plt.yticks(range(len(top_15_channels)), top_15_channels.index)
    plt.xlabel('Number of Videos Watched')
    plt.title('Top 15 Most Watched Channels/Creators')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'top_channels.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    # Content categories pie chart
    plt.figure(figsize=(10, 8))
    category_data = dict(category_counts.most_common(10))
    plt.pie(category_data.values(), labels=category_data.keys(), autopct='%1.1f%%', startangle=90)
    plt.title('Content Category Distribution')
    plt.axis('equal')
    plt.savefig(os.path.join(output_dir, 'content_categories.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    # Word cloud
    plt.figure(figsize=(15, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Most Common Words in Video Titles', fontsize=16, pad=20)
    plt.savefig(os.path.join(output_dir, 'video_titles_wordcloud.png'), dpi=300, bbox_inches='tight')
    plt.close()

def save_results(top_channels_overall, top_channels_by_year, category_counts, category_by_year):
    """Save content analysis results to files."""
    
    # Save top channels overall
    top_channels_overall.to_csv(os.path.join(output_dir, 'top_channels_overall.csv'))
    
    # Save top channels by year
    for year, data in top_channels_by_year.items():
        data.to_csv(os.path.join(output_dir, f'top_channels_{year}.csv'))
    
    # Save category analysis
    category_df = pd.DataFrame(list(category_counts.items()), columns=['Category', 'Count'])
    category_df.to_csv(os.path.join(output_dir, 'content_categories.csv'), index=False)
    
    # Save category evolution by year
    category_evolution = []
    for year, categories in category_by_year.items():
        for category, count in categories.items():
            category_evolution.append({'Year': year, 'Category': category, 'Count': count})
    
    category_evolution_df = pd.DataFrame(category_evolution)
    category_evolution_df.to_csv(os.path.join(output_dir, 'category_evolution_by_year.csv'), index=False)

def main():
    """Main execution function."""
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Load and process data
    df = load_data()
    df = extract_channel_names(df)
    df = categorize_content(df)
    
    # Analyze content
    top_channels_overall, top_channels_by_year = analyze_top_channels(df)
    category_counts, category_by_year = analyze_content_categories(df)
    
    # Create word cloud
    wordcloud = create_word_cloud(df)
    
    # Create visualizations
    create_visualizations(df, top_channels_overall, category_counts, wordcloud)
    
    # Save results
    save_results(top_channels_overall, top_channels_by_year, category_counts, category_by_year)
    
    print(f"Content analysis completed. Results saved to {output_dir}")
    print(f"Top channel: {top_channels_overall.index[0]} ({top_channels_overall.iloc[0]} videos)")
    print(f"Most common content category: {category_counts.most_common(1)[0][0]} ({category_counts.most_common(1)[0][1]} videos)")

if __name__ == "__main__":
    main()
