import pandas as pd

def run_eda(df: pd.DataFrame) -> pd.DataFrame:
    print("\n=== EDA: head ===")
    print(df.head())
    print("\n=== EDA: info ===")
    print(df.info())
    print("\n=== EDA: describe (numeric) ===")
    print(df.describe())
    return df
