import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

# Downlaoding the data for APPLE
ticker = "AAPL"
data = yf.download(ticker, period="2y")

print(data.columns)

# Calculating daily returns
data["Daily Return"] = data["Close"].pct_change()
data["MA20"] = data["Close"].rolling(20).mean()
data["MA50"] = data["Close"].rolling(50).mean()
data["MA20"].head(25)

# plot price with MA
plt.figure(figsize=(12, 6))
plt.plot(data["Close"], label="Close")
plt.plot(data["MA20"], label="MA20")
plt.plot(data["MA50"], label="MA50")
plt.title(f"{ticker} Price with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()

# Plotting as histogram

plt.figure(figsize=(8,5))
data["Daily Return"].hist(bins=50)
plt.title(f"{ticker} Daily Returns Histogram")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")
plt.show()
