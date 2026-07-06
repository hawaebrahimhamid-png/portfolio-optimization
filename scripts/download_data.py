import os
import pandas as pd
import yfinance as yf

BASE_DIR = r"C:\Users\admin\Desktop\10-academy\portfolio-optimization"
DATA_DIR = os.path.join(BASE_DIR, "data", "processed")
os.makedirs(DATA_DIR, exist_ok=True)

tickers = ["TSLA", "BND", "SPY"]
frames = []

for t in tickers:
    print(f"Downloading {t}")

    df = yf.download(
        t,
        start="2015-01-01",
        end="2026-06-30",
        auto_adjust=False,
    )

    # Flatten MultiIndex columns
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df.reset_index()

    # Remove the column index name left by yfinance
    df.columns.name = None
    # Show columns so we can verify
    print(df.columns)

    df["Ticker"] = t

    # Rename first column to Date if needed
    if df.columns[0] != "Date":
        df = df.rename(columns={df.columns[0]: "Date"})

    df = df[["Date", "Open", "High", "Low", "Close", "Volume", "Ticker"]]

    frames.append(df)

final_df = pd.concat(frames, ignore_index=True)

print(final_df.head())
print(final_df.columns)

file_path = os.path.join(DATA_DIR, "combined_data.csv")
final_df.to_csv(file_path, index=False)

print("Saved to:", file_path)
