import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Ergashov Botirjon", callback_data="0"),
        ],
        [InlineKeyboardButton("Qarshiyev Otabek", callback_data="1")],
        [InlineKeyboardButton("Yusupov Nurbek", callback_data="2")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo('./14.jpg')
    await update.message.reply_text(
        "Toshkent Davlat Stomatologiya Instituti Raqamli Ta'lim Texnologiyalar markazi eng yaxshi hodimi Kim",
        reply_markup=reply_markup)


employees = ["Ergashov Botirjon", "Qarshiyev Otabek", "Yusupov Nurbek"]


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    print(employees[int(query.data)])
    print(query.data)

    await query.edit_message_text(text=f"Siz tanlagan javob: {employees[int(query.data)]}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("7188533935:AAF1furVY_yP0ge8SAB2kAoVzZLFWvoE01o").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
