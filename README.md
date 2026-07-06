# Portfolio Optimization using Time Series Forecasting

## Week 9 Challenge - 10 Academy AI Mastery

### Project Overview

This project focuses on historical financial data analysis for portfolio optimization. Using the YFinance API, historical market data for Tesla (TSLA), Vanguard Total Bond Market ETF (BND), and the SPDR S&P 500 ETF (SPY) was collected and analyzed to understand market behavior before developing forecasting models.

The project supports Guide Me in Finance (GMF) Investments by providing insights into asset performance, volatility, and risk, which will be used in later forecasting and portfolio optimization tasks.

---

## Assets

- TSLA – Tesla Inc.
- BND – Vanguard Total Bond Market ETF
- SPY – SPDR S&P 500 ETF

Period:

January 1, 2015 – June 30, 2026

---

## Project Structure

```
portfolio-optimization/
│
├── data/
│   └── processed/
│       └── combined_data.csv
│
├── notebooks/
│   └── task1_eda.ipynb
│
├── scripts/
│   └── download_data.py
│
├── src/
├── tests/
├── README.md
└── requirements.txt
```

---

## Task 1 Objectives

- Download historical financial data using YFinance
- Clean and preprocess the datasets
- Perform exploratory data analysis (EDA)
- Calculate daily returns
- Analyze rolling statistics
- Detect outliers
- Perform stationarity testing using the Augmented Dickey-Fuller (ADF) Test
- Calculate Value at Risk (VaR)
- Calculate the Sharpe Ratio

---

## Data Cleaning

The following preprocessing steps were completed:

- Downloaded TSLA, BND, and SPY historical data
- Flattened MultiIndex columns from YFinance
- Combined all assets into one dataset
- Converted the Date column to datetime format
- Sorted data by Ticker and Date
- Checked missing values
- Checked duplicate records
- Verified data types

---

## Exploratory Data Analysis

The following visualizations were created:

- Closing Price Trends
- Daily Returns
- 30-Day Rolling Mean
- 30-Day Rolling Volatility
- Daily Return Distribution
- Boxplots for Outlier Detection

Additional analysis included:

- Highest Daily Returns
- Lowest Daily Returns

---

## Stationarity Test

The Augmented Dickey-Fuller (ADF) Test was performed.

Results:

- Closing Prices
  - Non-stationary
  - p-value > 0.05

- Daily Returns
  - Stationary
  - p-value < 0.05

This indicates that differencing is required before applying ARIMA models to stock prices.

---

## Risk Metrics

Risk metrics calculated include:

- Daily Returns
- 95% Historical Value at Risk (VaR)
- Annualized Sharpe Ratio

These metrics help evaluate the risk-return characteristics of each asset.

---

## Key Findings

- Tesla exhibited a strong long-term upward trend.
- Tesla showed substantially higher volatility than BND and SPY.
- Daily returns fluctuated around zero and were stationary.
- Closing prices were non-stationary and require differencing before ARIMA modeling.
- Tesla had the highest downside risk based on the 95% Value at Risk.
- The Sharpe Ratio indicated a positive but moderate risk-adjusted return.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- YFinance
- Statsmodels
- Scikit-learn
- Jupyter Notebook

---

## Future Work

The next phase of the project will include:

- ARIMA Model
- SARIMA Model
- LSTM Forecasting
- Portfolio Optimization
- Efficient Frontier
- Portfolio Backtesting
