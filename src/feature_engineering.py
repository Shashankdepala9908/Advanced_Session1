import pandas as pd

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # Create additional features based on columns typically found in computer price data
    if set(["processor_speed", "ram"]).issubset(df.columns):
        df["speed_per_ram"] = df["processor_speed"] / (df["ram"] + 1e-9)
    if set(["price", "storage"]).issubset(df.columns):
        df["price_per_storage"] = df["price"] / (df["storage"] + 1e-9)
    # One-hot encode categorical columns
    cat_cols = [c for c in df.select_dtypes(exclude="number").columns if df[c].nunique() < 20]
    if cat_cols:
        df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
    return df
