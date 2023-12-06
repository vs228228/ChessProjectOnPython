import copy

from PyQt6.QtWidgets import QMessageBox, QPushButton

from logic.pawn import Pawn
from logic.rock import Rock
from logic.knight import Knight
from logic.king import King
from logic.queen import Queen
from logic.bishop import Bishop


# Если что, вернуть то, что черные снизу, а белые сверху. Для этого тут поменять board + поменять класс Pawn

class Board:

    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        self.board[7] = [
            Rock("White"), Knight("White"),
            Bishop("White"), Queen("White"),
            King("White"), Bishop("White"),
            Knight("White"), Rock("White")
        ]
        self.board[6] = [
            Pawn("White"), Pawn("White"),
            Pawn("White"), Pawn("White"),
            Pawn("White"), Pawn("White"),
            Pawn("White"), Pawn("White")
        ]

        self.board[1] = [
            Pawn("Black"), Pawn("Black"),
            Pawn("Black"), Pawn("Black"),
            Pawn("Black"), Pawn("Black"),
            Pawn("Black"), Pawn("Black")
        ]
        self.board[0] = [
            Rock("Black"), Knight("Black"),
            Bishop("Black"), Queen("Black"),
            King("Black"), Bishop("Black"),
            Knight("Black"), Rock("Black")
        ]

        self.isWhite = True

    def findKingRow(self):
        if self.isWhite is True:
            for i in range(8):
                for j in range(8):
                    if self.board[i][j] is None:
                        continue
                    if self.board[i][j].get_name() == "King" and \
                            self.board[i][j].get_color() == "Black":
                        return i
        else:
            for i in range(8):
                for j in range(8):
                    if self.board[i][j] is None:
                        continue
                    if self.board[i][j].get_name() == "King" and \
                            self.board[i][j].get_color() == "White":
                        return i

    def findKingCol(self):
        if self.isWhite is True:
            for i in range(8):
                for j in range(8):
                    if self.board[i][j] is None:
                        continue
                    if self.board[i][j].get_name() == "King" and \
                            self.board[i][j].get_color() == "Black":
                        return j
        else:
            for i in range(8):
                for j in range(8):
                    if self.board[i][j] is None:
                        continue
                    if self.board[i][j].get_name() == "King" and \
                            self.board[i][j].get_color() == "White":
                        return j

    def isCheck(self):
        row = self.findKingRow()
        col = self.findKingCol()
        print(row)
        print(col)
        print(self.can_move_figure(3, 7, row, col))
        print(self.can_move_figure(3, 7, 0, 4))
        for i in range(8):
            for j in range(8):
                if self.can_move_figure(i, j, row, col) is True:
                    return True
        return False

    def transformPawn(self, btn):
        row = 0
        col = 0
        if self.isWhite is False:
            for i in range(8):
                if self.board[row][i] is None:
                    continue
                if self.board[row][i].get_name() == "Pawn":
                    col = i

        else:
            row = 7
            col = 0
            for i in range(8):
                if self.board[row][i] is None:
                    continue
                if self.board[row][i].get_name() == "Pawn":
                    col = i

        text = ""
        if self.isWhite is False:
            text = "White"
        else:
            text = "Black"
        match btn.text():
            case "Ферзь":
                self.board[row][col] = Queen(text)

            case "Слон":
                self.board[row][col] = Bishop(text)

            case "Конь":
                self.board[row][col] = Knight(text)

            case "Ладья":
                self.board[row][col] = Rock(text)

    def pawnToSmth(self):
        msg = QMessageBox()
        msg.setWindowTitle("Пешка дошла до конца")
        msg.setText("В какую фигуру превратить пешку?")
        #msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Close)
        queen = QPushButton("Ферзь")
        knight = QPushButton("Конь")
        rock = QPushButton("Ладья")
        bishop = QPushButton("Слон")
        msg.addButton(queen, QMessageBox.ButtonRole.AcceptRole)
        msg.addButton(knight, QMessageBox.ButtonRole.AcceptRole)
        msg.addButton(rock, QMessageBox.ButtonRole.AcceptRole)
        msg.addButton(bishop, QMessageBox.ButtonRole.AcceptRole)

        msg.buttonClicked.connect(self.transformPawn)

        msg.exec()


    def can_move_figure(self, row, col, new_row, new_col):
        if self.board[row][col] is None:
            return False

        #print(self.isWhite)
        #print(self.board[row][col].get_color())

        if self.isWhite is False and self.board[row][col].get_color() == "White":
            return False

        if self.isWhite is True and self.board[row][col].get_color() == "Black":
            return False

        return self.board[row][col].can_move(row, col, new_row, new_col, self.board)

    def move_figure(self, row, col, new_row, new_col):
        if self.can_move_figure(row, col, new_row, new_col) is True:
            board2 = copy.deepcopy(self.board)
            print(board2)
            self.board[new_row][new_col] = self.board[row][col]
            self.board[row][col] = None
            self.isWhite = not self.isWhite
            if self.board[new_row][new_col].get_name() == "Pawn" and \
                    (new_row == 0 or new_row == 7):
                self.pawnToSmth()
            if self.isCheck() is True:
                print("Ivan krit")
                print(board2)
                self.board = copy.deepcopy(board2)
                self.isWhite = not self.isWhite
                return False
            return True
        else:
            return False
