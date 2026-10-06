import requests

def get_trending():

    url = "https://api.coingecko.com/api/v3/search/trending"

    try:

        data = requests.get(url, timeout=10).json()

        msg = "🔥 TRENDING TOKENS\n\n"

        for i, coin in enumerate(data["coins"], 1):

            item = coin["item"]

            msg += (
                f"{i}. {item['name']} ({item['symbol']})\n"
                f"⭐ Rank: {item['market_cap_rank']}\n\n"
            )

        return msg

    except Exception as e:
        return str(e)