import requests
import apikey
import time
from datetime import datetime
import matplotlib.ticker as ticker

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
        return live_data['data'][0]['quote']['USD']['price'], live_data['status']['timestamp'], live_data['data'][0]['quote']['USD']['volume_24h']

    def generate_chart(price_list, time_list,volume_list, ax, plt):
        historical_data = BitcoinPrice.get_historical_data()
        previous_price = None
        for data in historical_data['Data']:
            current_price = data['close']
            price_list.append(current_price)
            time_list.append(data['time'])
            if previous_price is not None:
                if current_price > previous_price:
                    color = 'red'
                else:
                    color = 'blue'
                ax.plot(time_list[-2:], price_list[-2:], color=color)
            previous_price = current_price

        def format_xaxis(x, pos):
            """Convert unix timestamp to desired format."""
            return datetime.fromtimestamp(x).strftime('%d %b')

        # Set x-axis format
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_xaxis))
            
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.title('Bitcoin Price Over Time')
        
        # Adjust the size of the bottom chart
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width, box.height * 0.7])


    @staticmethod
    def update(counter, price_list, time_list,volume_list, ax, fig, plt):
        current_price, current_time, current_volume = BitcoinPrice.get_live_data()

        timestamp = datetime.strptime(current_time, '%Y-%m-%dT%H:%M:%S.%fZ')
        unix_timestamp = int(timestamp.timestamp())


        price_list.append(current_price)
        time_list.append(unix_timestamp)

        previous_price = price_list[-2] if len(price_list) > 1 else None
        if previous_price is not None:
            if current_price > previous_price:
                color = 'red'
            else:
                color = 'blue'
            ax.plot(time_list[-2:], price_list[-2:], color=color)

        def format_xaxis(x, pos):
            """Convert unix timestamp to desired format."""
            return datetime.fromtimestamp(x).strftime('%d %b')

        # Set x-axis format
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_xaxis))
        
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.title('Bitcoin Price Over Time')

        



    