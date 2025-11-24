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
└── README.md              # This file
```

## Key Features

### Data Analysis Utilities

- **`data_utils.py`**: Contains functions for statistical analysis, including outlier detection using the IQR method
- **`plotting_utils.py`**: Provides reusable visualization functions for comparing price distributions across different property features

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

### Installation Steps

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
```

For **Git-Bash**:
```bash
pyenv local 3.11.3
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Creating Requirements File

To ensure reproducibility, create a requirements file after installing packages:
```bash
pip freeze > requirements.txt
```

*Note: In rare cases, a requirements file created with `pip freeze` might not ensure that another (especially M1 chip) user can install and execute it properly. This can happen if libraries need to be compiled (e.g. SciPy). Then it also depends on environment variables and the actual system libraries.*

## Usage

### Running the Analysis

1. Activate your virtual environment:
   ```bash
   source .venv/bin/activate  # macOS/Linux
   # or
   .venv\Scripts\Activate.ps1  # Windows PowerShell
   ```

2. Launch Jupyter Lab:
   ```bash
   jupyter lab
   ```

3. Open `EDA.ipynb` to explore the analysis

### Data

The dataset should be placed in the `data/` folder as `eda.csv`. The `data/` folder is excluded from git tracking to protect sensitive data.

Column descriptions and metadata can be found in `column_names.md`.

### Unit Testing (Optional)

If you've written Python scripts for data processing, you can run unit tests:
```bash
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

All required Python packages and their versions are listed in `requirements.txt`. Install them using:

```bash
pip install -r requirements.txt
```

## Contributing

This is a project repository. For questions or issues, please refer to the assignment guidelines in `assignment.md`.

## License

See `LICENSE` file for details.
