# Project Architecture

## High-Level Overview

The YouTube Analysis project follows a modular pipeline architecture with distinct phases for data processing, analysis, and reporting.

```
Data Sources → Processing Pipeline → Analysis Modules → Output Generation
     ↓               ↓                    ↓                ↓
[JSON Files] → [Data Preparation] → [Multi-Analysis] → [Reports & Exports]
```

## Data Flow Architecture

### 1. Data Ingestion Layer
- **Input**: YouTube watch history JSON files (2020-2025)
- **Location**: `data/UserData_YouTube/`
- **Processing**: HTML entity cleaning, duplicate removal, timestamp parsing

### 2. Processing Pipeline
- **Data Preparation**: Centralized cleaning and validation
- **Temporal Feature Extraction**: Year, month, day, hour components
- **Content Categorization**: Keyword-based classification
- **Channel Extraction**: Pattern-based channel identification

### 3. Analysis Modules

#### Temporal Analysis
- Viewing patterns across time dimensions
- Peak usage identification
- Seasonal trend analysis
- Hour-by-day heatmap generation

#### Content Analysis
- Channel/creator ranking
- Content category distribution
- Word cloud generation from titles
- Evolution tracking over time

#### Behavioral Analysis
- Binge-watching session detection
- Average viewing frequency calculation
- Viewing habit pattern identification

#### Personalized Insights
- Interest-based content alignment
- Custom category tracking (drag content, podcasts, Norwegian pop)
- Recommendation generation

### 4. Output Generation Layer
- **Visualizations**: High-resolution PNG charts and graphs
- **Reports**: Markdown documents for Obsidian integration
- **Data Exports**: Multiple formats (CSV, JSON, Parquet)
- **Analytics**: Statistical summaries and key metrics

## Component Relationships

```
data_preparation.py
    ↓
├── temporal_analysis.py
├── content_analysis.py
├── behavioral_analysis.py
├── personalized_insights.py
    ↓
├── report_generation.py
├── data_export.py
    ↓
[Output Directory Structure]
```

## Directory Architecture

```
~/Developer/youtube-analysis/
├── data/                    # Input data sources
├── scripts/                 # Analysis modules
├── output/                  # Generated results
│   ├── temporal_analysis/   # Time-based insights
│   ├── content_analysis/    # Content preferences
│   ├── behavioral_insights/ # Usage patterns
│   ├── personalized_insights/ # Custom insights
│   ├── reports/            # Markdown documentation
│   ├── visualizations/     # Chart exports
│   └── exports/            # Multi-format data
├── config/                  # Configuration files
└── tests/                   # Test suites
```

## Processing Workflow

1. **Data Validation**: JSON integrity checks, file completeness
2. **Cleaning & Standardization**: HTML entity resolution, timestamp normalization
3. **Feature Engineering**: Temporal components, content categories
4. **Parallel Analysis**: Independent analysis modules
5. **Result Aggregation**: Consolidated reporting and visualization
6. **Export Generation**: Multiple output formats for different use cases
