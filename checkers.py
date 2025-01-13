from button import check_btn, create_dekan_btn
from function import read_dekan_table, read_voter_table, update_voter_table, read_zamDekan_table
from keys import channel


def first_checker(bot, msg):
    check_user = bot.get_chat_member(channel, user_id=msg.from_user.id).status
    if check_user == 'member' or check_user == 'creator' or check_user == 'admin':
        bot.send_message(msg.from_user.id,
                         text="Assalomu alaykun!\n"
                              "Toshkent Davlat Stomatologiya Institutida "
                              "eng yaxshi Dekanga ovoz berishingiz mumkin.",
                         reply_markup=create_dekan_btn())
    else:
        bot.send_message(msg.from_user.id,
                         text="Kanalimizga obuna bo'ling",
                         reply_markup=check_btn)


def checker_voter(bot, msg):
    user_id = msg.from_user.id
    voters = read_voter_table()
    for voter in voters:
        if voter[1] == user_id:
            bot.send_message(user_id, text="Siz bu tanlovda qatnashib bo'lgansiz :)")
            return False
    return True


def cheklov_votes(bot):
    dekans = read_dekan_table()
    if len(dekans) >= 10000:
        bot.send_message(556841744, text="Ovoz berish soni haddan tashqari oshib ketdi.\n"
                                         "Bu haqida qayg'urish kerak")
        return False
    for dekan in dekans:
        if dekan[2] >= 5000:
            bot.send_message(556841744, text="Ovoz berish soni haddan tashqari oshib ketdi.\n"
                                             "Bu haqida qayg'urish kerak")
            return False
    zamDekans = read_zamDekan_table()
    if len(zamDekans) >= 10000:
        bot.send_message(556841744, text="Ovoz berish soni haddan tashqari oshib ketdi.\n"
                                         "Bu haqida qayg'urish kerak")
        return False
    for zamDekan in zamDekans:
        if zamDekan[2] >= 5000:
            bot.send_message(556841744, text="Ovoz berish soni haddan tashqari oshib ketdi.\n"
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

