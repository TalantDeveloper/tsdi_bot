# from telebot import types, TeleBot
#
# from button import create_result_btn
# from checkers import first_checker, cheklov_votes, checker_voter
# from keys import TOKEN
#
# bot = TeleBot(TOKEN)
#
#
# @bot.message_handler(commands=['start'])
# def start(msg: types.Message):
#     if cheklov_votes(bot) and checker_voter(bot, msg):
#         first_checker(bot, msg)
#     else:
#         bot.send_message(
#             msg.from_user.id,
#             text=f"Natijani ko'rish 👀",
#             reply_markup=create_result_btn())
#
#
#
# bot.polling()
