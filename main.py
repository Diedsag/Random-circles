import sys
from random import randrange
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.but = QPushButton('Кнопка', self)
        self.but.move(50, 50)
        self.resize(500, 500)
        self.but.clicked.connect(self.draw)
        self.D = False

    def draw(self):
        self.D = True
        self.repaint()

    def paintEvent(self, event):
        if self.D:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(randrange(0, 255), randrange(0, 255), randrange(0, 255)))
            r = randrange(10, 100)
            qp.drawEllipse(randrange(100, 400), randrange(100, 400), r, r)
            self.D = False
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

