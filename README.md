## Turkish Investment Fund Returns Analysis (Python Project)

This project analyzes the historical performance of Turkish investment funds using summary return data. The code loads a CSV file containing returns over multiple timeframes, cleans the data, performs basic statistical analysis, and generates key visualizations.

## What it does

- Loads a CSV containing fund returns (1 month, 3 months, 6 months, YTD, 1 year, 3 years, 5 years)
- Cleans and converts percentage strings (e.g., `"1.234,56"` ➝ `1234.56`)
- Calculates:
  - Mean return for each fund
  - Volatility (standard deviation of returns) for each fund
- Generates two key plots:
  1.  Line chart showing **average return by time period**
  2.  Scatter plot of **risk (volatility) vs average return**

## DATA

Expected CSV file format:

| Fund Code | Fund Name | Category | 1 Ay (%) | 3 Ay (%) | 6 Ay (%) | ... |
|-----------|-----------|----------|----------|----------|----------|-----|

- Located at: `\001\data\1.ay.csv`
- Must include the return columns as listed in `sayisal_kolonlar`

---

##  Sample Output Visualizations

Saved automatically to the `/001/outputs/` directory:

- `grafik1.png` → Average return by time period
- `grafik2.png` → Risk vs return for all funds



