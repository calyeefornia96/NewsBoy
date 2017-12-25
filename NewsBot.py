from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
import re

TOKEN = "502882933:AAGtNf5KxO1QKFc7AE2UDLEUSmip5NNDAik"

stringHowItWorks = '''
This is a news bot:
Receive instant updates from news sites.
'''

def start(bot, update):
	update.message.reply_text("Hi!")
	update.message.reply_text(stringHowItWorks)

def help(bot, update):
	update.message.reply_text(stringHowItWorks)




def main():
	updater = Updater(TOKEN)
	updater.start_webhook(listen='0.0.0.0',
                      port=8443,
                      url_path= TOKEN,
                      key='private.key',
                      cert='cert.pem',
                      webhook_url='https://0.0.0.0:8443/' + TOKEN)

	

	updater.idle()





if __name__ == '__main__':
	main()