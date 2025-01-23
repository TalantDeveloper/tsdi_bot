from telebot import types, TeleBot
from keys import TOKEN, admin_id, chat_id, photo_1, photo_2, caption_2, bot_url, channel_name, caption_1, channel_name1
from button import create_zamDekan_btn, create_result_btn, create_dekan_btn, dekan_inline, zamDekan_inline
from function import add_dekan_voice, add_zamDekan_voice, read_dekan_table, result_all, \
    create_voter, update_voter_table, read_zamDekan_table, read_voter_table, insert_message, delete_message
from checkers import first_checker, checker_voter, cheklov_votes, send_admin_message
from power import message_sendler

token = TOKEN
bot = TeleBot(token)


@bot.message_handler(commands=['start'])
def start(msg: types.Message):
    if cheklov_votes(bot) and checker_voter(bot, msg):
        first_checker(bot, msg)
    else:
        bot.send_message(
            msg.from_user.id,
            text=f"Natijani ko'rish 👀",
            reply_markup=create_result_btn())


@bot.message_handler(commands=['allResult'])
def getAllResult(msg: types.Message):
    if msg.from_user.id == admin_id:
        voters = read_voter_table()
        for vote in voters:
            bot.send_message(admin_id, text=f"{vote[0]}-{vote[1]} @{vote[2]} <=>{vote[3]} <=>{vote[4]}")


@bot.message_handler(commands=['sendMessage'])
def send_message(msg: types.Message):
    if msg.from_user.id == admin_id:
        delete_message()
        inline_keyboard = dekan_inline()
        message_id_1 = message_sendler(channel_name, photo_1, caption_1, inline_keyboard)
        insert_message(channel_name, message_id_1)
        message_id_2 = message_sendler(channel_name1, photo_1, caption_1, inline_keyboard)
        insert_message(channel_name1, message_id_2)
        inline_keyboard = zamDekan_inline()

        message_id_3 = message_sendler(channel_name, photo_2, caption_2, inline_keyboard)
        insert_message(channel_name, message_id_3)
        message_id_4 = message_sendler(channel_name1, photo_2, caption_2, inline_keyboard)
        insert_message(channel_name1, message_id_4)


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
        bot.send_photo(msg.from_user.id, photo=photo_2,
                       caption=caption_2,
                       parse_mode='HTML',
                       reply_markup=create_zamDekan_btn(),
                       )
        create_voter(msg, dekan_id)

    elif msg.data[:8] == 'zamDekan':
        zamDekan_id = int(msg.data[8:])
        add_zamDekan_voice(zamDekan_id)
        zamDekan = read_zamDekan_table()[zamDekan_id - 1]
        bot.send_message(msg.from_user.id, text=f"Siz {zamDekan[1]} ga ovoz berdingiz!")
        update_voter_table(msg.from_user.id, zamDekan_id)

        result_all(bot, msg)

        vote = send_admin_message(msg)

        # We need one function. It's update channels message results.

        bot.send_message(admin_id, text=f"{vote[0]}-{vote[1]} @{vote[2]} <=>{vote[3]} <=>{vote[4]}")
    elif msg.data == 'result':
        result_all(bot, msg)


bot.polling()
