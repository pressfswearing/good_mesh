import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QCheckBox, QLabel, QPlainTextEdit, QPushButton


class MacOrder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pos1 = QCheckBox('Чизбургер', self)
        self.pos1.move(50, 60)

        self.pos2 = QCheckBox('Гамбургер', self)
        self.pos2.move(50, 100)

        self.pos3 = QCheckBox('Кока-Кола', self)
        self.pos3.move(50, 140)

        self.pos4 = QCheckBox('Нагетсы', self)
        self.pos4.move(50, 180)

        self.positions = [self.pos1, self.pos2, self.pos3, self.pos4]

        self.res = QPlainTextEdit(self)
        self.res.setEnabled(False)
        self.res.move(50, 270)
        self.res.resize(400, 250)

        self.btn = QPushButton('Заказать', self)
        self.btn.resize(70, 30)
        self.btn.move(50, 230)
        self.btn.clicked.connect(self.order)

        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Заказ в Макдональдсе')

    def order(self):
        self.res.clear()
        self.res.appendPlainText('Ваш заказ:')
        self.res.appendPlainText('')
        for i in self.positions:
            if i.isChecked():
                self.res.appendPlainText(i.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MacOrder()
    ex.show()
    sys.exit(app.exec())
