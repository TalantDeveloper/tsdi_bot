import requests

from function import read_dekan_table
from keys import TOKEN, channel_name, bot_url, caption_1, photo_1


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


def update_message(channel,message, image, text, btn):
    url = f"https://api.telegram.org/bot{TOKEN}/editMessageCaption"
    payload = {
        "chat_id": channel,
        "message_id": message,
        'photo': image,
        "caption": text,
        "parse_mode": "HTML",
        "reply_markup": {'inline_keyboard': btn}
    }
    response = requests.post(url, json=payload)
    print(response.json())
