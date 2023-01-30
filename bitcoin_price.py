import apikey
import requests
import json


header = {
    'X-CMC_PRO_API_KEY' : apikey.key,
    'Accepts': 'application/json'
}

params = {
    'start' : '1', 
    'limit' : '1',
    'convert' : 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

bitJson = requests.get(url, params=params, headers=header).json()

currentTime = bitJson['status']['timestamp']
coins = bitJson['data']