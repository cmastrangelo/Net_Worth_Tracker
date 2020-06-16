import json
from modules.cmc import CMC
import modules.helpers as helper
from tabulate import tabulate
import math
from decimal import Decimal
import datetime

net_worth = Decimal('0')
snapshots = helper.load_snapshots()
snapshot_data = {}

# Cryptocurrency
coinmarketcap = CMC()
with open('wallet/cryptocurrency.json', 'r') as f:
    crypto_data = json.loads(f.read())
crypto_totals = helper.get_all_cryptocurrency_prices(crypto_data, coinmarketcap)
cryptocurrency_net_worth = helper.display_and_get_cryptocurrency_totals(crypto_totals, coinmarketcap)
snapshot_data['cryptocurrency'] = crypto_totals
net_worth += cryptocurrency_net_worth

# Savings
savings_data = helper.collect_savings()
savings_total = helper.display_and_get_savings_totals(savings_data)
snapshot_data['savings'] = savings_data
net_worth += savings_total

# Robinhood
total_robinhood_value, robinhood_data = helper.get_robinhood_data()
snapshot_data['robinhood'] = robinhood_data
net_worth += total_robinhood_value

# Display total dedicated savings and investments
print('\n')
helper.display_total_dedicated_savings_and_investments(snapshot_data)

print('\nGetting projections...')
print('---------------------------------------------------------------------------------------------------------------')
last_14_day_slope = helper.get_projections()
last_point_slope, last_point_timeframe, fourteen_day_rate, increase_per_day = helper.get_last_point_slope()
print('\nLast 14 day slope:', last_14_day_slope)
print(
    'Last point slope:', last_point_slope, '-', last_point_timeframe,
    '(14 day rate of', str(fourteen_day_rate), 'or', str(increase_per_day), 'per day)'
)
print('---------------------------------------------------------------------------------------------------------------')
print('Total in Savings Account (Savings + Ren/Bills + Savings for Purchase):', helper.get_total_savings_and_rent(savings_data))
print('--------------------------------------------------------------------------------------------------------------')
print('Total for cryptocurrency:', cryptocurrency_net_worth, '(' + str(round(helper.get_percentage(cryptocurrency_net_worth, net_worth), 2)) + '%)')
print('Total for savings:', savings_total, '(' + str(round(helper.get_percentage(savings_total, net_worth), 2)) + '%)')
print('Total robinhood value:', total_robinhood_value, '(' + str(round(helper.get_percentage(total_robinhood_value, net_worth), 2)) + '%)')
print('------------------------------------------')
print('Total Net Worth:', net_worth, '\n\n')

latest_snapshot = helper.get_latest_snapshot()
print('Total last snapshot at ' +
      str(datetime.datetime.fromtimestamp(int(latest_snapshot['datetime']))) +
      ' value:',
      helper.get_snapshot_total_value(latest_snapshot))

while True:
    print('Press 1 to take snapshot, anything else to end')
    print('Press 2 to display graph.')
    i = int(input())
    if i == 1:
        # ~~~~~~~ Need to add savings_data to take_snapshot~~~~
        helper.take_snapshot(snapshot_data, coinmarketcap, snapshots)
    if i == 2:
        helper.display_snapshot_graph()
