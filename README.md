# Data Analysis Project Workspace

## Structure

```
/project-root
│
├── docs/                  # Guidelines, rubrics, planning, and reference Markdown files
├── reports/               # Deliverable reports and analysis results in Markdown
│   └── figures/           # Generated plots and figures
├── data/                  # Data-specific Markdown files and datasets
├── notebooks/             # Jupyter notebooks for each analysis stage
├── src/                   # Python scripts and reusable code
├── requirements.txt       # Python dependencies
├── README.md              # Project overview and instructions
├── .gitignore             # Files/folders to ignore in version control
└── LICENSE                # License information (if needed)
```

## Navigation Guide
- **docs/**: Guidelines, rubrics, planning, and reference Markdown files.
- **reports/**: Main deliverable reports and analysis results.
- **reports/figures/**: All generated plots and figures.
- **data/**: Data-specific Markdown files (e.g., data dictionaries) and datasets.
- **notebooks/**: Step-by-step Jupyter notebooks for each analysis stage.
- **src/**: Python scripts for data processing, feature engineering, and utilities.

## Usage
1. Start with the data dictionary in `notebooks/` and document variables in `data/`.
2. Perform univariate and bivariate analyses in dedicated notebooks, saving figures to `reports/figures/`.
3. Develop and evaluate features in `notebooks/` and `src/`.
4. Document findings and visualizations in `reports/EDA_report.md`.
5. Use version control for all code and data transformations.
6. Ensure reproducibility by maintaining `requirements.txt` and clear instructions. 