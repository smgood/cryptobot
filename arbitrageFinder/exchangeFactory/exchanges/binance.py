from arbitrageFinder.exchangeFactory.exchange import exchange
from arbitrageFinder.objects.trade import trade

from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode
import json

import hmac
import hashlib
import time
import requests

#api info: https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md
class binance ( ):

    def __init__(self, apiKey, secret):
        self.apiKey = apiKey
        self.secret = secret

        self.market = {}
        self.currencies = {}
        self.currencyPairs = {}
        self.tradeFee = 0.001 # all trades = 0.1%

        self.__getCurrencies ()
        self.__getCurrencyPairs()

    def getExchangeName (self):
        return 'binance'

    def apiQuery(self, path, type, method='GET', req=None):
        #Override Python’s treatment of mutable default arguments
        if req is None:
            req = {}

        url = 'https://api.binance.com' + path

        if type is 'public':
            dataBytes = urlopen(
                Request(
                    url + '?' + urlencode(req),
                    method=method
                )
            )

        else:
            req['timestamp'] = int(time.time() * 1000)
            signature = hmac.new(self.secret.encode(), urlencode(req).encode(), hashlib.sha512).hexdigest()
            req['signature'] = signature

            dataBytes = urlopen(
                Request(
                    url + '?' + urlencode(req),
                    method=method,
                    headers={'X-MBX-APIKEY': self.apiKey}
                )
            )

        return json.loads(dataBytes.read().decode('utf-8'))

#--------------------------------------------------------------------------------------------------------------------------------
    def getMarketPrices (self):
        data = self.apiQuery('/api/v3/ticker/bookTicker', 'public')

        for singleMarket in data:
            currencyPair = self.currencyPairs[singleMarket['symbol']]

            # Verify price not set to 0, market is active, and currencies are active
            if float(singleMarket['bidPrice']) > 0 and\
            currencyPair['isActive'] and\
            self.__isNotDisabled(currencyPair['base']) and\
            self.__isNotDisabled(currencyPair['quote']):
                self.__addCurrencyPairToMarket(
                    currencyPair['base'],
                    currencyPair['quote'],
                    1/float(singleMarket['bidPrice'])
                )
                self.__addCurrencyPairToMarket(
                    currencyPair['quote'],
                    currencyPair['base'],
                    float(singleMarket['askPrice'])
                )
        return self.market

    def __addCurrencyPairToMarket (self, sell, buy, price):
        if sell not in self.market:
            self.market[sell] = {}
        self.market[sell][buy] = trade(self, price, sell, buy)

    #Currently Binance does not support API to check wallet status for each coin
    def __getCurrencies (self):
        dataBytes = urlopen('https://www.binance.com/assetWithdraw/getAllAsset.html')
        data = json.loads(dataBytes.read().decode('utf-8'))

        for currency in data:
            currencySymbol = currency['assetCode']
            self.currencies[currencySymbol] = bool(currency['enableWithdraw'])

    def __isNotDisabled (self, currency):
        return (self.currencies[currency])

    def __getCurrencyPairs (self):
        data = self.apiQuery('/api/v1/exchangeInfo', 'public')
        currencyPairs = data['symbols']
        for pair in currencyPairs:
            self.currencyPairs[pair['symbol']] = {
                'base': pair['baseAsset'],
                'quote': pair['quoteAsset'],
                'isActive': (pair['status'] == 'TRADING')
            }
