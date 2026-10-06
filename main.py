import time
from rss import latest_news
from telegram_send import send_message
from database import is_sent, add_sent


def run():

    print("🚀 Crypto News Bot Running...")


    while True:

        try:

            news = latest_news()


            for item in news:

                link = item["link"]


                if is_sent(link):
                    continue


                message = f"""
📰 CRYPTO NEWS

{item['title']}

🔗 {link}
"""


                send_message(message)

                add_sent(link)

                print("Sent:", item["title"])



            print("⏳ Chờ 15 phút...")


            time.sleep(900)


        except Exception as e:

            print("Error:", e)

            time.sleep(60)



run()