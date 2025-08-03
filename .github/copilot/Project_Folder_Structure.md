# Project Folder Structure

## Overview
The project structure is designed to support a modular and scalable analysis pipeline, providing clear separation between data handling, processing, and output generation.

### Hierarchical Layout
```
~/Developer/youtube-analysis/
├── .github/                   # Project documentation files and templates
│   ├── copilot/               # Subdirectory for copilot-specific files
├── config/                    # Configuration files for the analysis scripts
├── data/                      # Input datasets and initial data files
│   └── UserData_YouTube/      # Raw YouTube data
├── output/                    # Results and analysis outputs
│   ├── behavioral_insights/   # Insights about viewing behaviors
│   ├── content_analysis/      # Reports on content preferences and trends
│   ├── personalized_insights/ # Tailored user insights
│   ├── reports/               # Generated markdown reports
│   ├── temporal_analysis/     # Temporal analysis results
│   ├── visualizations/        # PNG visualizations and charts
│   └── exports/               # Multi-format data exports
├── scripts/                   # Core processing and analysis scripts
│   ├── behavioral_analysis.py # Script for behavioral analysis
│   ├── content_analysis.py    # Script for content analysis
│   ├── data_export.py         # Exportation of processed data
│   ├── data_preparation.py    # Initial data cleaning and setup script
│   ├── personalized_insights.py # Personalized insights generation
│   ├── report_generation.py   # Comprehensive report creation
│   └── temporal_analysis.py   # Time-based analysis scripts
└── tests/                     # Testing files to verify functionality
```

### Description of Key Folders
- **.github/**: Contains templates and guidelines for project collaboration and contribution, including sections for copilot analysis.
- **config/**: Houses configuration files to manage and customize script operations.
- **data/**: The input directory for raw data files collected from YouTube exports.
- **output/**: The main directory for analysis results, categorized by insight type.
- **scripts/**: This directory contains all the Python files used to process, analyze, and export data.
- **tests/**: Provided for different testing suites to enhance reliability and accuracy.

### Development Approach
The directory separation follows a clean practice ensuring rigorous separation of functions and responsibilities, aligning with best practices for data analysis projects.
