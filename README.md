# Time Series Project — S&P 500 (AAPL, AMZN, GOOG, MSFT)

A cleaned-up, **real‑world project structure** derived from a learning notebook for analyzing
S&P 500 stock time series: moving averages, resampling, daily returns, and cross‑ticker
correlations with clear, modular Python code ready for GitHub.

## Features
- Load multiple stock CSVs and merge them into a single DataFrame
- Plot close prices and moving averages (10/20/50 by default)
- Compute daily returns and resample to various frequencies (M/Q/Y)
- Correlation matrix of close prices and percentage returns
- Simple CLI via `main.py`

## Repository Structure
```
time_series_project_sp500/
├── data/                # Put your CSVs here (e.g., AAPL_data.csv, AMZN_data.csv, ...)
├── images/              # Saved plots (optional)
├── notebooks/           # Optional exploration notebooks
├── src/
│   ├── data_loader.py
│   ├── analysis.py
│   ├── visualization.py
│   └── utils.py
├── .gitignore
├── main.py
├── pyproject.toml
└── requirements.txt
```

## Expected CSV Schema
Each CSV is expected to include at least:
- `date` (ISO format like YYYY-MM-DD)
- `open, high, low, close, volume`
- `Name` (ticker symbol like AAPL, AMZN, GOOG, MSFT)

> Tip: If your files do not contain a `Name` column, you can pass `--infer-name-from-filename`
and ensure the filename contains the ticker (e.g., `AAPL_data.csv`).

## Getting Started
1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Put data files** in `data/` (for example: `data/AAPL_data.csv`, `data/AMZN_data.csv`, `data/GOOG_data.csv`, `data/MSFT_data.csv`).

3. **Run the pipeline**
   ```bash
   python main.py --data-dir data --windows 10 20 50 --save-images
   ```

4. **Optional flags**
   - `--symbols AAPL AMZN GOOG MSFT` : explicitly choose which tickers to include
   - `--infer-name-from-filename` : if your CSVs lack a `Name` column
   - `--no-show` : don't open matplotlib windows (useful in CI)
   - `--save-images` : save plots into `images/`

## Notes
- This repo is intended as a **portfolio‑ready** baseline. Extend with Streamlit dashboards,
  add backtests, include more robust data validation, or build a CI workflow.
- Original learning code was a single script; here it's refactored into reusable modules.

## License
MIT