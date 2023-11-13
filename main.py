import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QPlainTextEdit
from dnevniklib.homeworks import Homeworks
from dnevniklib.student import Student
from dnevniklib.errors import token as token_error


class dnevnik(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 700, 700, 700)
        self.setWindowTitle('Дневник МЭШ 2.0')

        self.tokenn = QLineEdit(self)
        self.tokenn.move(200, 20)
        self.tokenn.resize(300, 25)
        self.tokenn.setText('paste your token here')

        self.day_for_all = QLineEdit(self)
        self.day_for_all.move(300, 50)
        self.day_for_all.resize(100, 30)
        self.day_for_all.setText('2023-10-25')

        self.homework_button = QPushButton('Домашки', self)
        self.homework_button.move(200, 80)
        self.homework_button.resize(300, 25)
        self.homework_button.clicked.connect(self.homework)

        self.schedule_button = QPushButton('Расписание', self)
        self.schedule_button.move(200, 110)
        self.schedule_button.resize(300, 25)
        self.schedule_button.clicked.connect(self.schedule)

        self.day_marks = QPushButton('Оценки за день', self)
        self.day_marks.move(200, 140)
        self.day_marks.resize(300, 25)
        self.day_marks.clicked.connect(self.day_marks_def)

        self.trimester_for_marks = QLineEdit(self)
        self.trimester_for_marks.move(300, 170)
        self.trimester_for_marks.resize(100, 30)
        self.trimester_for_marks.setText('1, 2, 3')

        self.trimester_marks = QPushButton('Средние баллы за триместр', self)
        self.trimester_marks.move(200, 200)
        self.trimester_marks.resize(300, 25)
        self.trimester_marks.clicked.connect(self.trimester_marks_def)

        self.text_space = QPlainTextEdit(self)
        self.text_space.setEnabled(False)
        self.text_space.move(200, 240)
        self.text_space.resize(300, 375)

        self.info = QPushButton('Информация', self)
        self.info.move(200, 650)
        self.info.resize(300, 25)
        self.info.clicked.connect(self.info_def)

    def homework(self):
        try:
            student = Student(token=self.tokenn.text())
            homework = Homeworks(Student(token=self.tokenn.text()))
            self.text_space.clear()
            self.text_space.appendPlainText(
                'Твои домашки на ' + self.day_for_all.text() + ':')
            self.text_space.appendPlainText('')
            home_workk = homework.get_homework_by_date(self.day_for_all.text())
            for i in range(len(home_workk)):
                self.text_space.appendPlainText(str(home_workk[i]))
        except token_error.DnevnikTokenError:
            self.text_space.clear()
            self.text_space.appendPlainText('Твой токен для бота сломан, напиши разработчику - @yandexerr - он тебе поможет.')

    def schedule(self):
        try:
            student = Student(token=self.tokenn.text())
            homework = Homeworks(Student(token=self.tokenn.text()))
            self.text_space.clear()
            self.text_space.appendPlainText(
                'Твоё расписание на ' + self.day_for_all.text() + ':')
            self.text_space.appendPlainText('')
            sche_dule = homework.get_schedule(self.day_for_all.text())
            for i in range(len(sche_dule)):
                self.text_space.appendPlainText(str(sche_dule[i]))
        except token_error.DnevnikTokenError:
            self.text_space.clear()
            self.text_space.appendPlainText('Твой токен для бота сломан, напиши разработчику - @yandexerr - он тебе поможет.')

    def day_marks_def(self):
        try:
            student = Student(token=self.tokenn.text())
            homework = Homeworks(Student(token=self.tokenn.text()))
            self.text_space.clear()
            self.text_space.appendPlainText(
                'Твои оценки за ' + self.day_for_all.text() + ':')
            self.text_space.appendPlainText('')
            mar_ks = homework.get_marks(self.day_for_all.text())
            for i in range(len(mar_ks)):
                self.text_space.appendPlainText(str(mar_ks[i]))
        except token_error.DnevnikTokenError:
            self.text_space.clear()
            self.text_space.appendPlainText('Твой токен для бота сломан, напиши разработчику - @yandexerr - он тебе поможет.')

    def trimester_marks_def(self):
        student = Student(token=self.tokenn.text())
        homework = Homeworks(Student(token=self.tokenn.text()))
        self.text_space.clear()
        self.text_space.appendPlainText(
            'Твои средние баллы за ' + str(int(self.trimester_for_marks.text())) + ' триместр:')
        self.text_space.appendPlainText('')
        trimes_ter_marks = homework.get_trimester_marks(
            str(int(self.trimester_for_marks.text()) - 1))
        for i in range(len(trimes_ter_marks)):
            self.text_space.appendPlainText(
                str(trimes_ter_marks[i]['name']) + ': ' + str(trimes_ter_marks[i]['mark']))

    def info_def(self):
        self.text_space.clear()
        self.text_space.appendPlainText('Информация о проекте:')
        self.text_space.appendPlainText('')
        self.text_space.appendPlainText(
            'ПК МЭШ был создан yandexerr.t.me в качестве замены')
        self.text_space.appendPlainText(
            'веб-сайту МЭШ, ведь он постоянно лагает и пользоваться им')
        self.text_space.appendPlainText('невозможно.')
        self.text_space.appendPlainText('')
        self.text_space.appendPlainText('Версия: 1.0.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = dnevnik()
    ex.show()
    sys.exit(app.exec())
