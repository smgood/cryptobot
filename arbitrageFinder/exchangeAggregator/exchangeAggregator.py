from arbitrageFinder.objects.arbitrage import arbitrage

class exchangeAggregator ( ):

    def __init__(self):
        self.marketMaxValue = {}
        self.bestArbitrage = arbitrage ()

    def addPrices (self, exchangeMarket):
        for sellCurrency in exchangeMarket:
            for buyCurrency in exchangeMarket[sellCurrency]:

                if sellCurrency not in self.marketMaxValue:
                    self.marketMaxValue[sellCurrency] = {}

                # try to get the cheapest price for each trade
                if buyCurrency not in self.marketMaxValue[sellCurrency] or\
                exchangeMarket[sellCurrency][buyCurrency].price < self.marketMaxValue[sellCurrency][buyCurrency].price:
                    self.marketMaxValue[sellCurrency][buyCurrency] = exchangeMarket[sellCurrency][buyCurrency]

#--------------------------------------------------------------------------------------------------------------------------------

    def getBestArbitrage (self):
        for currency1 in self.marketMaxValue:
            for currency2 in self.marketMaxValue[currency1]:

                trade1 = self.marketMaxValue[currency1][currency2]
                trade2 = self.marketMaxValue[currency2][currency1]

                profitMarginPercentage = self.__getProfitMargin (trade1, trade2)

                if profitMarginPercentage > self.bestArbitrage.profitMarginPercentage:
                    self.bestArbitrage.trade1 = trade1
                    self.bestArbitrage.trade2 = trade2
                    self.bestArbitrage.profitMarginPercentage = profitMarginPercentage

        return self.bestArbitrage

    def __getProfitMargin (self, trade1, trade2):
        diff = 1/(trade1.price * trade2.price) - 1

        tradeFee1 = trade1.exchange.tradeFee
        tradeFee2 = trade2.exchange.tradeFee

        return (diff - tradeFee1 - tradeFee2) * 100
