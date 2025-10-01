# Stock Analysis - Quantitative Finance Intro

This project demonstrates fundamental quantitative finance and data analysis skills using Python.  
It pulls real stock market data, computes basic indicators, and visualizes insights for decision-making.

## Features
- Pulls real-time stock data from Yahoo Finance (using `yfinance`)
- Calculates key metrics:
  - Daily returns
  - 20-day and 50-day moving averages
- Creates clear visualizations:
  - Price chart with moving averages
  - Daily return histogram
- Demonstrates Python data analysis workflow (pandas, matplotlib)

## 🛠️ Tech Stack
- **Python 3.9+**
- **Libraries**: `pandas`, `matplotlib`, `yfinance`

## 📊 Example Output
Price chart with moving averages:

<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/2a197f59-db56-4c09-8832-291025960a67" />

Daily returns histogram:

<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/43550056-edbf-4452-aca7-2fd78f14303a" />



## 🧠 My learning

- I learned how to use the [`yfinance`](https://pypi.org/project/yfinance/) library to download real stock market data (price history, volume, etc.) directly into a Pandas DataFrame.
- Daily return measures the percent change in price from one day to the next.  
  Formula: `(today's close - yesterday's close) / yesterday's close`
- Show how much the stock moves each day and are used to measure risk and volatility.  
  For Apple, most daily returns stayed close to 0 (about ±1%), so the stock wasn’t very volatile in the data we looked at.
- A moving average smooths price fluctuations by taking the average of the last \(n\) days’ closing prices.
  - Example: **MA20** = mean of the last 20 closing prices.  
- Moving averages help reveal trends and reduce day-to-day noise.
- `NaN` means “Not a Number”...also means missing or undefined data.
- The first daily return is `NaN` because there’s no previous day to compare to.  
- The first 19 rows of MA20 are `NaN` because you need 20 days of data before the average can be calculated.
  - This creates a gap at the beginning when comparing the closing price to MA20, and an even bigger gap between the closing price and MA50 (and between MA20 and MA50) because MA50 needs 50 days of data.








