import requests

def get_onchain():

    text = "🐋 ON-CHAIN REPORT\n\n"

    # ==========================
    # Trending Coins
    # ==========================
    try:
        url = "https://api.coingecko.com/api/v3/search/trending"
        data = requests.get(url, timeout=10).json()

        text += "🔥 Trending Coins\n"

        for i, coin in enumerate(data["coins"][:5], start=1):
            item = coin["item"]
            text += f"{i}. {item['name']} ({item['symbol']})\n"

        text += "\n"

    except Exception:
        text += "❌ Không lấy được Trending Coin\n\n"

    # ==========================
    # Global Market
    # ==========================
    try:
        url = "https://api.coingecko.com/api/v3/global"
        market = requests.get(url, timeout=10).json()["data"]

        btc = market["market_cap_percentage"]["btc"]
        total = market["total_market_cap"]["usd"] / 1e12

        text += "📊 Market Overview\n"
        text += f"• BTC Dominance: {btc:.2f}%\n"
        text += f"• Total Market Cap: ${total:.2f}T\n\n"

    except Exception:
        pass

    text += "🐳 Whale Activity\n"
    text += "• Coming Soon\n\n"

    text += "💰 Stablecoin Flow\n"
    text += "• Coming Soon\n\n"

    text += "🚨 Rugpull / Exploit\n"
    text += "• Coming Soon"

    return text