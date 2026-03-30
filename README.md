# Dataset Analysis Tool

## Description

This project is a command-line data analysis tool written in Python.
It enables quick exploratory analysis of datasets by computing summary statistics, correlations, and generating visualizations.

The tool is designed for flexible and efficient analysis directly from the terminal.

---

## Features

* Summary statistics (mean, std, min, max, quartiles)
* Correlation matrix for numerical variables
* Histograms for all numeric columns
* Scatter plots for highly correlated variable pairs
* Configurable correlation threshold
* Optional column selection
* Optional disabling of plots

---

## Installation

Clone the repository and install the package using `uv`:

```bash
py -m uv pip install -e .
```

---

## Usage

Run the tool with:

```bash
py -m uv run -m my_python_package
```

---

## Command-Line Options

```bash
--file PATH           Path to a CSV dataset
--thresh FLOAT        Correlation threshold (default: 0.25)
--no-plots            Disable all visualizations
--summary-only        Only display summary statistics
--cols COL1 COL2 ...  Select specific columns for analysis
```

---

## Examples

### Default run (uses included dataset)

```bash
py -m uv run -m my_python_package
```

### Use a custom dataset

```bash
py -m uv run -m my_python_package --file data.csv
```

### Only summary statistics

```bash
py -m uv run -m my_python_package --summary-only
```

### Disable plots

```bash
py -m uv run -m my_python_package --no-plots
```

### Set correlation threshold

```bash
py -m uv run -m my_python_package --thresh 0.5
```

### Analyze selected columns only

```bash
py -m uv run -m my_python_package --cols age income education
```

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

* Only numeric columns are used for correlation and plotting.
* Scatter plots are generated only for variable pairs with correlation above the specified threshold.
* The default dataset (`Income.csv`) is included in the package.

---

## Author

Mika Lowack
