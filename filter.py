keywords = [
    "bitcoin",
    "ethereum",
    "crypto",
    "btc",
    "eth",
    "etf",
    "fed",
    "sec",
    "binance",
    "hack",
    "whale",
    "liquidation",
    "government",
    "senate",
    "market"
]


def important_news(news):

    result = []

    for item in news:
        title = item["title"].lower()

        if any(k in title for k in keywords):
            result.append(item)

    return result