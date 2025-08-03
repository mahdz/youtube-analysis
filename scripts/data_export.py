import pandas as pd
import json
import os
from datetime import datetime

# Input and output paths
input_file = os.path.expanduser('~/Developer/youtube-analysis/output/cleaned_watch_history.csv')
output_dir = os.path.expanduser('~/Developer/youtube-analysis/output')
exports_dir = os.path.join(output_dir, 'exports')

def load_data():
    """Load the cleaned watch history data."""
    df = pd.read_csv(input_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def export_to_multiple_formats(df):
    """Export cleaned dataset in multiple formats."""
    
    # Ensure exports directory exists
    os.makedirs(exports_dir, exist_ok=True)
    
    # Export to CSV (already exists, but create a copy in exports)
    df.to_csv(os.path.join(exports_dir, 'youtube_watch_history.csv'), index=False)
    
    # Export to JSON
    df_json = df.copy()
    df_json['timestamp'] = df_json['timestamp'].astype(str)  # Convert datetime for JSON serialization
    df_json.to_json(os.path.join(exports_dir, 'youtube_watch_history.json'), orient='records', date_format='iso')
    
    # Export to Parquet (compressed, efficient format)
    try:
        df.to_parquet(os.path.join(exports_dir, 'youtube_watch_history.parquet'), index=False)
        print("Parquet export successful")
    except ImportError:
        print("Parquet export skipped (pyarrow not installed)")
    
    # Export summary statistics
    summary_stats = {
        'total_videos': len(df),
        'date_range': {
            'start': df['timestamp'].min().isoformat(),
            'end': df['timestamp'].max().isoformat()
        },
        'years_covered': sorted(df['timestamp'].dt.year.unique().tolist()),
        'export_timestamp': datetime.now().isoformat()
    }
    
    with open(os.path.join(exports_dir, 'dataset_summary.json'), 'w') as f:
        json.dump(summary_stats, f, indent=2)

def create_python_module():
    """Create a Python module for future analysis updates."""
    
    module_content = '''"""
YouTube Analysis Module

This module provides utilities for analyzing YouTube watch history data.
Created as part of the comprehensive YouTube viewing analysis project.
"""

import pandas as pd
import os
from datetime import datetime, timedelta

class YouTubeAnalyzer:
    """Main analyzer class for YouTube watch history data."""
    
    def __init__(self, data_file=None):
        """Initialize with data file path."""
        self.data_file = data_file or os.path.expanduser('~/Developer/youtube-analysis/output/cleaned_watch_history.csv')
        self.df = None
    
    def load_data(self):
        """Load the watch history data."""
        self.df = pd.read_csv(self.data_file)
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
        return self.df
    
    def get_viewing_stats(self):
        """Get basic viewing statistics."""
        if self.df is None:
            self.load_data()
        
        stats = {
            'total_videos': len(self.df),
            'date_range': (self.df['timestamp'].min(), self.df['timestamp'].max()),
            'years_covered': sorted(self.df['timestamp'].dt.year.unique()),
            'daily_average': len(self.df) / (self.df['timestamp'].max() - self.df['timestamp'].min()).days
        }
        return stats
    
    def get_recent_activity(self, days=30):
        """Get recent viewing activity."""
        if self.df is None:
            self.load_data()
        
        cutoff_date = self.df['timestamp'].max() - timedelta(days=days)
        recent_df = self.df[self.df['timestamp'] >= cutoff_date]
        return recent_df
    
    def search_titles(self, keyword):
        """Search for videos containing a keyword."""
        if self.df is None:
            self.load_data()
        
        return self.df[self.df['title'].str.contains(keyword, case=False, na=False)]

def quick_stats(data_file=None):
    """Quick function to get basic statistics."""
    analyzer = YouTubeAnalyzer(data_file)
    return analyzer.get_viewing_stats()

def search_videos(keyword, data_file=None):
    """Quick function to search for videos."""
    analyzer = YouTubeAnalyzer(data_file)
    return analyzer.search_titles(keyword)

# Example usage:
# from youtube_analysis import YouTubeAnalyzer, quick_stats
# analyzer = YouTubeAnalyzer()
# stats = analyzer.get_viewing_stats()
# recent = analyzer.get_recent_activity(days=7)
'''
    
    with open(os.path.join(output_dir, 'youtube_analysis.py'), 'w') as f:
        f.write(module_content)

def create_automation_script():
    """Create an automated analysis pipeline script."""
    
    automation_content = '''#!/usr/bin/env python3
"""
Automated YouTube Analysis Pipeline

This script runs the complete analysis pipeline in the correct order.
Use this for regular updates when new data is available.
"""

import os
import subprocess
import sys
from datetime import datetime

def run_script(script_name):
    """Run a Python script and handle errors."""
    script_path = os.path.join(os.path.dirname(__file__), f'{script_name}.py')
    
    print(f"Running {script_name}...")
    try:
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, text=True, check=True)
        print(f"✓ {script_name} completed successfully")
        if result.stdout:
            print(f"Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"✗ {script_name} failed: {e}")
        if e.stderr:
            print(f"Error: {e.stderr}")
        return False
    return True

def main():
    """Run the complete analysis pipeline."""
    print(f"Starting YouTube Analysis Pipeline - {datetime.now()}")
    print("="*50)
    
    # Define the analysis order
    scripts = [
        'data_preparation',
        'temporal_analysis',
        'content_analysis',
        'behavioral_analysis',
        'personalized_insights',
        'report_generation',
        'data_export'
    ]
    
    # Run each script in order
    success_count = 0
    for script in scripts:
        if run_script(script):
            success_count += 1
        print("-" * 30)
    
    print(f"Pipeline completed: {success_count}/{len(scripts)} scripts successful")
    
    if success_count == len(scripts):
        print("🎉 Full analysis pipeline completed successfully!")
    else:
        print("⚠️ Some scripts failed. Check the output above for details.")

if __name__ == "__main__":
    main()
'''
    
    pipeline_script = os.path.join(os.path.dirname(input_file), '..', 'scripts', 'run_analysis_pipeline.py')
    with open(pipeline_script, 'w') as f:
        f.write(automation_content)
    
    # Make the script executable
    os.chmod(pipeline_script, 0o755)

def create_requirements_file():
    """Create a requirements.txt file for dependencies."""
    
    requirements = '''# YouTube Analysis Project Dependencies
pandas>=1.5.0
matplotlib>=3.5.0
seaborn>=0.11.0
wordcloud>=1.8.0
pyarrow>=10.0.0  # Optional: for Parquet export
'''
    
    with open(os.path.join(os.path.dirname(input_file), '..', 'requirements.txt'), 'w') as f:
        f.write(requirements)

def main():
    """Main execution function."""
    print("Starting data export and integration...")
    
    # Load data
    df = load_data()
    
    # Export to multiple formats
    export_to_multiple_formats(df)
    
    # Create Python module for future use
    create_python_module()
    
    # Create automation pipeline
    create_automation_script()
    
    # Create requirements file
    create_requirements_file()
    
    print(f"Data export completed successfully!")
    print(f"Exports saved to: {exports_dir}")
    print(f"Python module created: {os.path.join(output_dir, 'youtube_analysis.py')}")
    print(f"Automation pipeline: ~/Developer/youtube-analysis/scripts/run_analysis_pipeline.py")
    print(f"Requirements file: ~/Developer/youtube-analysis/requirements.txt")

if __name__ == "__main__":
    main()
