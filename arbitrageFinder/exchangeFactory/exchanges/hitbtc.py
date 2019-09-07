from arbitrageFinder.exchangeFactory.exchange import exchange
from arbitrageFinder.objects.trade import trade

from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode
import json

#api info: https://api.hitbtc.com/
class hitbtc ( ):

    def __init__(self):
        self.market = {}
        self.trades = {}
        self.currencies = {}
        self.tradeFee = 0.001 #takerFee = 0.1%, makerFee = +0.01%

        self.__getCurrencies()
        self.__getTrades()

    def getExchangeName(self):
        return 'hitbtc'

    def apiQuery(self, command, type, req=None):
        #Override Python’s treatment of mutable default arguments
        if req is None:
            req = {}

        url = 'https://api.hitbtc.com/api/2'

        if type is 'public':
            url += '/public/' + command + '?' + urlencode(req)
            dataBytes = urlopen(url)

        return json.loads(dataBytes.read().decode('utf-8'))

#--------------------------------------------------------------------------------------------------------------------------------

    def getMarketPrices(self):
        data = self.apiQuery('ticker', 'public')

        for singleMarket in data:
            currencyPair = self.trades[singleMarket['symbol']]

            # Verify 2 currencies, price not set to 0, market is active, and currencies are active
            if singleMarket['ask'] is not None and\
            singleMarket['bid'] is not None and\
            float(singleMarket['ask']) > 0 and\
            self.__isNotDisabled(currencyPair['base']) and\
            self.__isNotDisabled(currencyPair['quote']):
            #API is currently missing whether or not trade is frozen
            #currencyPair['isActive']
                self.__addCurrencyPairToMarket(
                    currencyPair['base'],
                    currencyPair['quote'],
                    1 / float(singleMarket['bid'])
                )
                self.__addCurrencyPairToMarket(
                    currencyPair['quote'],
                    currencyPair['base'],
                    float(singleMarket['ask'])
                )
        return self.market


    def __addCurrencyPairToMarket (self, sell, buy, price):
        if sell not in self.market:
             self.market[sell] = {}
        self.market[sell][buy] = trade (self, price, sell, buy)

    def __getTrades (self):
        data = self.apiQuery('symbol', 'public')
        for symbol in data:
            self.trades[symbol['id']] = {
                'base': symbol['baseCurrency'],
                'quote': symbol['quoteCurrency'],
            }

    def __getCurrencies (self):
        data = self.apiQuery('currency', 'public')
        for currency in data:
            self.currencies[currency['id']] =\
                not bool(currency['delisted']) and\
                bool(currency['transferEnabled']) and\
                bool(currency['payinEnabled']) and\
                bool(currency['payoutEnabled'])

    def __isNotDisabled (self, currency):
        return (self.currencies[currency])
