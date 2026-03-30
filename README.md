# Dataset Analysis Tool

## Description

This project is a command-line data analysis tool written in Python.
It allows users to quickly load a dataset, compute summary statistics, analyze correlations, and generate visualizations.

The tool is designed for simple and fast exploratory data analysis.

---

## Features

* Summary statistics (mean, std, min, max, quartiles)
* Correlation matrix for numerical variables
* Histograms for all columns
* Scatter plots for highly correlated variable pairs

---

## Installation

Clone the repository and install the package using `uv`:

```bash
py -m uv pip install -e .
```

---

## Usage

Run the tool using:

```bash
py -m uv run -m my_python_package
```

This will:

1. Load the included dataset (`Income.csv`)
2. Print summary statistics
3. Show correlations
4. Generate histograms
5. Generate scatter plots for correlated variables

---

## Project Structure

```
project-root/
│
├── pyproject.toml
├── README.md
│
└── src/
    └── my_python_package/
        ├── __init__.py
        ├── __main__.py
        └── Income.csv
```

---

## Requirements

* Python >= 3.11
* pandas
* matplotlib

---

## Notes

* The dataset is included in the package.
* The tool focuses on numerical columns for correlation analysis.
* Scatter plots are only created for variable pairs with correlation above a threshold (default: 0.25).

---

## Author

Mika Lowack


install with: py -m uv pip install -e .

run with: py -m uv run -m my_python_package
