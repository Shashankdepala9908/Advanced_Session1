# Advanced_Algorithms_Computer_Prices

Pipeline for cleaning, engineering, and scaling data in a **computer prices** dataset.

## Data
- `data/computer_prices_all.csv` — raw dataset
- `data/processed_all_computer_prices.csv` — processed output

## Environment Setup
```bash
python -m venv .venv
# Activate
# Windows: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Run the Pipeline
```bash
python src/main.py --data data/computer_prices_all.csv --save data/processed_all_computer_prices.csv
```
or simply
```bash
python src/main.py
```

## Steps Performed
1. **EDA** — preview, info, and summary stats.
2. **Cleaning** — fill numeric NA, trim outliers.
3. **Feature Engineering** — compute `speed_per_ram`, `price_per_storage`, and encode categoricals.
4. **Scaling** — normalize numeric columns.

---
Modify modules in `src/` as needed for your assignment.
