import requests

def get_meme():

    url = "https://api.coingecko.com/api/v3/search/trending"

    try:
        data = requests.get(url, timeout=10).json()

        message = "🐸 TRENDING MEME COINS\n\n"

        count = 1

        for coin in data["coins"]:

            item = coin["item"]

            symbol = item["symbol"].upper()

            # Chỉ lấy các memecoin phổ biến
            if symbol in [
                "DOGE",
                "SHIB",
                "PEPE",
                "BONK",
                "FLOKI",
                "WIF",
                "BRETT",
                "MOG",
                "PENGU"
            ]:

                message += f"{count}. {item['name']} ({symbol})\n"
                count += 1

            if count > 5:
                break

        if count == 1:
            return "📭 Hiện chưa có memecoin nổi bật."

        return message

    except Exception:
        return "❌ Không lấy được dữ liệu Memecoin."