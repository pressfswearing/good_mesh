import telebot
from dnevniklib.student import Student
from requests import get
from dnevniklib.homeworks import Homeworks

bot = telebot.TeleBot('6487833703:AAGL9V98CNDHPP7X7FWbYueOug3hstP84Lg')
student = Student(token="eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIyODg2Mzg0Iiwic2NwIjoib3BlbmlkIHByb2ZpbGUiLCJhdWQiOiIyOjEiLCJuYmYiOjE2OTc2NDAyMTUsIm1zaCI6ImRkM2IwN2ZmLWU1NTEtNGY1Ny05NzRhLTYwYWE5YTQwN2RjYSIsImF0aCI6InN1ZGlyIiwiaXNzIjoiaHR0cHM6XC9cL3NjaG9vbC5tb3MucnUiLCJybHMiOiJ7MTpbMTgzOjE2OltdLDMwOjQ6W10sNDA6MTpbXSwyMDoyOltdXX0iLCJleHAiOjE2OTg1MDQyMTUsImlhdCI6MTY5NzY0MDIxNSwianRpIjoiMTliYTQ0NGItZTBkYy00MGJhLWJhNDQtNGJlMGRjMjBiYWJkIiwic3NvIjoiYWQ5MjBlYTUtN2VhZS00ZWFjLTg1YmEtY2E0ZjczM2RjMDY0In0.brV2tA-sqWYf8rANHvLhGtvsvGS5K4RTpH64FMWE3egLmIvNJsplqnpIrigk5yp6OjafA_6pLM1dMCzm424vGoTNnPx93tZAdTCKg4_SY7vMLS1HbrRnpwDSAkNjUDljms-rIWZzq_biDT3VrfS4F9AgQPrplrjQEGwWzWndEpsYYrwDtX0kxuPkZIF2hZMI0EvbQcV25cKfzJTuzLcxhCsCJTjB0oeEWfwxU_v9Tsr7-kiVOxG73be41MxrChmaH25QAcsAgV1Eg17FWe38M0wgayPtC90b-t69C68U1JB_g1Qosrk5jNqxlfvPX9vclU3bzYBi2_0ZAE9GVXnBXw")
homework = Homeworks(Student(token='eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIyODg2Mzg0Iiwic2NwIjoib3BlbmlkIHByb2ZpbGUiLCJhdWQiOiIyOjEiLCJuYmYiOjE2OTc2NDAyMTUsIm1zaCI6ImRkM2IwN2ZmLWU1NTEtNGY1Ny05NzRhLTYwYWE5YTQwN2RjYSIsImF0aCI6InN1ZGlyIiwiaXNzIjoiaHR0cHM6XC9cL3NjaG9vbC5tb3MucnUiLCJybHMiOiJ7MTpbMTgzOjE2OltdLDMwOjQ6W10sNDA6MTpbXSwyMDoyOltdXX0iLCJleHAiOjE2OTg1MDQyMTUsImlhdCI6MTY5NzY0MDIxNSwianRpIjoiMTliYTQ0NGItZTBkYy00MGJhLWJhNDQtNGJlMGRjMjBiYWJkIiwic3NvIjoiYWQ5MjBlYTUtN2VhZS00ZWFjLTg1YmEtY2E0ZjczM2RjMDY0In0.brV2tA-sqWYf8rANHvLhGtvsvGS5K4RTpH64FMWE3egLmIvNJsplqnpIrigk5yp6OjafA_6pLM1dMCzm424vGoTNnPx93tZAdTCKg4_SY7vMLS1HbrRnpwDSAkNjUDljms-rIWZzq_biDT3VrfS4F9AgQPrplrjQEGwWzWndEpsYYrwDtX0kxuPkZIF2hZMI0EvbQcV25cKfzJTuzLcxhCsCJTjB0oeEWfwxU_v9Tsr7-kiVOxG73be41MxrChmaH25QAcsAgV1Eg17FWe38M0wgayPtC90b-t69C68U1JB_g1Qosrk5jNqxlfvPX9vclU3bzYBi2_0ZAE9GVXnBXw'))

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'здесь приветственное сообщение')

@bot.message_handler(commands=['private_data'])
def private_data(message):
	bot.send_message(message.chat.id, 'Имя: ' + student.first_name + \
		'\nОтчество: ' + student.middle_name + \
		'\nФамилия: ' + student.last_name + \
		'\nЛогин: ' + student.login + \
		'\nID: ' + student.person_id + \
		'\nКласс: ' + student.class_name + \
		'\nВозраст: ' + str(student.age))

@bot.message_handler(commands=['homeworks'])
def homeworks(message):
	date = bot.send_message(message.chat.id, 'Введи дату, на которую нужно получить домашку, в таком формате:\n2023-10-18')
	bot.register_next_step_handler(date, homeworks1)
def homeworks1(message):
	date = message.text
	home_workk = homework.get_homework_by_date('2023-10-18')
	for i in range(len(home_workk)):
		strr = str(home_workk[i])
		bot.send_message(message.chat.id, strr)

@bot.message_handler(commands=['marks'])
def marks(message):
	date = bot.send_message(message.chat.id, 'Введи дату, на которую хочешь получить оценки, в таком формате:\n2023-10-18')
	bot.register_next_step_handler(date, marks1)


bot.polling(interval = 0, none_stop = True)