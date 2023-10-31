from logic.chessFigure import ChessFigure
from logic.rock import Rock
from logic.bishop import Bishop


class Queen(ChessFigure):
    __NAME__ = "Queen"

    def is_move_valid(self, row, col, new_row, new_col, board):
        if self.is_friendly_figure(new_row, new_col, board):
            return False

        if not ((abs(row - new_row) == abs(col - new_col)) or
                (row == new_row or col == new_col)):
            return False

        return True

    @staticmethod
    def is_move_like_rock(row, col, new_row, new_col):
        if row == new_row or col == new_col:
            return True

        return False

    @staticmethod
    def is_move_like_bishop(row, col, new_row, new_col):
        if abs(row - new_row) == abs(col - new_col):
            return True

        return False

    # сделать проверку на то, как ходит ферзь и от этого менять метод is_way_clear

    def is_way_clear(self, row, col, new_row, new_col, board):
        # при изменении метода менять его так же и в Bishop/Rock
        if self.is_move_like_bishop(row, col, new_row, new_col):
            b = Bishop(self.color)
            return b.can_move(row, col, new_row, new_col, board)
            # move_distance_row = 1 if (row < new_row) else -1
            # move_distance_col = 1 if (col < new_col) else -1
            #
            # while row != new_row - 1 and col != new_col - 1:
            #     row += move_distance_row
            #     col += move_distance_col
            #     if not self.is_empty_cell(row, col, board):
            #         return False
            #
            #     return True

        elif self.is_move_like_rock(row, col, new_row, new_col):
            r = Rock(self.color)
            return r.can_move(row, col, new_row, new_col, board)
        #     step = 0
        #     is_col_move = False
        #     if row == new_row:
        #         step = 1 if (col < new_col) else -1
        #         is_col_move = True
        #     else:
        #         step = 1 if (row < new_row) else -1
        #
        #     while col != new_col - 1 and is_col_move:
        #         col += step
        #         if not Rock.is_empty_cell(row, col, board):
        #             return False
        #
        #     while row != new_row - 1:
        #         row += step
        #         if not Rock.is_empty_cell(row, col, board):
        #             return False
        #
        #     return True
        #
        # return False

    def can_move(self, row, col, new_row, new_col, board):
        if not self.is_move_valid(row, col, new_row, new_col, board):
            return False

        if not self.is_way_clear(row, col, new_row, new_col, board):
            return False

        return True
