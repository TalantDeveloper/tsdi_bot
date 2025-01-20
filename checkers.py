import sqlite3

from button import check_btn, create_dekan_btn
from function import read_dekan_table, read_voter_table, update_voter_table, read_zamDekan_table
from keys import channel, channel1, admin_id, photo_1, caption_1


def first_checker(bot, msg):
    check_user = bot.get_chat_member(channel, user_id=msg.from_user.id).status
    check_user1 = bot.get_chat_member(channel1, user_id=msg.from_user.id).status
    if check_user == 'member' or check_user == 'creator' or check_user == 'admin' or check_user == 'administrator':
        if check_user1 == 'member' or check_user1 == 'creator' or check_user1 == 'admin' or check_user1 == 'administrator':
            bot.send_photo(msg.from_user.id,
                           photo=photo_1,
                           caption=caption_1,
                           parse_mode='HTML',
                           reply_markup=create_dekan_btn())
        else:
            bot.send_message(msg.from_user.id,
                             text="Kanalimizga obuna bo'ling",
                             reply_markup=check_btn)
    else:
        bot.send_message(msg.from_user.id,
                         text="Kanalimizga obuna bo'ling",
                         reply_markup=check_btn)


def checker_voter(bot, msg):
    user_id = msg.from_user.id
    voters = read_voter_table()
    for voter in voters:
        if voter[1] == user_id:
            bot.send_message(user_id, text="Siz ovoz berib bo'lgansiz")
            return False
    return True


def cheklov_votes(bot):
    voters = read_voter_table()
    if len(voters) >= 10000:
        bot.send_message(admin_id, text="Ovoz berish soni haddan tashqari oshib ketdi.\n"
                                         "Bu haqida qayg'urish kerak")
        return False
    dekans = read_dekan_table()
    for dekan in dekans:
        if dekan[2] >= 5000:
            bot.send_message(admin_id, text="Ovoz berish soni haddan tashqari oshib ketdi.\n"
                                             "Bu haqida qayg'urish kerak")
            return False
    zamDekans = read_zamDekan_table()
    for zamDekan in zamDekans:
        if zamDekan[2] >= 5000:
            bot.send_message(admin_id, text="Ovoz berish soni haddan tashqari oshib ketdi.\n"
                                             "Bu haqida qayg'urish kerak")
            return False
    return True


def send_admin_message(msg):
    user_id = msg.from_user.id
    voters = read_voter_table()
    for voter in voters:
        if voter[1] == user_id:
            return voter
    return user_id
