import requests

def get_fear():

    try:

        url = "https://api.alternative.me/fng/?limit=1"

        data = requests.get(url, timeout=10).json()["data"][0]

        value = data["value"]
        status = data["value_classification"]

        return (
            "😨 FEAR & GREED INDEX\n\n"
            f"📊 Index: {value}/100\n"
            f"🔥 Sentiment: {status}"
        )

    except Exception as e:

        return f"❌ {e}"