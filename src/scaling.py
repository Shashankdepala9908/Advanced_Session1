import pandas as pd
from sklearn.preprocessing import StandardScaler

def scale_features(df: pd.DataFrame, cols=None) -> pd.DataFrame:
    df = df.copy()
    if cols is None:
        cols = df.select_dtypes(include="number").columns.tolist()
    if not cols:
        return df
    scaler = StandardScaler()
    df[cols] = scaler.fit_transform(df[cols])
    return df
