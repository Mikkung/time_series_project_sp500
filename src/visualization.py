from __future__ import annotations
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import Iterable

def plot_prices_by_symbol(all_data: pd.DataFrame, show=True, save_path: str | None = None):
    symbols = list(all_data['Name'].unique())
    n = len(symbols)
    cols = 2
    rows = (n + cols - 1) // cols
    plt.figure(figsize=(10*cols, 5*rows))
    for idx, sym in enumerate(symbols, 1):
        plt.subplot(rows, cols, idx)
        df = all_data[all_data['Name'] == sym]
        plt.plot(df['date'], df['close'])
        plt.title(sym)
        plt.xlabel("Date")
        plt.ylabel("Close")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    if show:
        plt.show()

def plot_moving_averages(ma_df: pd.DataFrame, windows: Iterable[int], show=True, save_path: str | None = None):
    symbols = list(ma_df['Name'].unique())
    n = len(symbols)
    cols = 2
    rows = (n + cols - 1) // cols
    plt.figure(figsize=(10*cols, 5*rows))
    for idx, sym in enumerate(symbols, 1):
        plt.subplot(rows, cols, idx)
        df = ma_df[ma_df['Name'] == sym]
        for w in windows:
            plt.plot(df['date'], df[f'close_{w}'], label=f'MA{w}')
        plt.title(f"{sym} — Moving Averages")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    if show:
        plt.show()

def plot_corr_heatmap(corr: pd.DataFrame, title: str, show=True, save_path: str | None = None):
    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title(title)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    if show:
        plt.show()