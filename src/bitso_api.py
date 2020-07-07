import os
import time
import json
import hmac
import hashlib
import requests

os.getcwd()

class BitsoAPI:
    def __init__(self, book = 'btc_mxn'):
        self.book = book
        self.__url = 'https://api.bitso.com/v3/'
        self.__key = os.environ['BITSO_API_KEY']
        self.__secret = os.environ['BITSO_API_SECRET']
        self.nonce = str(int(round(time.time() * 1000)))

    def trades(self, limit = 25):
        endpoint = 'trades/?book={}&limit={}'.format(self.book, limit)
        url = self.__url + endpoint 
        return requests.get(url).json()

    def account_status(self):
        endpoint = 'account_status'
        return self.__get_requests(endpoint)

    def account_balance(self):
        endpoint = 'balance'
        return self.__get_requests(endpoint)
   
    def place_order(self, price, major = 1):
        parameters = {
            'book': self.book,
            'major': major,
            'price': price,
            'side': 'buy',
            'type': 'limit',
        }
        endpoint = 'orders'
        return self.__post_requests(self, endpoint, parameters)

    def __get_requests(self, endpoint):
        url = self.__url + endpoint
        headers = { 'Authorization' : self.__auth(endpoint = endpoint) }
        return requests.get(url, headers = headers).json()

    def __post_requests(self, endpoint, parameters):
        url = self.__url + endpoint
        headers = {
            'Authorization': self.__auth(endpoint = endpoint, verb = 'POST', parameters = parameters)
        }
        return requests.post(url, json = parameters, headers = header).json()

    def __auth(self, endpoint, verb = 'GET', parameters = {}):
        return 'Bitso %s:%s:%s' % (self.__key, self.nonce, self.__signature(endpoint, verb, parameters))
    
    def __signature(self, endpoint, verb = 'GET', parameters = {}):
        message = self.nonce + verb + '/v3/' + endpoint
        if(verb == 'POST'):
            message += json.dumps(parameters)
        return hmac.new(self.__secret.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()

