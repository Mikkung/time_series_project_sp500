from __future__ import annotations
import argparse
import os
import pandas as pd

from src.utils import find_csvs
from src.data_loader import load_many
from src.analysis import add_moving_averages, correlation_matrices
from src.visualization import plot_prices_by_symbol, plot_moving_averages, plot_corr_heatmap

def build_closing_price_matrix(all_data: pd.DataFrame) -> pd.DataFrame:
    # pivot to wide: one column per Name with 'close' values
    pivot = all_data.pivot_table(index='date', columns='Name', values='close')
    # rename columns to e.g., AAPL_close
    pivot = pivot.rename(columns={c: f"{c}_close" for c in pivot.columns})
    return pivot

def parse_args():
    ap = argparse.ArgumentParser(description="S&P 500 Time Series Analysis")
    ap.add_argument("--data-dir", type=str, default="data", help="Directory containing CSVs")
    ap.add_argument("--symbols", nargs="*", default=None, help="Subset of tickers to include (e.g., AAPL AMZN GOOG MSFT)")
    ap.add_argument("--windows", nargs="*", type=int, default=[10,20,50], help="Moving average windows")
    ap.add_argument("--infer-name-from-filename", action="store_true", help="Infer 'Name' from filename if missing")
    ap.add_argument("--no-show", action="store_true", help="Do not display plots")
    ap.add_argument("--save-images", action="store_true", help="Save plots into images/")
    return ap.parse_args()

def maybe_path(path: str | None) -> str | None:
    if not path:
        return None
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path

def main():
    args = parse_args()
    csvs = find_csvs(args.data_dir, args.symbols)
    if not csvs:
        raise SystemExit(f"No CSV files found in {args.data_dir}. Put files like AAPL_data.csv there.")
    all_data = load_many(csvs, infer_name_from_filename=args.infer_name_from_filename)
    if 'date' in all_data.columns:
        all_data = all_data.sort_values(['Name','date'])
    # 1) Prices by symbol
    prices_img = maybe_path("images/prices_by_symbol.png") if args.save_images else None
    plot_prices_by_symbol(all_data, show=not args.no_show, save_path=prices_img)

    # 2) Moving averages
    ma_df = add_moving_averages(all_data, windows=tuple(args.windows))
    ma_img = maybe_path("images/moving_averages.png") if args.save_images else None
    plot_moving_averages(ma_df, windows=args.windows, show=not args.no_show, save_path=ma_img)

    # 3) Correlations
    closing_matrix = build_closing_price_matrix(all_data)
    close_corr, pct_corr = correlation_matrices(closing_matrix)
    close_img = maybe_path("images/corr_close.png") if args.save_images else None
    pct_img = maybe_path("images/corr_pct.png") if args.save_images else None
    plot_corr_heatmap(close_corr, "Correlation — Close Prices", show=not args.no_show, save_path=close_img)
    plot_corr_heatmap(pct_corr, "Correlation — % Returns", show=not args.no_show, save_path=pct_img)

if __name__ == "__main__":
    main()