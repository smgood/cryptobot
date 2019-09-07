from .exchanges.poloniex import poloniex
from .exchanges.bittrex import bittrex
from .exchanges.binance import binance
from .exchanges.hitbtc import hitbtc

from .apiKeys import poloniexKey
from .apiKeys import bittrexKey
from .apiKeys import binanceKey

class exchangeFactory ( ):

    def createExchange (name):
        if name == 'poloniex':
            return poloniex (poloniexKey['key'], poloniexKey['secret'])
        elif name == 'bittrex':
            return bittrex (bittrexKey['key'], bittrexKey['secret'])
        elif name == 'binance':
            return binance (binanceKey['key'], binanceKey['secret'])
        elif name == 'hitbtc':
            return hitbtc ()
        else:
            return None
