IMPORTANT_KEYWORDS = [
    "ETF",
    "BlackRock",
    "Fidelity",
    "SEC",
    "Binance",
    "Coinbase",
    "Ethereum",
    "Solana",
    "Bitcoin",
    "Hack",
    "Exploit",
    "Rug",
    "Rugpull",
    "Whale",
    "Liquidation",
    "Bridge",
    "Stablecoin",
    "USDT",
    "USDC",
    "Fed",
    "CPI",
]
def is_important(title):

    title = title.lower()

    for word in IMPORTANT_KEYWORDS:
        if word.lower() in title:
            return True

    return False