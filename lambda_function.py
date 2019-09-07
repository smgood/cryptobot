from arbitrageFinder.main import getBestArbitrage
from twilio.rest import Client

def lambda_handler(event, context):

    # list of supported exchanges
    supportedExchanges = ['poloniex', 'bittrex', 'binance']

    # find best aritrage opportunity
    info = getBestArbitrage(supportedExchanges)

    if info.profitMarginPercentage > 5:
        message = 'ARBITRAGE OPPORTUNITY\n'
        message += 'Buy {} for {} on {}\n'.format(info.trade1.buy, info.trade1.sell, info.trade1.exchange.getExchangeName())
        message += 'Buy {} for {} on {}\n'.format(info.trade2.buy, info.trade2.sell, info.trade2.exchange.getExchangeName())
        message += 'Profit margin: {}%\n'.format(round(info.profitMarginPercentage, 3))

        # # Your Account SID from twilio.com/console
        account_sid = ""
        # Your Auth Token from twilio.com/console
        auth_token  = ""

        client = Client(account_sid, auth_token)

        sms = client.messages.create(
            to="", # ex: "+10123456789"
            from_="", # ex: "+10123456789"
            body=message
        )
