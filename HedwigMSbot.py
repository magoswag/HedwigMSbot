import telegram
from telegram.ext import *

mi_bot = telegram.Bot(token='682980920:AAGybjIygCGh3O6qXVdNCYgAazuJ8pBR6cc')
mi_bot_updater = Updater(mi_bot.token)

def listener(bot, update):
	id=update.message.chat_id
	mensaje=update.message.text
	hora=str(update.message.date)
	print('ID: '+ str(id) + (' Mensaje: ') + mensaje)
	print('ID: '+str(id)+ ' Hora del mensaje: '+ hora)
	elif 'hora' in message:
		bot.sendMessage(chat_id=id, text='Estamos a '+ hora)

def hora(bot, update):
	id=update.message.chat_id
	hora=str(update.message.date)
	bot.sendMessage(chat_id=id, text='Estamos a '+ hora)

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
	bot.sendMessage(chat_id=id, text='Los comandos que puedes utilizar conmigo son: /start /help /hora')



start_handler = CommandHandler('start',start)
listener_handler = MessageHandler(Filters.text, listener)
help_handler= CommandHandler('help',help)
hora_handler= CommandHandler('hora', hora)

dispatcher = mi_bot_updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(listener_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(hora_handler)

mi_bot_updater.start_polling()
mi_bot_updater.idle()

while True:
	pass