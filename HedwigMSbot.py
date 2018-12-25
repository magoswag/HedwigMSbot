import telegram
from telegram.ext import *


mi_bot = telegram.Bot(token='682980920:AAGybjIygCGh3O6qXVdNCYgAazuJ8pBR6cc')
mi_bot_updater = Updater(mi_bot.token)




def start(bot, update, pass_chat_data=True):  # Comando de bienvenida
	id = update.message.chat_id
	mensaje = update.message.text
	if id == 4432484:
		bot.sendMessage(chat_id=id, text=
		'Bienvenido, amo ⚡️\n¿Qué haremos hoy?')
	else:
		bot.sendMessage(chat_id=id, text=
		'Bienvenido! 😊\nYo seré tu asistente personal. ¿Qué puedo hacer por ti?')

# Comando para saber los comandos que puede ejecutar el bot
def help(bot, update):
	id = update.message.chat_id
	mensaje = update.message.text
	bot.sendMessage(chat_id=id,
	text='Los comandos que puedes utilizar conmigo son: /start /help /fecha')

# Te dice el id, mensaje y la fecha a la que se ha enviado el mensaje
def listener(bot, update):
	id = update.message.chat_id
	user = update.message.from_user
	mensaje = update.message.text
	#date1 = telegram.Message.date
	date = str(update.message.date)
	print('ID: ' + str(id) + ' Mensaje: ' + mensaje)
	print('ID: ' + str(id) + ' Hora del mensaje: ' + date)
	if ('Hola' in mensaje or 'hola' in mensaje) and len(mensaje) < 20:
		bot.sendMessage(chat_id=id, text='Hola '+ user.first_name + '!')
	if ('fecha' in mensaje or 'Fecha' in mensaje or 'dia' in mensaje or 'Dia' in mensaje)
	and len(mensaje) <50:  # Para que te diga a que fecha estamos sin usar comando
		bot.sendMessage(chat_id=id, text='Estamos a ' + date)

# Comando para saber la fecha en la que estás
def fecha(bot, update):
	id = update.message.chat_id
	fecha = str(update.message.date)
	bot.sendMessage(chat_id=id, text='Estamos a ' + fecha)

def addC(filter, handler, **args):
        dp.add_handler(CommandHandler(filter, handler, **args))

def addM(filter, handler, **args):
        dp.add_handler(MessageHandler(filter, handler, **args))

dp = mi_bot_updater.dispatcher

addC('start', start)
addM(Filters.text, listener)
addC('help', help)
addC('fecha', fecha)


mi_bot_updater.start_polling()
mi_bot_updater.idle()

while True:
	pass