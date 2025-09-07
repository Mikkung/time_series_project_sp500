from __future__ import annotations
import pandas as pd

def add_moving_averages(df: pd.DataFrame, windows=(10,20,50)) -> pd.DataFrame:
    out = df.copy()
    for w in windows:
        out[f'close_{w}'] = out['close'].rolling(window=w, min_periods=w).mean()
    return out

def daily_returns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out['daily_return_pct'] = out['close'].pct_change() * 100.0
    return out

def resample_close(df: pd.DataFrame, rule: str = 'M') -> pd.Series:
    if 'date' in df.columns and not isinstance(df.index, pd.DatetimeIndex):
        df = df.set_index('date')
    return df['close'].resample(rule).mean()

def correlation_matrices(closing_price_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    # Expect columns like AAPL_close, AMZN_close, ...
    # 1) Close price correlation
    close_corr = closing_price_df.corr()
    # 2) Percentage change correlation (drop first NaN after pct_change)
    pct_df = closing_price_df.pct_change().dropna()
    pct_corr = pct_df.corr()
    return close_corr, pct_corr