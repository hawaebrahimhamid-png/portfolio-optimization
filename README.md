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

# Task 2: Time Series Forecasting Models

## Objective

The objective of this task was to develop, train, and evaluate multiple time series forecasting models to predict Tesla stock closing prices. The models implemented include classical statistical models (ARIMA and Auto-ARIMA) and a deep learning approach (LSTM).

The goal was to compare model performance based on accuracy, complexity, and interpretability.

---

# 1. Data Preparation

The Tesla stock dataset was prepared for time series forecasting.

- The data was split chronologically to preserve the time order.
- Training data was used for model fitting.
- Testing data was used for evaluating future price predictions.
- Random shuffling was avoided because it can introduce future information into the training process.

The target variable used for forecasting was:

- **Close Price**

---

# 2. ARIMA Model

A classical ARIMA model was implemented to forecast Tesla stock prices.

## Model Selection

The ARIMA parameters were selected using time series analysis techniques and model evaluation.

The selected model:

```
ARIMA(1,1,1)
```

Parameters:

- p = 1 (autoregressive term)
- d = 1 (differencing)
- q = 1 (moving average term)

The model was trained using the training dataset and used to generate forecasts for the test period.

---

# 3. Auto-ARIMA Optimization

Auto-ARIMA was used to automatically search for the best ARIMA parameters by minimizing the Akaike Information Criterion (AIC).

The selected model:

```
ARIMA(0,1,0)
```

Auto-ARIMA helped optimize the model selection process without manually testing different parameter combinations.

---

# 4. LSTM Model

A Long Short-Term Memory (LSTM) neural network was developed to capture nonlinear patterns in Tesla stock prices.

## Data Preparation

The closing prices were scaled using:

```
MinMaxScaler
```

A sequence length of 60 days was used:

- Previous 60 days → Predict next day

The input data was reshaped into:

```
(samples, time steps, features)

(8604, 60, 1)
```

---

## LSTM Architecture

The model architecture:

- LSTM layer with 50 units
- Dropout layer (0.2)
- LSTM layer with 50 units
- Dropout layer (0.2)
- Dense output layer

Training configuration:

- Optimizer: Adam
- Loss function: Mean Squared Error
- Epochs: 20
- Batch size: 32

---

# 5. Model Evaluation

The models were evaluated using:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)

Lower values indicate better forecasting performance.

## Results Comparison

| Model | MAE | RMSE | MAPE |
|---|---:|---:|---:|
| ARIMA | 54.46 | 70.58 | 17.25% |
| Auto-ARIMA | 54.44 | 70.54 | 17.24% |
| LSTM | 256.28 | 259.66 | 72.23% |

---

# 6. Model Selection Discussion

Based on the evaluation results, **Auto-ARIMA achieved the best performance** with the lowest MAE, RMSE, and MAPE values.

The ARIMA-based models performed better than the LSTM model because Tesla stock prices in this dataset were better captured by statistical time-series patterns.

The LSTM model produced higher errors, possibly because:

- Only the closing price was used as input.
- Stock prices contain high levels of noise and uncertainty.
- More hyperparameter tuning and additional features may be required.

Although LSTM models are powerful for learning complex patterns, the simpler Auto-ARIMA model provided better forecasting accuracy in this experiment.

---

# Conclusion

Three forecasting approaches were developed and compared:

- ARIMA
- Auto-ARIMA
- LSTM

The final selected model was:

**Auto-ARIMA**

because it achieved the lowest forecasting errors and provided the most accurate predictions for Tesla stock prices in the test period.
## Project Structure

The project follows a modular structure:

- src/: reusable Python modules
- notebooks/: analysis notebooks
- tests/: automated tests
- data/: datasets
- .github/workflows/: CI pipeline

## Task 3: Forecast Future Market Trends

### Objective

Forecast Tesla stock prices for the next six months using the best-performing forecasting model.

### Completed Work

- Selected Auto-ARIMA as the best forecasting model.
- Generated a six-month Tesla stock price forecast.
- Visualized historical prices, forecasts, and 95% confidence intervals.
- Analyzed forecast trends and uncertainty.
- Identified investment opportunities and risks.
- Saved the forecast for future portfolio optimization.

