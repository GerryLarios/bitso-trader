import requests

api_url = 'https://api.bitso.com/v3/trades' 

def fetch_trades(book = 'btc_mxn', limit = 100):
    url = api_url + '/?book={}&limit={}'.format(book, limit)
    return requests.get(url).json()

