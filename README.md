# King County Housing Data - Exploratory Data Analysis

[![Shipping files](https://github.com/neuefische/ds-eda-project-template/actions/workflows/workflow-03.yml/badge.svg?branch=main&event=workflow_dispatch)](https://github.com/neuefische/ds-eda-project-template/actions/workflows/workflow-03.yml)

This project focuses on exploratory data analysis (EDA) of the King County Housing dataset, providing insights and recommendations for real estate clients. The analysis explores factors influencing house prices in King County, Washington, USA.

## Project Overview

The King County Housing dataset contains information about home sales in King County, including features such as location, size, condition, and various property characteristics. Through comprehensive EDA, this project aims to:

- Identify key factors affecting house prices
- Provide geographical insights about the housing market
- Generate actionable recommendations for buyers and sellers
- Support data-driven decision making in real estate

## Repository Structure

```
ds-eda-project/
├── data/                    # Data files (not tracked in git)
│   └── eda.csv             # King County Housing dataset
├── optional/                # Optional data processing scripts and tests
│   ├── data_processing.py  # Data cleaning and transformation functions
│   ├── test_data_imputation.py
│   └── test_data_transformation.py
├── EDA.ipynb               # Main exploratory data analysis notebook
├── 1_Fetching_the_data_eda.ipynb  # Initial data fetching notebook
├── data_utils.py           # Utility functions for data analysis
├── plotting_utils.py       # Utility functions for visualizations
├── column_names.md         # Column descriptions and metadata
├── assignment.md           # Project requirements and client profiles
├── workflow.md             # EDA methodology and workflow guide
├── requirements.txt        # Python dependencies
├── Makefile               # Automation commands for setup and development
└── README.md              # This file
```

## Key Features

### Data Analysis Utilities

- **`data_utils.py`**: Contains functions for statistical analysis:
  - `detect_outliers_iqr()`: Detects outliers using the Interquartile Range (IQR) method. Returns detailed statistics including quartiles, bounds, outlier counts, and percentages.

- **`plotting_utils.py`**: Provides reusable visualization functions:
  - `plot_price_comparison()`: Creates bar charts comparing average prices across missing, zero, and non-zero values of a specified column. Useful for analyzing the impact of missing or zero-value features on house prices.

### Optional Data Processing Scripts

The `optional/` directory contains additional utilities for data processing:

- **`data_processing.py`**: Data cleaning and transformation functions:
  - `impute_mean()`: Fills missing values with the mean of the series
  - `is_greater_than_average()`: Transforms a series into binary values (0/1) based on whether values are above or below the average

- **`test_data_imputation.py`** and **`test_data_transformation.py`**: Unit tests for the data processing functions

### Main Deliverables

1. **EDA.ipynb**: Well-documented Jupyter notebook containing the complete exploratory data analysis
2. **README.md**: Comprehensive documentation of the repository (this file)
3. **Presentation**: High-level overview slides for non-technical clients (PDF format)

## Requirements

- Python 3.11.3 (managed via pyenv)
- Virtual environment (venv)
- Node.js (for Plotly support in Jupyter Lab)

## Setup

### Prerequisites

Before setting up the project, ensure you have:
- `pyenv` installed
- `Node.js` installed (for Plotly visualizations in Jupyter Lab)
- `make` installed (for using Makefile commands)

### Quick Setup with Makefile

The easiest way to set up the project is using the provided Makefile:

```bash
make setup
```

This command will:
- Check for `pyenv` installation
- Install Python 3.11.3 if not already installed
- Create a virtual environment (`.venv`)
- Upgrade pip
- Install all dependencies from `requirements.txt`
- Register a Jupyter kernel named "Python (ds-eda-project)"

After setup, activate the virtual environment:
```bash
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\Activate.ps1  # Windows PowerShell
```

### Manual Installation Steps

If you prefer to set up manually or the Makefile doesn't work on your system:

#### **macOS**

**Step 1:** Check Node.js version
```sh
node -v
```

If Node.js is not installed, update Homebrew and install Node:
```sh
brew update
brew install node
```

**Step 2:** Set up Python environment and install dependencies
```bash
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --user --name=ds-eda-project --display-name="Python (ds-eda-project)"
```

#### **Windows**

**Step 1:** Install Node.js (if not already installed)
```sh
choco upgrade chocolatey
choco install nodejs
```

**Step 2:** Set up Python environment

For **PowerShell**:
```PowerShell
pyenv local 3.11.3
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --user --name=ds-eda-project --display-name="Python (ds-eda-project)"
```

For **Git-Bash**:
```bash
pyenv local 3.11.3
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --user --name=ds-eda-project --display-name="Python (ds-eda-project)"
```

### Creating Requirements File

To ensure reproducibility, create a requirements file after installing packages:
```bash
make update-requirements
# or manually:
pip freeze > requirements.txt
```

*Note: In rare cases, a requirements file created with `pip freeze` might not ensure that another (especially M1 chip) user can install and execute it properly. This can happen if libraries need to be compiled (e.g. SciPy). Then it also depends on environment variables and the actual system libraries.*

## Usage

### Makefile Commands

The project includes a Makefile with convenient commands for common tasks. Run `make help` to see all available commands:

```bash
make help
```

**Available commands:**

- `make setup` - Complete environment setup (pyenv, venv, dependencies, Jupyter kernel)
- `make install` - Install dependencies from requirements.txt
- `make test` - Run unit tests with pytest
- `make jupyter` or `make notebook` - Start Jupyter Lab
- `make clean` - Remove virtual environment and cache files (__pycache__, .pytest_cache, etc.)
- `make update-requirements` - Update requirements.txt with currently installed packages
- `make register-kernel` - Register the virtual environment as a Jupyter kernel
- `make check-env` - Verify that the virtual environment exists

**Example workflow:**
```bash
make setup          # Initial setup
make jupyter        # Start Jupyter Lab
make test           # Run tests
make clean          # Clean up when done
```

### Running the Analysis

1. Activate your virtual environment:
   ```bash
   source .venv/bin/activate  # macOS/Linux
   # or
   .venv\Scripts\Activate.ps1  # Windows PowerShell
   ```

2. Launch Jupyter Lab:
   ```bash
   make jupyter
   # or manually:
   jupyter lab
   ```

3. Open `EDA.ipynb` to explore the analysis. Make sure to select the "Python (ds-eda-project)" kernel from the kernel dropdown.

### Data

The dataset should be placed in the `data/` folder as `eda.csv`. The `data/` folder is excluded from git tracking to protect sensitive data.

Column descriptions and metadata can be found in `column_names.md`.

### Using Utility Functions

The utility modules can be imported in your notebooks:

```python
from data_utils import detect_outliers_iqr
from plotting_utils import plot_price_comparison

# Detect outliers in a column
outlier_stats = detect_outliers_iqr(df, 'price')

# Create price comparison plot
fig, ax = plt.subplots(figsize=(8, 5))
plot_price_comparison(df, 'sqft_basement', ax, 
                      'Basement Impact on Price', 
                      'No Basement', 'Has Basement')
```

### Unit Testing (Optional)

If you've written Python scripts for data processing, you can run unit tests:
```bash
make test
# or manually:
pytest
```

This command will execute all functions in your project that start with the word **test**.

## Project Methodology

This project follows an iterative EDA workflow:

1. **Understanding the Data**: Load and examine the dataset structure, check for missing values, identify data types
2. **Research Questions & Hypotheses**: Formulate questions and testable hypotheses about factors affecting house prices
3. **Exploring the Data**: Visualize distributions, identify patterns, detect outliers
4. **Cleaning the Data**: Handle missing values, remove outliers, transform features where necessary
5. **Relationships Analysis**: Compute correlations, analyze feature relationships with price
6. **Insights & Recommendations**: Derive actionable insights for clients

For detailed methodology guidance, see `workflow.md`.

## Key Insights

The analysis provides at least:
- **3 insights** regarding the overall data (including one geographical insight)
- **3 recommendations** tailored to specific client needs

## Client Profiles

The project includes analysis tailored to various client profiles (buyers and sellers) with different needs and constraints. See `assignment.md` for the complete list of client profiles.

## Dependencies

All required Python packages and their versions are listed in `requirements.txt`. Key dependencies include:

- **Data Analysis**: pandas, numpy
- **Visualization**: matplotlib, seaborn, altair, folium
- **Jupyter**: jupyterlab, ipywidgets, rise (for presentations)
- **Database**: psycopg2-binary, SQLAlchemy
- **Utilities**: missingno, python-dotenv

Install them using:

```bash
make install
# or manually:
pip install -r requirements.txt
```

## Contributing

This is a project repository. For questions or issues, please refer to the assignment guidelines in `assignment.md`.

## License

See `LICENSE` file for details.
