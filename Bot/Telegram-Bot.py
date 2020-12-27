from telegram.ext import Updater
updater = Updater(token='...............................', use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)


def salamFunc(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="!سلام!")

from telegram.ext import CommandHandler
salam_handler = CommandHandler('salam', salamFunc)
dispatcher.add_handler(salam_handler)

updater.start_polling()
