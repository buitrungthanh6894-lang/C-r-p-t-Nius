import feedparser

RSS_FEEDS = [
    "https://cointelegraph.com/rss",
    "https://cryptopotato.com/feed/",
    "https://decrypt.co/feed"
]

KEYWORDS = [
    "hack",
    "hacked",
    "exploit",
    "rug",
    "rugpull",
    "rug pull",
    "scam",
    "stolen",
    "drain",
    "drained",
    "breach",
    "phishing",
    "attack"
]

def get_rugpull():

    message = "🚨 SECURITY ALERTS\n\n"

    found = 0
    seen = set()

    for rss in RSS_FEEDS:

        try:
            feed = feedparser.parse(rss)

            for item in feed.entries:

                title = item.title

                if title in seen:
                    continue

                if any(k in title.lower() for k in KEYWORDS):

                    seen.add(title)

                    message += f"📰 {title}\n"
                    message += f"🔗 {item.link}\n\n"

                    found += 1

                    if found >= 5:
                        return message

        except Exception:
            continue

    if found == 0:
        return "✅ Không phát hiện vụ Hack/Rugpull nổi bật."

    return message