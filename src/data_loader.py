from __future__ import annotations
import pandas as pd
from pathlib import Path

def load_stock_csv(path: str, infer_name_from_filename: bool = False) -> pd.DataFrame:
    df = pd.read_csv(path)
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    if 'Name' not in df.columns and infer_name_from_filename:
        # infer ticker from filename prefix (e.g., AAPL_data.csv -> AAPL)
        ticker = Path(path).stem.split('_')[0].upper()
        df['Name'] = ticker
    return df

def load_many(paths: list[str], infer_name_from_filename: bool = False) -> pd.DataFrame:
    frames = []
    for p in paths:
        frames.append(load_stock_csv(p, infer_name_from_filename=infer_name_from_filename))
    if not frames:
        return pd.DataFrame()
    df = pd.concat(frames, ignore_index=True)
    # Ensure datetime and sort
    if 'date' in df.columns:
        df = df.sort_values(['Name','date']) if 'Name' in df.columns else df.sort_values('date')
    return df