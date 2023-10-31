from logic.chessFigure import ChessFigure


class Bishop(ChessFigure):
    __NAME__ = "Bishop"

    def is_move_valid(self, row, col, new_row, new_col, board):
        if self.is_friendly_figure(new_row, new_col, board):
            return False

        if not (abs(row - new_row) == abs(col - new_col)):
            return False

        return True

    def is_way_clear(self, row, col, new_row, new_col, board):
        # при изменении метода менять его так же и в Queen
        move_distance_row = 1 if (row < new_row) else -1
        move_distance_col = 1 if (col < new_col) else -1

        while (row != new_row - move_distance_row and
               col != new_col - move_distance_col):
            row += move_distance_row
            col += move_distance_col
            if not self.is_empty_cell(row, col, board):
                return False

        return True

    def can_move(self, row, col, new_row, new_col, board):
        if not self.is_move_valid(row, col, new_row, new_col, board):
            return False

        if not self.is_way_clear(row, col, new_row, new_col, board):
            return False

        return True
