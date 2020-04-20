from decimal import Decimal
from tabulate import tabulate
from modules.stocks import get_ticker_price_iex
import math
import json
import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from pandas.plotting import register_matplotlib_converters


def collect_savings():
    with open('wallet/savings.json') as f:
        return json.loads(f.read())


def display_snapshot_graph():
    snapshot_data = load_snapshots()
    list_of_datetimes = []
    list_of_totals = []
    for snapshot_timestamp in snapshot_data:
        total_value = get_snapshot_total_value(snapshot_data[snapshot_timestamp])
        snapshot_datetime = datetime.datetime.fromtimestamp(int(snapshot_timestamp))
        list_of_datetimes.append(snapshot_datetime)
        list_of_totals.append(total_value)

    register_matplotlib_converters()
    fig, ax = plt.subplots()
    ax.plot(list_of_datetimes, list_of_totals)

    fmt = '${x:,.0f}'
    tick = mtick.StrMethodFormatter(fmt)
    ax.yaxis.set_major_formatter(tick)
    plt.gcf().autofmt_xdate()
    plt.show()


def get_all_cryptocurrency_prices(crypto_data, coinmarketcap):
    crypto_totals = {}
    full_symbol_list = []
    for location in crypto_data:
        for symbol in crypto_data[location]:
            if symbol not in full_symbol_list:
                full_symbol_list.append(symbol)
    coinmarketcap.update_prices(full_symbol_list)
    for location in crypto_data:
        print('Cryptocurrencies in', location.title() + ':')
        table = []
        columns = ['Symbol', 'Quantity', 'Price', 'Value']
        table.append(columns)
        for crypto_symbol in crypto_data[location]:
            qty = Decimal(str(crypto_data[location][crypto_symbol]))
            print(coinmarketcap.get_price(crypto_symbol))
            price = Decimal(str(coinmarketcap.get_price(crypto_symbol)))
            value = Decimal(str(math.floor(qty * price * Decimal(100)) / Decimal(100)))
            if crypto_symbol in crypto_totals:
                crypto_totals[crypto_symbol] += qty
            else:
                crypto_totals[crypto_symbol] = qty
            table.append([crypto_symbol.upper(), qty, price, value])
        print(tabulate(table, headers="firstrow"), end='\n\n')
    return crypto_totals


def get_robinhood_data():
    with open('wallet/robinhood.json') as f:
        robinhood_file_data = json.loads(f.read())
    robinhood_data = {}
    total_robinhood_value = Decimal('0')
    print('Displaying robinhood totals:')
    for stock_symbol in robinhood_file_data:
        total_symbol_value = Decimal('0')
        if stock_symbol == 'wallet':
            print('Wallet:')
            wallet_table = [['Type', 'Value']]
            robinhood_data['wallet'] = {}
            for wallet_type in robinhood_file_data['wallet']:
                wallet_table.append((wallet_type, robinhood_file_data['wallet'][wallet_type]))
                value = Decimal(str(robinhood_file_data['wallet'][wallet_type]))
                robinhood_data['wallet'][wallet_type] = str(value)
                total_robinhood_value += value
                total_symbol_value += Decimal(str(value))
            print(tabulate(wallet_table, headers="firstrow"), end='\n')
            print('Wallet total:', total_symbol_value, '\n')
        else:
            total_qty = 0
            price = Decimal(str(get_ticker_price_iex(stock_symbol)))
            symbol_dict = {'price': str(price)}
            print('Symbol', stock_symbol, 'Price:', symbol_dict['price'])
            stock_table = [['Type', 'Qty', 'Value']]
            for stock_symbol_type in robinhood_file_data[stock_symbol]:
                qty = Decimal(str(robinhood_file_data[stock_symbol][stock_symbol_type]))
                value = qty * price
                symbol_dict[stock_symbol_type] = str(qty)
                stock_table.append((stock_symbol_type, qty, value))
                total_robinhood_value += value
                total_qty += qty
                total_symbol_value += Decimal(value)
            robinhood_data[stock_symbol] = symbol_dict
            print(tabulate(stock_table, headers='firstrow'), end='\n')
            print('Total for', stock_symbol + ': $' + str(total_symbol_value) + ' with', total_qty, 'stocks.\n')

    return total_robinhood_value, robinhood_data


def display_and_get_cryptocurrency_totals(crypto_totals, coinmarketcap):
    print('Cryptocurrencies totals:')
    table = []
    columns = ['Symbol', 'Quantity', 'Price', 'Value']
    table.append(columns)
    cryptocurrency_net_worth = Decimal('0')
    for crypto_symbol in crypto_totals:
        qty = Decimal(str(crypto_totals[crypto_symbol]))
        price = Decimal(str(coinmarketcap.get_price(crypto_symbol)))
        value = Decimal(str(math.floor(qty * price * Decimal('100')) / Decimal('100')))
        cryptocurrency_net_worth += value
        table.append([crypto_symbol.upper(), qty, price, value])
    print(tabulate(table, headers="firstrow"), end='\n\n')
    return cryptocurrency_net_worth


def get_savings_table(savings_data):
    table = [['Type', 'Quantity']]
    for saving_type in savings_data:
        table.append([saving_type, savings_data[saving_type]])
    return table


def get_savings_total(table):
    total = Decimal('0')
    for saving_type in table[1:]:
        total += Decimal(str(saving_type[1]))
    return total


def get_total_rent_and_bills(rent_and_bills):
    total = Decimal('0')
    for amount in rent_and_bills:
        total += Decimal(str(amount))
    return total


def display_and_get_savings_totals(savings_data):
    table = get_savings_table(savings_data)
    print('Savings total:')
    print(tabulate(table, headers="firstrow"), end='\n\n')
    total = get_savings_total(table)
    return total


def display_total_dedicated_savings_and_investments(snapshot_data):
    total_dedicated_dict = {}
    for savings_type in snapshot_data['savings']:
        total_dedicated_dict[savings_type] = Decimal(str(snapshot_data['savings'][savings_type]))
    for symbol in snapshot_data['robinhood']:
        if symbol == 'wallet':
            for symbol_type in snapshot_data['robinhood'][symbol]:
                total_dedicated_dict[symbol_type] += Decimal(str(snapshot_data['robinhood'][symbol][symbol_type]))
        else:
            price = snapshot_data['robinhood'][symbol]['price']
            for symbol_type in snapshot_data['robinhood'][symbol]:
                if symbol_type != 'price':
                    total_dedicated_dict[symbol_type] += Decimal(str((snapshot_data['robinhood'][symbol][symbol_type]))) * Decimal(str(float(price)))
    print('Displaying total dedicated savings and investments:')

    rows = [['Type', 'Value']]
    for savings_type in total_dedicated_dict:
        rows.append([savings_type, total_dedicated_dict[savings_type]])
    print(tabulate(rows, headers="firstrow"), end='\n\n')


def get_snapshot_total_value(snapshot):
    total = Decimal('0')
    for comodity in snapshot:
        if comodity == 'cryptocurrency':
            for t in snapshot[comodity]:
                total += Decimal(snapshot[comodity][t]['value'])
        if comodity == 'savings':
            for t in snapshot[comodity]:
                total += Decimal(str(snapshot[comodity][t]))
        if comodity == 'robinhood':
            for comodity_symbol in snapshot[comodity]:
                if comodity_symbol == 'wallet':
                    for wallet_type in snapshot[comodity][comodity_symbol]:
                        total += Decimal(snapshot[comodity]['wallet'][wallet_type])
                else:
                    price = Decimal('0')
                    for stock_type in snapshot[comodity][comodity_symbol]:
                        if stock_type != 'price':
                            total += Decimal(snapshot[comodity][comodity_symbol]['price']) * Decimal(snapshot[comodity][comodity_symbol][stock_type])
    return total


def get_latest_snapshot():
    snapshots = load_snapshots()
    latest_snapshot = ''
    for snapshot in snapshots:
        if latest_snapshot == '':
            latest_snapshot = snapshot
        else:
            if snapshot > latest_snapshot:
                latest_snapshot = snapshot
    snapshots[latest_snapshot]['datetime'] = latest_snapshot
    return snapshots[latest_snapshot]


def make_projection(snapshot_list, second_point_index, index_delta):
    snapshot_1 = snapshot_list[-1]
    snapshot_2 = snapshot_list[second_point_index]
    datetime_1 = datetime.datetime.fromtimestamp(Decimal(snapshot_1[0]))
    datetime_2 = datetime.datetime.fromtimestamp(Decimal(snapshot_2[0]))
    time_delta = datetime_1 - datetime_2
    print('Projection for last timeframe:', time_delta)
    value_2 = Decimal(get_snapshot_total_value(snapshot_2[1]))
    value_1 = Decimal(get_snapshot_total_value(snapshot_1[1]))
    print('Most recent:', value_2, 'Last timeframe:', value_1)
    point_2 = (0, value_2)
    point_1 = (1, value_1)

    m = Decimal(str((point_2[1] - point_1[1]) / (point_2[0] - point_1[0])))
    b = Decimal(str(point_2[1]))
    projection = m*Decimal(str((index_delta + 1)))+b
    prediction_time_delta = time_delta * index_delta
    prediction_datetime = datetime_1 + prediction_time_delta
    number_of_gaps_between_points = Decimal('-1') * Decimal(second_point_index) - Decimal('1')
    m_per_datapoint = round(m / number_of_gaps_between_points, 2)

    print('At slope', m_per_datapoint, 'the projection for', prediction_datetime, 'is', projection)


def get_projections():
    snapshots = load_snapshots()
    snapshot_list = snapshot_to_list(snapshots)

    # First comparison
    make_projection(snapshot_list, -2, 12)
    make_projection(snapshot_list, -4, 6)
    make_projection(snapshot_list, -8, 1.5)


def load_snapshots():
    with open('snapshots.json', 'r') as f:
        return json.loads(f.read())


def load_rent_and_bills():
    with open('wallet/rent_and_bills.json') as f:
        return json.loads(f.read())


def save_snapshots(snapshot):
    with open('snapshots.json', 'w') as f:
        json.dump(snapshot, f, indent=2)


def snapshot_to_list(snapshots):
    snapshot_list = []
    for snapshot_timestamp in snapshots:
        snapshot_list.append((snapshot_timestamp, snapshots[snapshot_timestamp]))
    snapshot_list.sort(key=lambda x: x[0])
    return snapshot_list


def take_snapshot(snapshot_data, coinmarketcap, snapshots):
    snapshot = {}
    if 'cryptocurrency' in snapshot_data:
        snapshot['cryptocurrency'] = {}
        for crypto_symbol in snapshot_data['cryptocurrency']:
            qty = Decimal(str(snapshot_data['cryptocurrency'][crypto_symbol]))
            price = Decimal(str(coinmarketcap.get_price(crypto_symbol)))
            value = Decimal(str(math.floor(qty * price * Decimal('100')) / Decimal('100')))
            snapshot['cryptocurrency'][crypto_symbol] = {'qty': str(qty), 'price': str(price), 'value': str(value)}
    if 'savings' in snapshot_data:
        snapshot['savings'] = {}
        for savings_type in snapshot_data['savings']:
            snapshot['savings'][savings_type] = snapshot_data['savings'][savings_type]
    if 'robinhood' in snapshot_data:
        snapshot['robinhood'] = snapshot_data['robinhood']
    snapshots[str(round(datetime.datetime.now().timestamp()))] = snapshot
    save_snapshots(snapshots)


def get_percentage(this, total):
    return Decimal(str(this)) * Decimal('100') / Decimal(str(total))


def get_total_savings_and_rent(savings_data):
    table = get_savings_table(savings_data)
    total = get_savings_total(table)
    rent_and_bills = load_rent_and_bills()
    total_rend_and_bills = get_total_rent_and_bills(rent_and_bills)
    return str(total + total_rend_and_bills)
