#!/usr/bin/env python3
"""
YouTube Analysis Pipeline
Main script to execute the complete YouTube data analysis workflow.
"""

import os
import sys
import subprocess
from datetime import datetime

def run_script(script_name, description):
    """Run a Python script and handle errors."""
    script_path = os.path.join('scripts', script_name)
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, text=True, check=True)
        print(result.stdout)
        if result.stderr:
            print(f"Warning: {result.stderr}")
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}:")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error in {description}: {e}")
        return False

def main():
    """Execute the complete analysis pipeline."""
    start_time = datetime.now()
    
    print("🎬 YouTube Analysis Pipeline Starting")
    print(f"Started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Pipeline steps in order
    pipeline_steps = [
        ('data_preparation.py', 'Data Preparation & Cleaning'),
        ('temporal_analysis.py', 'Temporal Analysis'),
        ('content_analysis.py', 'Content Analysis'),
        ('behavioral_analysis.py', 'Behavioral Analysis'),
        ('personalized_insights.py', 'Personalized Insights'),
        ('report_generation.py', 'Report Generation'),
        ('data_export.py', 'Data Export')
    ]
    
    results = []
    
    for script_name, description in pipeline_steps:
        success = run_script(script_name, description)
        results.append((description, success))
        
        if not success:
            print(f"\n⚠️  Pipeline stopped due to error in {description}")
            print("You can continue from the next step manually if needed.")
            break
    
    # Summary
    end_time = datetime.now()
    duration = end_time - start_time
    
    print(f"\n{'='*60}")
    print("📊 PIPELINE SUMMARY")
    print(f"{'='*60}")
    print(f"Total duration: {duration}")
    print(f"Completed at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    successful = sum(1 for _, success in results if success)
    total = len(results)
    
    for description, success in results:
        status = "✅" if success else "❌"
        print(f"{status} {description}")
    
    print(f"\nSuccessful: {successful}/{total}")
    
    if successful == total:
        print("\n🎉 All analyses completed successfully!")
        print("Check the 'output/' directory for your results.")
    else:
        print(f"\n⚠️  {total - successful} step(s) failed. Check error messages above.")

if __name__ == "__main__":
    main()
