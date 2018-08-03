import telegram
from telegram.ext import *

mi_bot = telegram.Bot(token='682980920:AAGybjIygCGh3O6qXVdNCYgAazuJ8pBR6cc')
mi_bot_updater = Updater(mi_bot.token)

def start(bot, update, pass_chat_data=True): #Comando de bienvenida
	id=update.message.chat_id
	mensaje=update.message.text
	if id==4432484:
		bot.sendMessage(chat_id=id, text='Bienvenido, amo ⚡️')
	else:
		bot.sendMessage(chat_id=id, text='Bienvenido! 😊')

def help(bot, update): #Comando para saber los comandos que puede ejecutar el bot
	id=update.message.chat_id
	mensaje=update.message.text
	bot.sendMessage(chat_id=id, text='Los comandos que puedes utilizar conmigo son: /start /help /fecha')

def listener(bot, update): #Te dice el id, mensaje y la fecha a la que se ha enviado el mensaje
	id=update.message.chat_id
	user=update.message.from_user
	mensaje=update.message.text
	date=str(update.message.date)
	print('ID: '+ str(id) + ' Mensaje: ' + mensaje)
	print('ID: '+ str(id) + ' Hora del mensaje: '+ date)
	if 'Hola' in mensaje or 'hola' in mensaje:
		bot.sendMessage(chat_id=id, text='Hola '+ user.first_name+'!')
	if 'fecha' in mensaje or 'Fecha' in mensaje: #Para que te diga a que fecha estamos sin usar comando
		bot.sendMessage(chat_id=id, text='Estamos a '+ date)


def fecha(bot, update): #Comando para saber la fecha en la que estás
	id=update.message.chat_id
	fecha=str(update.message.date)
	bot.sendMessage(chat_id=id, text='Estamos a '+ fecha)

start_handler = CommandHandler('start',start)
listener_handler = MessageHandler(Filters.text, listener)
help_handler= CommandHandler('help', help)
fecha_handler= CommandHandler('fecha', fecha)

dispatcher = mi_bot_updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(listener_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(fecha_handler)


mi_bot_updater.start_polling()
mi_bot_updater.idle()

while True:
	pass
