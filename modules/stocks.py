import yfinance as yf
import datetime
from iexfinance.stocks import Stock
from apikeys import iexkey


def get_ticker_price(ticker):
    now = datetime.datetime.now()
    if now.hour < 21:
        now = now - datetime.timedelta(days=1)
    print('Downloading stock data...')
    date_str = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    if now.weekday()<5:
        data = yf.download(ticker, date_str, date_str)
        price = data.Close[date_str]
    else:
        five_days_ago = now - datetime.timedelta(days=5)
        five_days_ago_str = str(five_days_ago.year) + '-' + str(five_days_ago.month) + '-' + str(five_days_ago.day)
        data = yf.download(ticker, five_days_ago_str, date_str)
        price = data.Close.iloc[-1]
    return price


def get_ticker_price_iex(ticker):
    data = Stock(ticker, token=iexkey).get_quote()
    return data['latestPrice']
