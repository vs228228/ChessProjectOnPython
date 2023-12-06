from PyQt6.QtWidgets import QMainWindow, QApplication, QMenu
# from design.testDESIGN import Ui_Form
import sys
from design.lolo import Ui_Form
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

    board = Board()
    selectedFig = None

    def findXPos(self, px):
        x = 0
        startPX = 27
        while x < 7:
            if startPX < px:
                x += 1
                if startPX == 82:
                    startPX += 54
                else:
                    startPX += 55
            else:
                break
        return x

    def findYPos(self, px):
        y = 0
        startPX = 28
        while y < 7:
            if startPX < px:
                y += 1
                if startPX == 136:
                    startPX += 55
                else:
                    startPX += 54
            else:
                break
        return y

    def changeWhitePawn(self, text):
        match text:
            case "logic.queen.Queen":
                self.selectedFig.setStyleSheet \
                    ("image:url(design/chess_Figure/wQ.png);\n"
                     "borded: none;\n"
                     "background-color: rgba(255,255,255,0);")

            case "logic.rock.Rock":
                self.selectedFig.setStyleSheet \
                    ("image:url(design/chess_Figure/wR.png);\n"
                     "borded: none;\n"
                     "background-color: rgba(255,255,255,0);\n"
                     "")

            case "logic.knight.Knight":
                self.selectedFig.setStyleSheet\
                    ("image:url(design/chess_Figure/wN.png);\n"
"borded: none;\n"
"background-color: rgba(255,255,255,0);")

            case "logic.bishop.Bishop":
                self.selectedFig.setStyleSheet\
                    ("image:url(design/chess_Figure/wB.png);\n"
"borded: none;\n"
"background-color: rgba(255,255,255,0);")

    def changeBlackPawn(self, text):
        match text:
            case "logic.queen.Queen":
                self.selectedFig.setStyleSheet \
                    ("image:url(design/chess_Figure/bQ.png);\n"
"borded: none;\n"
"background-color: rgba(255,255,255,0);")

            case "logic.rock.Rock":
                self.selectedFig.setStyleSheet \
                    ("image:url(design/chess_Figure/bR.png);\n"
"borded: none;\n"
"background-color: rgba(255,255,255,0);\n"
"")

            case "logic.knight.Knight":
                self.selectedFig.setStyleSheet \
                    ("image:url(design/chess_Figure/bN.png);\n"
"borded: none;\n"
"background-color: rgba(255,255,255,0);")

            case "logic.bishop.Bishop":
                self.selectedFig.setStyleSheet \
                    ("image:url(design/chess_Figure/bB.png);\n"
"borded: none;\n"
"background-color: rgba(255,255,255,0);")

    def mousePressEvent(self, event):
        # print("Tist")
        cell = self.childAt(event.pos())
        if cell is None:
            self.selectedFig = None
        elif self.selectedFig is None:
            self.selectedFig = cell
            x = self.findXPos(cell.pos().x())
            y = self.findYPos(cell.pos().y())
            if self.board.board[y][x] is None:
                self.selectedFig = None
        else:
            startX = self.findXPos(self.selectedFig.pos().x())
            startY = self.findYPos(self.selectedFig.pos().y())
            endX = self.findXPos(cell.pos().x())
            endY = self.findYPos(cell.pos().y())
            print(startX)
            print(startY)
            print(endX)
            print(endY)
            # print(self.board.can_move_figure(startY, startX, endY, endX))

            isSomeFigure = False
            if self.board.board[endY][endX] is not None:
                isSomeFigure = True

            if self.board.move_figure(startY, startX, endY, endX):
                if isSomeFigure is True:
                    cell.deleteLater()
                self.selectedFig.move(cell.pos().x(), cell.pos().y())
                # cell.deleteLater()
                if endY == 0 and self.board.board[endY][endX].get_color()\
                        == "White":
                    index = str(self.board.board[endY][endX]).find(' ')
                    text = str(self.board.board[endY][endX])[1:index]
                    self.changeWhitePawn(text)

                elif endY == 7 and self.board.board[endY][endX].get_color()\
                        == "Black":
                    index = str(self.board.board[endY][endX]).find(' ')
                    text = str(self.board.board[endY][endX])[1:index]
                    self.changeBlackPawn(text)

            self.selectedFig = None


    def mouseReleaseEvent(self, event):
        # print("test")
        cell = self.childAt(event.pos())
        if self.selectedFig is not None and cell != self.selectedFig:
            startX = self.findXPos(self.selectedFig.pos().x())
            startY = self.findYPos(self.selectedFig.pos().y())
            endX = self.findXPos(cell.pos().x())
            endY = self.findYPos(cell.pos().y())
            # print(startX)
            # print(startY)
            # print(endX)
            # print(endY)
            # print(self.board.can_move_figure(startY, startX, endY, endX))
            isSomeFigure = False

            if self.board.board[endY][endX] is not None:
                isSomeFigure = True

            if self.board.move_figure(startY, startX, endY, endX):
                if isSomeFigure is True:
                    cell.deleteLater()
                self.selectedFig.move(cell.pos().x(), cell.pos().y())
                if endY == 0 and self.board.board[endY][endX].get_color()\
                        == "White":
                    index = str(self.board.board[endY][endX]).find(' ')
                    text = str(self.board.board[endY][endX])[1:index]
                    self.changeWhitePawn(text)

                elif endY == 7 and self.board.board[endY][endX].get_color()\
                        == "Black":
                    index = str(self.board.board[endY][endX]).find(' ')
                    text = str(self.board.board[endY][endX])[1:index]
                    self.changeBlackPawn(text)


            self.selectedFig = None


class SplachWindow(QMainWindow, Ui_Form1):

    def __init__(self):
        super(SplachWindow, self).__init__()
        self.setupUi(self)

    def startProg(self):
        window.show()
        self.close()

    def endProg(self):
        self.close()


# window = MainWindow()

if __name__ == '__main__':
    # TODO Использовать паттерн MVP

    # unittest.main()
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setFixedSize(739, 668)
    # window.show()
    window2 = SplachWindow()
    window2.setFixedSize(739, 668)
    window2.show()

    app.exec()
