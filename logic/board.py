# Модуль логики шахматной доски

import copy

from PyQt6.QtWidgets import QMessageBox, QPushButton

from logic.pawn import Pawn
from logic.rock import Rock
from logic.knight import Knight
from logic.king import King
from logic.queen import Queen
from logic.bishop import Bishop

"""
Класс Board является классом, реализующем логику шахмат.
Проверка мата, шаха и т.д., а также передвижение фигур реализованы тут
"""


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
        self.isFindCheck = False
        self.isFindStalament = False

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
        # print(row)
        # print(col)
        # print(self.can_move_figure(3, 7, row, col))
        # print(self.can_move_figure(3, 7, 0, 4))
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
        # msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Close)
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

    def is_checkmate(self):
        self.isWhite = not self.isWhite
        if self.isCheck() is True:
            self.isFindCheck = True
            for i in range(8):
                for j in range(8):
                    board2 = copy.deepcopy(self.board)
                    if self.board[i][j] is not None:
                        if self.board[i][j].get_color() == "White" and \
                                self.isWhite is False:
                            for row in range(8):
                                for col in range(8):
                                    self.isWhite = not self.isWhite
                                    if self.move_figure(i, j, row, col) \
                                            is True:
                                        self.isWhite = not self.isWhite
                                        if self.isCheck() is False:
                                            self.board = copy.deepcopy(board2)
                                            self.isFindCheck = False
                                            return False
                                    self.board = copy.deepcopy(board2)
                                    self.isWhite = not self.isWhite
                        elif self.board[i][j].get_color() == "Black" and \
                                self.isWhite is True:
                            for row in range(8):
                                for col in range(8):
                                    self.isWhite = not self.isWhite
                                    if self.move_figure(i, j, row, col) \
                                            is True:
                                        self.isWhite = not self.isWhite
                                        if self.isCheck() is False:
                                            self.board = copy.deepcopy(board2)
                                            self.isFindCheck = False
                                            return False
                                    self.board = copy.deepcopy(board2)
                                    self.isWhite = not self.isWhite
            self.isWhite = not self.isWhite
            self.board = copy.deepcopy(board2)
            self.isFindCheck = False
            return True
        else:
            self.isWhite = not self.isWhite
            self.isFindCheck = False
            return False

    def is_stalemate(self):
        self.isWhite = not self.isWhite
        if self.isCheck() is False:
            self.isFindStalament = True
            for i in range(8):
                for j in range(8):
                    board2 = copy.deepcopy(self.board)
                    if self.board[i][j] is not None:
                        if self.board[i][j].get_color() == "White" and \
                                self.isWhite is False:
                            self.isWhite = not self.isWhite
                            for row in range(8):
                                for col in range(8):
                                    if self.move_figure(i, j, row, col) \
                                            is True:
                                        self.isFindStalament = False
                                        self.board = copy.deepcopy(board2)
                                        return False
                        elif self.board[i][j].get_color() == "Black" and \
                                self.isWhite is True:
                            self.isWhite = not self.isWhite
                            for row in range(8):
                                for col in range(8):
                                    if self.move_figure(i, j, row, col) \
                                            is True:
                                        self.isFindStalament = False
                                        self.board = copy.deepcopy(board2)
                                        return False
            self.isFindStalament = False
            return True
        else:
            self.isWhite = not self.isWhite
            self.isFindStalament = False
            return False

    def castling_condition(self, row, col, new_row, new_col):
        if self.board[new_row][new_col] is not None:
            if self.board[row][col].get_name() == "King" and \
                    self.board[new_row][new_col].get_name() == "Rock":

                print(self.board[row][col].is_moved())
                print(self.board[new_row][new_col].is_moved())
                if self.board[row][col].is_moved() is False and \
                        self.board[new_row][new_col].is_moved() is False:
                    if self.board[row][col].get_color() == \
                            self.board[new_row][new_col].get_color():
                        print("Заход есть")

                        return True

        return False

    def can_move_figure(self, row, col, new_row, new_col):
        if self.board[row][col] is None:
            return False

        # print(self.isWhite)
        # print(self.board[row][col].get_color())

        if self.isWhite is False and self.board[row][col].get_color() == "White":
            return False

        if self.isWhite is True and self.board[row][col].get_color() == "Black":
            return False

        return self.board[row][col].can_move(row, col, new_row, new_col, self.board)

    def move_figure(self, row, col, new_row, new_col):
        if self.castling_condition(row, col, new_row, new_col) is True:
            if self.isWhite is True and \
                    self.board[row][col].get_color() == "Black":
                return False
            elif self.isWhite is False and \
                    self.board[row][col].get_color() == "White":
                return False
            # print("Ты точно смог бро")
            if self.board[new_row][new_col].is_way_clear \
                        (new_row, new_col, row, col, self.board) is True:
                # print("Ты точно смог бро 2")
                king_col = 0
                rock_col = 0
                if col > new_col:
                    king_col = col - 2
                    rock_col = king_col + 1
                else:
                    king_col = col + 2
                    rock_col = king_col - 1

                board2 = copy.deepcopy(self.board)
                self.isWhite = not self.isWhite
                self.board[row][rock_col] = self.board[row][col]
                self.board[row][col] = None
                # print(self.isCheck())
                if self.isCheck() is True:
                    self.isWhite = not self.isWhite
                    self.board = copy.deepcopy(board2)
                    return False
                self.board[row][king_col] = self.board[row][rock_col]
                self.board[row][rock_col] = None
                # print(self.isCheck())
                if self.isCheck() is True:
                    self.isWhite = not self.isWhite
                    self.board = copy.deepcopy(board2)
                    return False

                self.board = copy.deepcopy(board2)
                self.board[row][king_col] = self.board[row][col]
                self.board[row][col] = None
                self.board[new_row][rock_col] = self.board[new_row][new_col]
                self.board[new_row][new_col] = None
                # self.isWhite = not self.isWhite
                # print(self.board)
                return True
        elif self.can_move_figure(row, col, new_row, new_col) is True:
            board2 = copy.deepcopy(self.board)
            # print(board2)
            self.board[new_row][new_col] = self.board[row][col]
            self.board[row][col] = None
            self.isWhite = not self.isWhite
            if self.board[new_row][new_col].get_name() == "Pawn" and \
                    (new_row == 0 or new_row == 7):
                self.pawnToSmth()
            if self.isCheck() is True:
                print("Под шахом будет после такого хода")
                #print(board2)
                self.board = copy.deepcopy(board2)
                self.isWhite = not self.isWhite
                return False

            if self.isFindCheck is False:
                # print(self.isWhite)
                if self.is_checkmate() is True:
                    msg = QMessageBox()
                    msg.setWindowTitle("Мат")
                    msg.setText("Мат")
                    msg.setStandardButtons(QMessageBox.StandardButton.Ok)

                    msg.exec()

            return True
        else:
            return False
