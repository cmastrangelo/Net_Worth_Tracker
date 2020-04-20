# Import yfinance
import yfinance as yf

# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
data = yf.download('TERP', '2019-09-18', '2019-09-18')

# Plot the close prices
import matplotlib.pyplot as plt

print(data.Close)