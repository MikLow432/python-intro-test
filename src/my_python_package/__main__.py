from importlib import resources

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_data(path):
    return pd.read_csv(path)

def summary(df):
    print("\nSummary:")
    print(df.describe().round(3))

def correlation(df):
    print("\nCorrelations:")
    cors = df.corr(numeric_only=True)
    print(cors)
    return cors

def scatter(df,cors,thresh= 0.25):

    mask = np.triu(np.ones(cors.shape), k=1).astype(bool)
    unique_corr = cors.where(mask).stack().reset_index()
    unique_corr.columns = ['V1', 'V2', 'Corr']
    pairs = unique_corr[unique_corr['Corr'] >= thresh]

    print("\nCorrelations over Threshold:")
    print(pairs)

    width = len(pairs)
    fig, axes = plt.subplots(nrows=1, ncols=width, figsize=(4 * width, 4))

    if len(pairs) == 1:
        axes = [axes]

    for i in range(len(pairs)):
        col_x = pairs.iloc[i, 0]
        col_y = pairs.iloc[i, 1]
        df.plot.scatter(x=col_x, y=col_y, ax=axes[i], alpha=0.6)
        axes[i].set_title(f"Scatter:\n {col_x} vs\n {col_y}")

    plt.tight_layout()

def histogram(df):
    cols = df.columns.values.tolist()
    width = len(cols)

    fig, axes = plt.subplots(nrows=1, ncols=width, figsize=(4*width, 4))

    if len(cols) == 1:
        axes = [axes]

    for col, ax in zip(cols, axes):
        df[col].hist(ax=ax)
        ax.set_title(f"Histogram of {col}")
    plt.tight_layout()


def main(path,thresh=0.25):
    df = load_data(path)
    summary(df)
    cors = correlation(df)
    histogram(df)
    scatter(df,cors,thresh)
    plt.show()

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default=None)
    args = parser.parse_args()

    if args.file:
        main(args.file)
    else:
        path = resources.files("my_python_package").joinpath("Income.csv")
        main(path)