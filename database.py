import json
import os


FILE = "sent_news.json"


def load_sent():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def save_sent(sent):

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(sent, f, ensure_ascii=False, indent=2)



def is_sent(link):

    sent = load_sent()

    return link in sent



def add_sent(link):

    sent = load_sent()

    sent.append(link)

    # giữ tối đa 200 tin gần nhất
    sent = sent[-200:]

    save_sent(sent)