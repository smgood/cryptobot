from arbitrageFinder.exchangeFactory.exchange import exchange
from arbitrageFinder.objects.trade import trade

from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode
import json

import hmac
import hashlib
import time

#api info: https://bittrex.com/home/api
class bittrex ( ):

    def __init__(self, apiKey, secret):
        self.apiKey = apiKey
        self.secret = secret

        self.market = {}
        self.currencies = {}
        self.tradeFee = 0.0025 # all trades 0.25%
        self.__marketsActive = {}

        self.__getCurrencies ()
        self.__getMarketsActive ()

    def getExchangeName(self):
        return 'bittrex'

    def apiQuery(self, command, type, req=None):
        #Override Python’s treatment of mutable default arguments
        if req is None:
            req = {}

        url = 'https://bittrex.com/api/v1.1/'

        if type is 'public':
            url += 'public/' + command + '?' + urlencode(req)
            dataBytes = urlopen(url)

        else:
            req['nonce'] = int(time.time())
            req['apikey'] = self.apiKey
            url += type + '/' + command + '?' + urlencode(req)

            signature = hmac.new(self.secret.encode(), url.encode(), hashlib.sha512).hexdigest()
            headers = {'apisign': signature}
            dataBytes = urlopen(
                Request(
                    url,
                    headers=headers
                    )
            )

        return json.loads(dataBytes.read().decode('utf-8'))

#--------------------------------------------------------------------------------------------------------------------------------

    def getMarketPrices(self):
        data = self.apiQuery('getmarketsummaries', 'public')

        for singleMarket in data['result']:
            currencyPair = self.__marketsActive[singleMarket['MarketName']]

            # Verify 2 currencies, price not set to 0, market is active, and currencies are active
            if float(singleMarket['Ask']) > 0 and\
            currencyPair['isActive'] and\
            self.__isNotDisabled(currencyPair['base']) and\
            self.__isNotDisabled(currencyPair['quote']):
                self.__addCurrencyPairToMarket(
                    currencyPair['base'],
                    currencyPair['quote'],
                    float(singleMarket['Ask'])
                )
                self.__addCurrencyPairToMarket(
                    currencyPair['quote'],
                    currencyPair['base'],
                    1 / float(singleMarket['Bid'])
                )
        return self.market

    def __addCurrencyPairToMarket (self, sell, buy, price):
        if sell not in self.market:
             self.market[sell] = {}
        self.market[sell][buy] = trade (self, price, sell, buy)

    def __getCurrencies (self):
        data = self.apiQuery('getcurrencies', 'public')
        for currency in data['result']:
            currencySymbol = currency['Currency']
            self.currencies[currencySymbol] = bool(currency['IsActive'])

    def __isNotDisabled (self, currency):
        return (self.currencies[currency])

    def __getMarketsActive (self):
        data = self.apiQuery('getMarkets', 'public')
        for market in data['result']:
            self.__marketsActive[market['MarketName']] = {
                'base': market['BaseCurrency'],
                'quote': market['MarketCurrency'],
                'isActive': bool(market['IsActive'])
            }
