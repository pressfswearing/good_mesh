import telebot
from dnevniklib.homeworks import Homeworks
from dnevniklib.student import Student
from dnevniklib.errors import token as token_error
from background import keep_alive

bot = telebot.TeleBot('token')

@bot.message_handler(commands=['start'])
def start(message):
  general_file = open('general_datas.txt', 'r', encoding='utf-8')
  line = general_file.read()
  array = line.split("\n")
  for i in array:
    if message.from_user.username in i:
      bot.send_message(message.chat.id, 'Готово! Теперь можешь запускать команды!')
      break
    else:
      bot.send_message(message.chat.id, 'Привет! Отправь /login, чтобы получить доступ к боту!')

@bot.message_handler(commands=['login'])
def login(message):
  token = bot.send_message(message.chat.id, 'Отправь мне токен, полученный по этой инструкции: https://telegra.ph/Kak-poluchit-token-dlya-dostupa-k-botu-MEHSH-20-11-02')
  bot.register_next_step_handler(token, login1)
def login1(message):
  general_file = open('general_datas.txt', 'a+', encoding='utf-8')
  general_file.write('\n' + message.from_user.username + '@' + str(message.text) + '@' + str(message.from_user.id))
  bot.send_message(message.chat.id, 'Готово, токен получен!')
  bot.send_message(message.chat.id, 'Теперь можешь вызвать одну из команд:\n/schedule - расписание на определённый день.\n/homeworks - домашки на определённый день.\n/marks - оценки на определённый день.\n/trimester_marks - средние баллы за определённый триместр.')

@bot.message_handler(commands=['homeworks'])
def homeworks(message):
  date = bot.send_message(message.chat.id, 'Отправь дату, на которую хочешь увидеть домашки, в таком формате:\n2023-10-25')
  bot.register_next_step_handler(date, homeworks1)
def homeworks1(message):
  date = message.text
  general_file = open('general_datas.txt', 'r', encoding='utf-8')
  line = general_file.read()
  array = line.split("\n")
  for i in array:
    if message.from_user.username in i:
      profile_split = i.split("@")
      username = profile_split[0]
      token = profile_split[1]
      try:
        student = Student(token=token)
        homework = Homeworks(Student(token=token))
        homeworks_general = []
        homeworks = homework.get_homework_by_date(date)
        for i in range(len(homeworks)):
          homeworks_general.append(homeworks[i])
        for i in homeworks_general:
          bot.send_message(message.chat.id, i)
      except token_error.DnevnikTokenError:
        bot.send_message(message.chat.id, 'Твой токен для бота сломан, напиши разработчику - @yandexerr - он тебе поможет.')

@bot.message_handler(commands=['schedule'])
def schedule(message):
  date = bot.send_message(message.chat.id, 'Отправь дату, на которую хочешь увидеть расписание, в таком формате:\n2023-10-25')
  bot.register_next_step_handler(date, schedule1)
def schedule1(message):
  date = message.text
  general_file = open('general_datas.txt', 'r', encoding='utf-8')
  line = general_file.read()
  array = line.split("\n")
  for i in array:
    if message.from_user.username in i:
      profile_split = i.split("@")
      username = profile_split[0]
      token = profile_split[1]
      try:
        student = Student(token=token)
        homework = Homeworks(Student(token=token))
        schedule_general = []
        schedule = homework.get_schedule(date)
        for i in range(len(schedule)):
          schedule_general.append(schedule[i])
        for i in schedule_general:
          bot.send_message(message.chat.id, i)
      except token_error.DnevnikTokenError:
        bot.send_message(message.chat.id, 'Твой токен для бота сломан, напиши разработчику - @yandexerr - он тебе поможет.')

@bot.message_handler(commands=['marks'])
def marks(message):
  date = bot.send_message(message.chat.id, 'Отправь дату, на которую хочешь увидеть оценки, в таком формате:\n2023-10-25')
  bot.register_next_step_handler(date, marks1)
def marks1(message):
  date = message.text
  general_file = open('general_datas.txt', 'r', encoding='utf-8')
  line = general_file.read()
  array = line.split("\n")
  for i in array:
    if message.from_user.username in i:
      profile_split = i.split("@")
      username = profile_split[0]
      token = profile_split[1]
      try:
        student = Student(token=token)
        homework = Homeworks(Student(token=token))
        marks_general = []
        marks = homework.get_marks(date)
        for i in range(len(marks)):
          marks_general.append(marks[i])
        for i in marks_general:
          bot.send_message(message.chat.id, i)
      except token_error.DnevnikTokenError:
        bot.send_message(message.chat.id, 'Твой токен для бота сломан, напиши разработчику - @yandexerr - он тебе поможет.')

@bot.message_handler(commands=['trimester_marks'])
def trimester_marks(message):
  trimester = bot.send_message(message.chat.id, 'Введи номер триместра, на который хочешь посмотерть средние баллы.\n1 - 1 триместр\n2 - 2 триместр\n3 - 3 триместр.')
  bot.register_next_step_handler(trimester, trimester_marks1)
def trimester_marks1(message):
  trimester = str(int(message.text )- 1)
  general_file = open('general_datas.txt', 'r', encoding='utf-8')
  line = general_file.read()
  array = line.split("\n")
  for i in array:
    if message.from_user.username in i:
      profile_split = i.split("@")
      username = profile_split[0]
      token = profile_split[1]
      try:
        student = Student(token=token)
        homework = Homeworks(Student(token=token))
        trimes_ter_marks = homework.get_trimester_marks(trimester)
        for i in range(len(trimes_ter_marks)):
            bot.send_message(message.chat.id, str(trimes_ter_marks[i]['name']) + ': ' + str(trimes_ter_marks[i]['mark']))
      except token_error.DnevnikTokenError:
        bot.send_message(message.chat.id, 'Твой токен для бота сломан, напиши разработчику - @yandexerr - он тебе поможет.')

@bot.message_handler(commands=['admin_notification'])
def admin_notification(message):
  if message.from_user.username == 'yandexerr':
    notify = bot.send_message(message.chat.id, 'введи текст уведомления, которое надо разослать всем')
    bot.register_next_step_handler(notify, admin_notification1)
  else:
    bot.send_message(message.chat.id, 'Ты не являешься админом этого бота.')
def admin_notification1(message):
  notify = message.text
  general_file = open('general_datas.txt', 'r', encoding='utf-8')
  line = general_file.read()
  array = line.split("\n")
  for i in array:
    profile_split = i.split("@")
    print(profile_split)
    username = profile_split[0]
    token = profile_split[1]
    tg_id = profile_split[2]
    bot.send_message(int(tg_id), notify)
  bot.send_message(message.chat.id, 'Уведомления разосланы!')

@bot.message_handler(commands=['info'])
def info(message):
  bot.send_message(message.chat.id, 'Хочу сказать спасибо себе за то, что я гений, и всем людям, которые меня поддерживали. Отдельное спасибо моей лучшей подруге, лучше её нет никого)\nСвязь со мной - @yandexerr')

keep_alive()
bot.polling(interval = 0, none_stop = True)