import requests

from function import read_dekan_table
from keys import TOKEN, channel_name, bot_url, caption_1, photo_1

inline_keyboard = []
dekans = read_dekan_table()
for dekan in dekans:
    btn = {
        'text': f"{dekan[1]} - {dekan[2]}",
        'url': bot_url,
    }
    inline_keyboard.append([btn])
# print(inline_keyboard)


def message_sendler(channel, image, text, btn):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

    # Define the payload
    payload = {
        "chat_id": channel,
        "photo": image,
        "caption": text,
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": btn
        }
    }

    # Send the request
    response = requests.post(url, json=payload)
    return response.json()['result']['message_id']


# print(message_sendler(channel_name, photo_1, caption_1, inline_keyboard))
