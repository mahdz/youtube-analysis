import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

# Input and output paths
base_dir = os.path.expanduser('~/Developer/youtube-analysis/output')
reports_dir = os.path.join(base_dir, 'reports')
visualizations_dir = os.path.join(base_dir, 'visualizations')
obsidian_dir = os.path.expanduser('~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Vault/04-Resources/YouTube-Analysis')

def create_master_report():
    """Create a comprehensive markdown report for Obsidian integration."""
    
    # Ensure directories exist
    os.makedirs(reports_dir, exist_ok=True)
    os.makedirs(obsidian_dir, exist_ok=True)
    
    report_content = f"""---
title: YouTube Viewing Analysis Report
type: analysis
tags: [youtube, data-analysis, media-consumption, personal-insights]
created: {datetime.now().strftime('%Y-%m-%d')}
---

# YouTube Viewing Analysis Report

## Executive Summary

This comprehensive analysis examines YouTube viewing patterns from 2020-2025, providing insights into temporal behavior, content preferences, and viewing habits.

## Key Findings

### Temporal Patterns
- Peak viewing times and seasonal trends identified
- Viewing volume changes over the 6-year period tracked
- Hour-by-day viewing patterns visualized

### Content Preferences
- Top channels and creators ranked by viewing frequency
- Content categories analyzed and tracked over time
- Video title word cloud revealing common themes

### Behavioral Insights
- Average viewing frequency calculated (daily/weekly/monthly)
- Binge-watching sessions detected and analyzed
- Viewing patterns and habits identified

### Personalized Insights
- Alignment with stated interests (Norwegian pop, drag content, podcasts)
- LGBTQ+ content consumption patterns tracked
- Content recommendations based on viewing history

## Visualizations

All visualizations are saved in high-resolution PNG format:
- `temporal_patterns.png` - Viewing patterns across time dimensions
- `viewing_heatmap.png` - Hour-by-day viewing intensity
- `top_channels.png` - Most watched channels/creators
- `content_categories.png` - Content category distribution
- `video_titles_wordcloud.png` - Common words in video titles

## Data Files

Detailed analysis results are available in CSV format:
- Temporal analysis: `temporal_analysis/`
- Content analysis: `content_analysis/`
- Behavioral insights: `behavioral_insights/`
- Personalized insights: `personalized_insights/`

## Analysis Methodology

1. **Data Preparation**: JSON files from 2020-2025 processed and cleaned
2. **Temporal Analysis**: Time-based patterns extracted and visualized
3. **Content Analysis**: Channel identification and categorization
4. **Behavioral Analysis**: Viewing habits and patterns detected
5. **Personalized Analysis**: Interest-based insights generated

## Next Steps

- Regular updates with new viewing data
- Enhanced content categorization using NLP
- Integration with other media consumption data
- Predictive modeling for content recommendations

---

*Generated on {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}*
"""
    
    # Save to both reports directory and Obsidian vault
    with open(os.path.join(reports_dir, 'master_report.md'), 'w') as f:
        f.write(report_content)
    
    with open(os.path.join(obsidian_dir, 'YouTube_Analysis_Report.md'), 'w') as f:
        f.write(report_content)

def create_executive_summary():
    """Create a concise executive summary with top 10 insights."""
    
    summary_content = f"""---
title: YouTube Analysis - Executive Summary
type: summary
tags: [youtube, insights, executive-summary]
created: {datetime.now().strftime('%Y-%m-%d')}
---

# YouTube Analysis - Executive Summary

## Top 10 Insights

1. **Peak Viewing Time**: Identified optimal viewing hours for content consumption
2. **Seasonal Trends**: Discovered viewing pattern variations across months
3. **Top Content Creator**: Determined most-watched channel/creator
4. **Content Category Preference**: Identified primary content category consumption
5. **Viewing Frequency**: Calculated average videos watched per day/week/month
6. **Binge-Watching Behavior**: Detected and quantified viewing sessions
7. **Interest Alignment**: Measured consumption of stated interest content (drag, podcasts, Norwegian pop)
8. **Viewing Evolution**: Tracked changes in viewing habits over 6 years
9. **Content Discovery**: Analyzed balance between familiar and new content
10. **Platform Engagement**: Overall viewing volume and engagement patterns

## Key Metrics Dashboard

- **Total Videos Analyzed**: [To be populated by actual data]
- **Date Range**: 2020-2025
- **Peak Viewing Day**: [To be determined from analysis]
- **Peak Viewing Hour**: [To be determined from analysis]
- **Most Watched Category**: [To be determined from analysis]
- **Average Daily Views**: [To be calculated]

## Recommendations

1. **Content Curation**: Focus on identified peak categories
2. **Viewing Schedule**: Optimize content consumption during peak hours
3. **Interest Expansion**: Explore related content in preferred categories
4. **Viewing Balance**: Maintain healthy viewing habits and patterns

---

*Analysis Period: 2020-2025 | Generated: {datetime.now().strftime('%Y-%m-%d')}*
"""
    
    with open(os.path.join(reports_dir, 'executive_summary.md'), 'w') as f:
        f.write(summary_content)
    
    with open(os.path.join(obsidian_dir, 'YouTube_Executive_Summary.md'), 'w') as f:
        f.write(summary_content)

def create_data_dictionary():
    """Create a comprehensive data dictionary documenting all fields and metrics."""
    
    dictionary_content = f"""---
title: YouTube Analysis - Data Dictionary
type: documentation
tags: [data-dictionary, documentation, youtube-analysis]
created: {datetime.now().strftime('%Y-%m-%d')}
---

# YouTube Analysis - Data Dictionary

## Raw Data Fields

### cleaned_watch_history.csv
- `title`: Video title (string, HTML entities cleaned)
- `timestamp`: Watch timestamp (datetime, ISO format)
- `time`: Original timestamp string from JSON
- `year`: Extracted year from timestamp (integer)
- `month`: Extracted month from timestamp (integer, 1-12)
- `day_of_week`: Day of week (integer, 0=Monday, 6=Sunday)
- `hour`: Hour of day (integer, 0-23)
- `date`: Date component only (date)

## Derived Fields

### Content Analysis
- `extracted_channel`: Channel name extracted from title (string)
- `categories`: Content categories assigned (list)

### Temporal Analysis
- `video_count`: Number of videos per time period (integer)
- `peak_hour`: Hour with highest viewing activity (integer)
- `peak_day`: Day of week with highest viewing activity (integer)

## Analysis Outputs

### Temporal Analysis Files
- `yearly_analysis.csv`: Videos watched per year
- `monthly_analysis.csv`: Videos watched per month
- `day_of_week_analysis.csv`: Videos watched per day of week
- `hourly_analysis.csv`: Videos watched per hour
- `peak_hour_result.txt`: Peak viewing hour
- `peak_day_result.txt`: Peak viewing day

### Content Analysis Files
- `top_channels_overall.csv`: Top 20 channels by view count
- `top_channels_YYYY.csv`: Top 10 channels per year
- `content_categories.csv`: Category distribution
- `category_evolution_by_year.csv`: Category trends over time

### Behavioral Analysis Files
- `behavioral_insights.txt`: Key behavioral metrics

### Personalized Analysis Files
- `personalized_insights.txt`: Interest-based analysis results

## Metrics Definitions

- **Binge Session**: Multiple videos watched within 2-hour window
- **Peak Time**: Time period with highest viewing frequency
- **Content Category**: Keyword-based classification of video content
- **Channel Extraction**: Pattern-based extraction from video titles
- **Viewing Frequency**: Videos per time unit (day/week/month)

## File Locations

- **Project Root**: `~/Developer/youtube-analysis/`
- **Data Input**: `~/Developer/youtube-analysis/data/UserData_YouTube/`
- **Analysis Output**: `~/Developer/youtube-analysis/output/`
- **Obsidian Integration**: `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Vault/04-Resources/YouTube-Analysis/`

---

*Last Updated: {datetime.now().strftime('%Y-%m-%d')}*
"""
    
    with open(os.path.join(reports_dir, 'data_dictionary.md'), 'w') as f:
        f.write(dictionary_content)
    
    with open(os.path.join(obsidian_dir, 'YouTube_Data_Dictionary.md'), 'w') as f:
        f.write(dictionary_content)

def main():
    """Main execution function."""
    print("Generating comprehensive reports...")
    
    # Create all reports
    create_master_report()
    create_executive_summary()
    create_data_dictionary()
    
    print(f"Reports generated successfully!")
    print(f"Reports saved to: {reports_dir}")
    print(f"Obsidian files saved to: {obsidian_dir}")

if __name__ == "__main__":
    main()
