import requests

MIN_MC = 50000          # Market Cap tối thiểu
MAX_MC = 5000000        # Market Cap tối đa
MIN_LIQUIDITY = 30000   # Thanh khoản tối thiểu
MIN_VOLUME = 50000      # Volume 24h tối thiểu
MIN_CHANGE = 30         # Tăng ít nhất 30%

CHAINS = [
    "solana",
    "base",
    "bsc",
    "ethereum"
]


def get_new_memes():

    url = "https://api.dexscreener.com/latest/dex/search?q=meme"

    try:

        data = requests.get(url, timeout=10).json()

        pairs = data.get("pairs", [])

        message = "🚀 HOT MEME ALERTS\n\n"

        found = 0

        for pair in pairs:

            chain = pair.get("chainId", "")

            if chain not in CHAINS:
                continue

            mc = pair.get("marketCap") or 0
            liq = pair.get("liquidity", {}).get("usd", 0)
            vol = pair.get("volume", {}).get("h24", 0)
            change = pair.get("priceChange", {}).get("h24", 0)

            if mc < MIN_MC or mc > MAX_MC:
                continue

            if liq < MIN_LIQUIDITY:
                continue

            if vol < MIN_VOLUME:
                continue

            if change < MIN_CHANGE:
                continue

            token = pair["baseToken"]["symbol"]
            name = pair["baseToken"]["name"]

            message += (
                f"🐸 {name} ({token})\n"
                f"🌐 {chain.upper()}\n"
                f"💰 MC: ${mc:,.0f}\n"
                f"💧 LP: ${liq:,.0f}\n"
                f"📈 24H: {change:.2f}%\n"
                f"📊 Volume: ${vol:,.0f}\n"
                f"🔗 {pair['url']}\n\n"
            )

            found += 1

            if found == 5:
                break

        if found == 0:
            return "📭 Không tìm thấy memecoin đạt điều kiện."

        return message

    except Exception as e:
        return f"❌ {e}"