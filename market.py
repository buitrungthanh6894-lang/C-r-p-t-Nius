import requests

def get_market():

    try:

        url = "https://api.coingecko.com/api/v3/global"

        data = requests.get(url, timeout=10).json()["data"]

        total_cap = data["total_market_cap"]["usd"] / 1e12
        volume = data["total_volume"]["usd"] / 1e9
        btc_dom = data["market_cap_percentage"]["btc"]
        eth_dom = data["market_cap_percentage"]["eth"]
        active = data["active_cryptocurrencies"]
        markets = data["markets"]

        text = (
            "📊 CRYPTO MARKET\n\n"

            f"💰 Market Cap: ${total_cap:.2f}T\n"
            f"📈 24H Volume: ${volume:.2f}B\n\n"

            f"👑 BTC Dominance: {btc_dom:.2f}%\n"
            f"🟣 ETH Dominance: {eth_dom:.2f}%\n\n"

            f"🪙 Active Coins: {active:,}\n"
            f"🏦 Exchanges: {markets:,}"
        )

        return text

    except Exception as e:

        return f"❌ {e}"