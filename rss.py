import feedparser

IMPORTANT_KEYWORDS = [
    "Bitcoin",
    "BTC",
    "Ethereum",
    "ETH",
    "ETF",
    "BlackRock",
    "Fidelity",
    "SEC",
    "Binance",
    "Coinbase",
    "Solana",
    "SOL",
    "Whale",
    "Hack",
    "Exploit",
    "Rug",
    "Rugpull",
    "Liquidation",
    "Stablecoin",
    "USDT",
    "USDC",
    "Fed",
    "CPI",
    "Trump"
]

def latest_news():
    url = "https://cointelegraph.com/rss"
    feed = feedparser.parse(url)

    news = []

    if not feed.entries:
        return news

    for item in feed.entries:
        title = item.title

        if any(keyword.lower() in title.lower() for keyword in IMPORTANT_KEYWORDS):
            news.append({
                "title": title,
                "link": item.link
            })

        if len(news) >= 5:
            break

    return news