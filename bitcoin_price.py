import requests
import apikey
import time

class BitcoinPrice:
    header = {
        'X-CMC_PRO_API_KEY' : apikey.key,
        'Accepts': 'application/json'
    }

    params = {
        'start' : '1', 
        'limit' : '1',
        'convert' : 'USD'
    }

    historicalUrl = 'https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USD&limit=2000&toTs=-1&api_key=05bde4f591713196c1ddb739ed58ce648b1be4869278e315286711285e80ad1b'
    liveUpdateUrl = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    @staticmethod
    def get_historical_data():
        historical_data = requests.get(BitcoinPrice.historicalUrl).json()
        return historical_data['Data']

    @staticmethod
    def get_live_data():
        live_data = requests.get(BitcoinPrice.liveUpdateUrl, params=BitcoinPrice.params, headers=BitcoinPrice.header).json()
        return live_data['data'][0]['quote']['USD']['price'], live_data['status']['timestamp']

    @staticmethod
    def generate_chart(price_list, time_list, ax):
        historical_data = BitcoinPrice.get_historical_data()
        for data in historical_data['Data']:
            price_list.append(data['close'])
            time_list.append(data['time'])

        ax.plot(time_list, price_list, color='tab:red')

    @staticmethod
    def update(counter, price_list, time_list, ax, fig, plt):
        current_price, current_time = BitcoinPrice.get_live_data()
        price_list.append(current_price)
        time_list.append(current_time)
        ax.plot(time_list, price_list, color='tab:red')
        fig.canvas.draw()