from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Execute command /start'
    logging.info('Command /start complited')
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    user_name = update.message.chat.username
    logging.info("User: %s, Message: %s", user_name, user_text)

def main():
    mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY)

    logging.info('The Bot has started')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

    logging.info('The Bot has finished work')
main()
