import requests
from telebot import types

from function import read_dekan_table, read_zamDekan_table
from keys import bot_url, TOKEN, caption_1, channel_name

chat_id = "-1002481531999"


def update_result(bot, msg):
    result_dekan = types.InlineKeyboardMarkup(row_width=1)
    dekans = read_dekan_table()
    for dekan in dekans:
        result_dekan.add(
            types.InlineKeyboardButton(text=f"{dekan[2]} - {dekan[1]}", url=bot_url)
        )

    bot.send_photo(msg.from_user.id, photo="https://tsdi.uz/assets/images/slider/stom.jpg",
                   caption="Fakultet dekanlari",
                   reply_markup=result_dekan)

    result_zamDekan = types.InlineKeyboardMarkup(row_width=1)
    zamDekans = read_zamDekan_table()
    for zamDekan in zamDekans:
        result_zamDekan.add(
            types.InlineKeyboardButton(text=f"{zamDekan[2]} - {zamDekan[1]}", url=bot_url)
        )

    bot.send_photo(msg.from_user.id, photo="https://tsdi.uz/assets/images/slider/stom.jpg",
                   caption="Yoshlar bilan ishlash bo'yicha dekan muovinlari",
                   reply_markup=result_zamDekan)


reply_markup = {
    "inline_keyboard": [
        [
            {"text": "Button 1", "url": "https://t.me/thetsdivoicebot"},
        ],
        [
            {"text": "Button 2", "url": "https://t.me/thetsdivoicebot"}
        ]
    ]
}


def check_update():
    url = f"https://api.telegram.org/bot{TOKEN}/editMessageMedia"
    url1 = f"https://api.telegram.org/bot{TOKEN}/editMessageCaption"
    inline_keyboard = []
    dekans = read_dekan_table()
    for dekan in dekans:
        btn = {
            'text': f"{dekan[2]} - {dekan[1]}",
            'url': bot_url,
        }
        inline_keyboard.append([btn])

    url = f"https://api.telegram.org/bot{TOKEN}/editMessageCaption"

    # Define the new caption and inline keyboard
    payload = {
        "chat_id": channel_name,
        "message_id": 67,
        "caption": caption_1,
        "parse_mode": "HTML",
        "reply_markup": {'inline_keyboard': inline_keyboard}

    }

    response = requests.post(url, json=payload)
    print(response.json())


# check_update()
