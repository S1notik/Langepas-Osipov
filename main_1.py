import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        #qp.setPen(QPen(QColor(r, g, b), 8, Qt.SolidLine))
        qp.setBrush(QBrush(QColor(r, g, b), Qt.SolidPattern))
        x = randint(0, 400)
        y = randint(0, 400)
        r = randint(0, 100)
        qp.drawEllipse(x, y, x + r, y + r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())