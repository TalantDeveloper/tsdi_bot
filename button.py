from telebot import types
from function import read_dekan_table, read_zamDekan_table
from keys import channel_url, channel_url1, bot_url

check_btn = types.InlineKeyboardMarkup(row_width=1)

check_btn.add(
    types.InlineKeyboardButton(text="1 - kanalimiz", url=channel_url),
    types.InlineKeyboardButton(text="2 - kanalimiz", url=channel_url1),
    types.InlineKeyboardButton(text="✅ Tekshirish", callback_data="checksub"),
)


def create_dekan_btn():
    check_dekan = types.InlineKeyboardMarkup(row_width=1)
    dekans = read_dekan_table()
    for dekan in dekans:
        check_dekan.add(
            types.InlineKeyboardButton(text=f"{dekan[2]} - {dekan[1]}", callback_data=f"dekan{dekan[0]}")
        )
    return check_dekan


def create_zamDekan_btn():
    check_zamDekan = types.InlineKeyboardMarkup(row_width=1)
    zamDekans = read_zamDekan_table()
    for zamDekan in zamDekans:
        check_zamDekan.add(
            types.InlineKeyboardButton(text=f"{zamDekan[2]} - {zamDekan[1]}", callback_data=f"zamDekan{zamDekan[0]}")
        )
    return check_zamDekan


def create_result_btn():
    result_btn = types.InlineKeyboardMarkup(row_width=1)
    result_btn.add(types.InlineKeyboardButton(text="Natijani tekshirish", callback_data='result'))
    return result_btn


def dekan_inline():
    inline_keyboard = []
    dekans = read_dekan_table()
    for dekan in dekans:
        btn = {
            'text': f"{dekan[2]} - {dekan[1]}",
            'url': bot_url,
        }
        inline_keyboard.append([btn])
    return inline_keyboard


def zamDekan_inline():
    inline_keyboard = []
    zamDekans = read_zamDekan_table()
    for zamDekan in zamDekans:
        btn = {
            'text': f"{zamDekan[2]} - {zamDekan[1]}",
            'url': bot_url,
        }
        inline_keyboard.append([btn])
    return inline_keyboard

