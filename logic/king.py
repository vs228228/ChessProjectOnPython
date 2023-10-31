from logic.chessFigure import ChessFigure


class King(ChessFigure):
    __NAME__ = "King"

    def is_move_valid(self, row, col, new_row, new_col, board):
        if self.is_friendly_figure(new_row, new_col, board):
            return False

        if not (max(abs(row - new_row), abs(col - new_col)) == 1):
            return False

        return True

    def can_move(self, row, col, new_row, new_col, board):
        if not self.is_move_valid(row, col, new_row, new_col, board):
            return False

        return True