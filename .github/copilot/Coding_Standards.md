# Coding Standards

## Python Style Guidelines

### General Principles
- Follow **PEP 8** Python style guidelines
- Use **snake_case** for variables and function names
- Use **PascalCase** for class names
- Use **UPPER_CASE** for constants

### Code Organization

#### Function Structure
- Keep functions focused on a single responsibility
- Use descriptive function names that clearly indicate purpose
- Include docstrings for all functions using triple quotes
- Limit function length to maintain readability

```python
def load_data():
    """Load the cleaned watch history data."""
    df = pd.read_csv(input_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df
```

#### Variable Naming
- Use descriptive variable names
- Avoid abbreviations unless commonly understood
- Use meaningful prefixes for related variables

```python
# Good
input_file = os.path.expanduser('~/Developer/youtube-analysis/output/cleaned_watch_history.csv')
output_dir = os.path.expanduser('~/Developer/youtube-analysis/output/temporal_analysis')

# Avoid
if = '~/path/file.csv'
od = '~/path/dir'
```

#### Import Organization
- Standard library imports first
- Third-party library imports second
- Local application imports last
- Separate each group with a blank line

```python
import os
import json
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from youtube_analysis import YouTubeAnalyzer
```

### Documentation Standards

#### File Headers
Each Python file should include:
- Brief description of the file's purpose
- Input and output path definitions
- Main functionality overview

#### Function Documentation
- Include docstrings for all functions
- Describe parameters and return values
- Use clear, concise language

```python
def analyze_viewing_patterns(df):
    """Analyze viewing patterns across different time dimensions.
    
    Args:
        df: DataFrame containing cleaned watch history data
        
    Returns:
        dict: Dictionary containing analysis results for different time periods
    """
```

### Error Handling

#### Exception Management
- Use specific exception types rather than bare `except` clauses
- Provide meaningful error messages
- Handle file operations with appropriate exception handling

```python
try:
    with open(os.path.join(directory, filename), 'r') as file:
        data = json.load(file)
except (json.JSONDecodeError, KeyError, ValueError) as e:
    print(f"Error processing {filename}: {e}")
```

#### Logging and Output
- Use consistent print statements for user feedback
- Provide progress indicators for long-running operations
- Include file paths in success/failure messages

### Code Quality

#### Modularity
- Encapsulate nested logic into separate functions
- Keep main execution functions simple and readable
- Use helper functions for complex operations

#### Data Handling
- Validate data inputs before processing
- Handle missing or corrupted data gracefully
- Use pandas best practices for data manipulation

#### File Path Management
- Use `os.path.expanduser()` for home directory references
- Use `os.path.join()` for cross-platform path construction
- Define paths at the beginning of modules

### Testing Approach
- Write test cases for core functions
- Test with sample data sets
- Validate output formats and file generation
