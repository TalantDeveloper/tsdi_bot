from telebot import types, TeleBot
from keys import TOKEN, admin_id
from button import create_zamDekan_btn, create_result_btn
from function import add_dekan_voice, add_zamDekan_voice, read_dekan_table, result_all, \
    create_voter, update_voter_table, read_zamDekan_table, read_voter_table
from checkers import first_checker, checker_voter, cheklov_votes, send_admin_message

token = TOKEN
bot = TeleBot(token)


@bot.message_handler(commands=['start'])
def start(msg: types.Message):
    if cheklov_votes(bot) and checker_voter(bot, msg):
        first_checker(bot, msg)
    else:
        bot.send_message(
            msg.from_user.id,
            text=f"Natijani tekshirishingiz mumkin!!!",
            reply_markup=create_result_btn())


@bot.message_handler(commands=['allResult'])
def getAllResult(msg: types.Message):
    if msg.from_user.id == 556841744:
        voters = read_voter_table()
        for vote in voters:
            bot.send_message(admin_id, text=f"{vote[0]}-{vote[1]} @{vote[2]} <=>{vote[3]} <=>{vote[4]}")


@bot.callback_query_handler(func=lambda x: x.data)
def query(msg: types.CallbackQuery):
    bot.delete_message(msg.from_user.id, msg.message.id)
    if msg.data == "checksub":
        first_checker(bot, msg)
    elif msg.data[:5] == 'dekan':
        dekan_id = int(msg.data[5:])
        add_dekan_voice(dekan_id)
        dekan = read_dekan_table()[dekan_id - 1]
        bot.send_message(msg.from_user.id, text=f"Siz {dekan[1]} ga ovoz berdingiz")
        bot.send_message(msg.from_user.id,
                         text="Toshkent Davlat Stomatologiya Institutida "
                              "eng yaxshi Yoshlar bilan ishlash bo'yicha dekam muoviniga"
                              "ovoz bering.",
                         reply_markup=create_zamDekan_btn())
        create_voter(msg, dekan_id)

    elif msg.data[:8] == 'zamDekan':
        zamDekan_id = int(msg.data[8:])
        add_zamDekan_voice(zamDekan_id)
        zamDekan = read_zamDekan_table()[zamDekan_id - 1]
        bot.send_message(msg.from_user.id, text=f"Siz {zamDekan[1]} ga ovoz berdingiz!")
        bot.send_message(msg.from_user.id, text=result_all())
        update_voter_table(msg.from_user.id, zamDekan_id)
        vote = send_admin_message(msg)
        bot.send_message(admin_id, text=f"{vote[0]}-{vote[1]} @{vote[2]} <=>{vote[3]} <=>{vote[4]}")
    elif msg.data == 'result':
        bot.send_message(msg.from_user.id, text=result_all())


bot.polling()
