from arbitrageFinder.main import getBestArbitrage

# list of supported exchanges
supportedExchanges = ['poloniex', 'bittrex', 'binance', 'hitbtc']

# find best aritrage opportunity
info = getBestArbitrage(supportedExchanges)

message = 'ARBITRAGE OPPORTUNITY\n'
message += 'Buy {} for {} on {}\n'.format(info.trade1.buy, info.trade1.sell, info.trade1.exchange.getExchangeName())
message += 'Buy {} for {} on {}\n'.format(info.trade2.buy, info.trade2.sell, info.trade2.exchange.getExchangeName())
message += 'Profit margin: {}%\n'.format(round(info.profitMarginPercentage, 5))
print (message)
