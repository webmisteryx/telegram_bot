from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

#Logging the bot's actions
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

# Main function for launch the bot
def main():
    #Without a proxy does not work in Russia
    mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY)

    logging.info('The Bot has started')

    dp = mybot.dispatcher

    # Catch bot's command and send answer    
    dp.add_handler(CommandHandler('start', greet_user))
    # Catch bot's message and write it to log
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

    logging.info('The Bot has finished work')

# Bot launch
main()
