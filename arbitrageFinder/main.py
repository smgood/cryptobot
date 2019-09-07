from .exchangeFactory.exchangeFactory import exchangeFactory
from .exchangeAggregator.exchangeAggregator import exchangeAggregator

def getBestArbitrage (supportedExchanges):

    # class that compares exchanges to find best arbtrage
    exchanges = exchangeAggregator ()

    # find best deal for each currency pair
    for exchangeName in supportedExchanges:
        exchange = exchangeFactory.createExchange (exchangeName)
        exchanges.addPrices(exchange.getMarketPrices())

    # find best aritrage opportunity
    return exchanges.getBestArbitrage()
