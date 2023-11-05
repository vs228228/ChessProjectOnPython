from PyQt6.QtWidgets import QMainWindow, QApplication
from design.testDESIGN import Ui_Form
import sys
import unittest
from logic.board import Board
from my_unittest import TestingBoard
from design.splachWindow1 import Ui_Form2
from design.splachWindow3 import Ui_Form1


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Chess")

class SplachWindow(QMainWindow, Ui_Form1):

    def __init__(self):
        super(SplachWindow, self).__init__()
        self.setupUi(self)



if __name__ == '__main__':
    # TODO Использовать паттерн MVP

    # unittest.main()
    app = QApplication(sys.argv)

    window = MainWindow()
  #  window.show()
    window2 = SplachWindow()
    window2.setFixedSize(739, 668)
    window2.show()

    app.exec()
