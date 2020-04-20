from coinmarketcap.clients import CoinMarketCapClient
from iexfinance.stocks import Stock
import json
import datetime
import time

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from apikeys import iexkey, cmckey


def get_price_from_iexfinance(symbol):
    if symbol == 'btc':
        data = Stock("BTCUSDT", token=iexkey).get_quote()
    if symbol == 'eth':
        data = Stock('ETHUSDT', token=iexkey).get_quote()
    return data['latestPrice']


class CMC:
    def __init__(self):
        self.coins = {}

    def get_price(self, symbol):
        return self.coins[symbol]

    def update_prices(self, full_symbol_list):
        print('Updating cache:')
        for symbol in full_symbol_list:
            print(symbol)
            if symbol == 'eth' or symbol == 'btc':
                coin_price = get_price_from_iexfinance(symbol)
                print(coin_price)
            else:
                url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
                parameters = {
                    'symbol': symbol.upper()
                }
                headers = {
                    'Accepts': 'application/json',
                    'X-CMC_PRO_API_KEY': cmckey,
                }

                session = Session()
                session.headers.update(headers)

                try:
                    response = session.get(url, params=parameters)
                    data = json.loads(response.text)
                    print(data)
                    coin_price = str(data['data'][symbol.upper()]['quote']['USD']['price'])
                except (ConnectionError, Timeout, TooManyRedirects) as e:
                    print(e)

            self.coins[symbol] = coin_price
        else:
            print('Using old cache...')
