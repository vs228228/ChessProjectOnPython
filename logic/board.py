from logic.pawn import Pawn
from logic.rock import Rock
from logic.knight import Knight
from logic.king import King
from logic.queen import Queen
from logic.bishop import Bishop


class Board:
    """
    TODO В общем, после каждого хода можно проверять короля противоположного цвета
    TODO чисто тем, что применять к нему методы can_move всех иных фигур не его цвета
    TODO так можно понять, будет ли шах после этого хода или нет
    TODO а ещё проверять это в начале каждого хода, там можно выявить шах
    """
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        self.board[0] = [
            Rock("White"), Knight("White"),
            Bishop("White"), Queen("White"),
            King("White"), Bishop("White"),
            Knight("White"), Rock("White")
        ]
        self.board[1] = [
            Pawn("White"), Pawn("White"),
            Pawn("White"), Pawn("White"),
            Pawn("White"), Pawn("White"),
            Pawn("White"), Pawn("White")
        ]

        self.board[6] = [
            Pawn("Black"), Pawn("Black"),
            Pawn("Black"), Pawn("Black"),
            Pawn("Black"), Pawn("Black"),
            Pawn("Black"), Pawn("Black")
        ]
        self.board[7] = [
            Rock("Black"), Knight("Black"),
            Bishop("Black"), Queen("Black"),
            King("Black"), Bishop("Black"),
            Knight("Black"), Rock("Black")
        ]

    def can_move_figure(self, row, col, new_row, new_col):
        if self.board[row][col] is None:
            return False

        return self.board[row][col].can_move(row, col, new_row, new_col, self.board)
