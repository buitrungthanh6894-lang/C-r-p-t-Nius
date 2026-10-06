import ccxt


exchange = ccxt.binance()


def get_price():

    btc = exchange.fetch_ticker("BTC/USDT")
    eth = exchange.fetch_ticker("ETH/USDT")


    return {
        "BTC": btc["last"],
        "ETH": eth["last"]
    }