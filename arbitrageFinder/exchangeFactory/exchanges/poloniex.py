from arbitrageFinder.exchangeFactory.exchange import exchange
from arbitrageFinder.objects.trade import trade

from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode
import json

import hmac
import hashlib
import time

#api info: https://poloniex.com/support/api/
class poloniex ( ):

    def __init__(self, apiKey, secret):
        self.apiKey = apiKey
        self.secret = secret

        self.market = {}
        self.currencies = {}
        self.tradeFee = 0.002 #takerFee = 0.2%, makerFee = 0.1%

        self.__getCurrencies ()

    def getExchangeName (self):
        return 'poloniex'

    def apiQuery(self, command, type, req=None):
        #Override Python’s treatment of mutable default arguments
        if req is None:
            req = {}

        if type == 'public':
            url = 'https://poloniex.com/public?command=' + command + '&' + urlencode(req)
            dataBytes = urlopen(url)
        else:
            url = 'https://poloniex.com/tradingApi'
            req['command'] = command
            req['nonce'] = int(time.time())
            postData = urlencode(req)

            signature = hmac.new(self.secret.encode(), postData.encode(), hashlib.sha512).hexdigest()
            headers = {
                'Sign': signature,
                'Key' : self.apiKey
            }

            dataBytes = urlopen(
                Request(
                    url,
                    postData,
                    headers
                    )
            )

        return json.loads(dataBytes.read().decode('utf-8'))

#--------------------------------------------------------------------------------------------------------------------------------

    def getMarketPrices (self):
        dataJson = self.apiQuery('returnTicker', 'public')

        for key in dataJson:
            marketInfo = dataJson[key]
            currencyPair = key.split('_')

            # Verify 2 currencies, price not set to 0, market is active, and currencies are active
            if len(currencyPair) == 2 and \
            float(marketInfo['lowestAsk']) > 0 and\
            not int(marketInfo['isFrozen']) and\
            self.__isNotDisabled(currencyPair[0]) and\
            self.__isNotDisabled(currencyPair[1]):
                self.__addCurrencyPairToMarket(
                    currencyPair[0],
                    currencyPair[1],
                    float(marketInfo['lowestAsk'])
                )
                self.__addCurrencyPairToMarket(
                    currencyPair[1],
                    currencyPair[0],
                    1/float(marketInfo['highestBid']))
        return self.market

    def __addCurrencyPairToMarket (self, sell, buy, price):
        if sell not in self.market:
            self.market[sell] = {}
        self.market[sell][buy] = trade (self, price, sell, buy)

    def __getCurrencies (self):
        dataJson = self.apiQuery('returnCurrencies', 'public')
        for key in dataJson:
            self.currencies[key] = not bool(dataJson[key]['disabled'])

    def __isNotDisabled (self, currency):
        return (self.currencies[currency])
