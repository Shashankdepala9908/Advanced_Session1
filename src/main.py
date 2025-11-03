import os
import argparse
import pandas as pd
from eda import run_eda
from cleaning import clean_data
from feature_engineering import engineer_features
from scaling import scale_features

DEFAULT_RAW = "data/computer_prices_all.csv"
DEFAULT_OUTPUT = "data/processed_all_computer_prices.csv"

def ensure_data_exists(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Data file not found: {path}. Place your CSV in 'data/' or pass --data PATH.")

def main():
    parser = argparse.ArgumentParser(description="Pipeline for computer prices dataset.")
    parser.add_argument("--data", default=DEFAULT_RAW, help="Path to input CSV (raw). Default: data/computer_prices_all.csv")
    parser.add_argument("--save", default=DEFAULT_OUTPUT, help="Path to save processed CSV.")
    args = parser.parse_args()

    ensure_data_exists(args.data)
    df = pd.read_csv(args.data)
    df = run_eda(df)
    df = clean_data(df)
    df = engineer_features(df)
    df = scale_features(df)
    os.makedirs(os.path.dirname(args.save), exist_ok=True)
    df.to_csv(args.save, index=False)
    print(f"\n✅ Pipeline finished. Rows: {len(df)} | Saved: {args.save}")

if __name__ == "__main__":
    main()
