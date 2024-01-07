import config
from telegram.ext import *


print('Bot started...')


def start_command(update, context):
    update.message.reply_text('START COMMAND')


def help_command(update, context):
    update.message.reply_text('HELP COMMAND')


def oc_analytics_command(update, context):
    update.message.reply_text('btc')


def handle_message(update, context):
    text = str(update.message.text).lower()
    update.message.reply_text(text)


def error(update, context):
    print('ERROR')


def main():
    updater = Updater(config.TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("btc", oc_analytics_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
