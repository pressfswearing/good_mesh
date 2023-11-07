import telebot
from background import keep_alive

bot = telebot.TeleBot('token')

@bot.message_handler(commands=['start'])
def start(message):
	file = open('waiters_list.txt', 'a+', encoding='utf-8')
	line = file.read()
	array = line.split('\n')
	file.write('\n' + str(message.from_user.id) + str(len(array)))
	bot.send_message(message.chat.id, 'Привет! Сейчас проводятся тех.работы по запуску бота до 11:00. Ждём тебя!')

keep_alive()
bot.polling(none_stop = True, interval = 0)