from logic.chessFigure import ChessFigure


class Knight(ChessFigure):
    __NAME__ = "Knight"

    def is_move_valid(self, row, col, new_row, new_col, board):
        if self.is_friendly_figure(new_row, new_col, board):
            return False

        if abs(row - new_row) == 2 and abs(col - new_col) == 1:
            return True

        if abs(row - new_row) == 1 and abs(col - new_col) == 2:
            return True

        return False

    def can_move(self, row, col, new_row, new_col, board):
        if self.is_move_valid(row, col, new_row, new_col, board):
            return True

        return False
