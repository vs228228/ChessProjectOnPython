from PyQt6.QtWidgets import QMainWindow, QApplication
from design.testDESIGN import Ui_Form
import sys
import unittest
from logic.board import Board
from my_unittest import TestingBoard


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Chess")


if __name__ == '__main__':
    # TODO Использовать паттерн MVP

    # unittest.main()
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
