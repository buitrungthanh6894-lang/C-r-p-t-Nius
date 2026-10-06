from openai import OpenAI
from config import OPENAI_API_KEY


client = OpenAI(
    api_key=OPENAI_API_KEY
)


def analyze_news(title):

    prompt = f"""
Bạn là chuyên gia crypto.

Phân tích tin:

{title}

Trả lời:

1. Tin này ảnh hưởng BTC thế nào?
2. Bullish hay Bearish?
3. Mức độ ảnh hưởng 1-10
"""


    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )


    return response.choices[0].message.content