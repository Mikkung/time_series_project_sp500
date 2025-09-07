from pathlib import Path
from typing import List

def find_csvs(data_dir: str, symbols: List[str] | None = None) -> list[str]:
    p = Path(data_dir)
    if symbols:
        # match any file that begins with SYMBOL and ends with .csv
        files = []
        for sym in symbols:
            files.extend([str(f) for f in p.glob(f"{sym}*.csv")])
        return files
    return [str(f) for f in p.glob("*.csv")]