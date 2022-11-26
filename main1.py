import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow


class Exspresso(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("mn.ui", self)
        self.otobr()

    def otobr(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        db.setDatabaseName("coffee.db")
        # И откроем подключение
        db.open()

        # QTableView - виджет для отображения данных из базы
        view = self.tableView
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        model = QSqlTableModel(self, db)
        model.setTable('cof')
        model.select()
        self.model = model
        view.setModel(model)


if __name__ == "__main__":
     app = QApplication(sys.argv)
     ex = Exspresso()
     ex.show()
     sys.exit(app.exec_())
