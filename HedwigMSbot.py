import telegram
from telegram.ext import *

mi_bot = telegram.Bot(token='682980920:AAGybjIygCGh3O6qXVdNCYgAazuJ8pBR6cc')
mi_bot_updater = Updater(mi_bot.token)
	
def listener(bot, update):
	id=update.message.chat_id
	mensaje=update.message.text
	hora=update.message.date
	print('ID: '+ str(id) + (' Mensaje: ') + mensaje)
	print('Hora del mensaje: ' + hora)
	if 'hora' in mensaje:
		bot.sendMessage(chat_id=id, text= 'Son las ')

def start(bot, update, pass_chat_data=True):
	id=update.message.chat_id
	mensaje=update.message.text
	if id==4432484:
		bot.sendMessage(chat_id=id, text='Bienvenido, amo ⚡️')
	else:
		bot.sendMessage(chat_id=id, text='Bienvenido! 😊')

def help(bot, update):
	id=update.message.chat_id
	mensaje=update.message.text
	bot.sendMessage(chat_id=id, text='Los comandos que puedes utilizar conmigo son: /start /help')



start_handler = CommandHandler('start',start)
listener_handler = MessageHandler(Filters.text, listener)
help_handler= CommandHandler('help',help)

dispatcher = mi_bot_updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(listener_handler)
dispatcher.add_handler(help_handler)

mi_bot_updater.start_polling()
mi_bot_updater.idle()

while True:
	pass