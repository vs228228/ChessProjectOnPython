from logic.chessFigure import ChessFigure


class Rock(ChessFigure):
    __NAME__ = "Rock"
    __isMoved__ = False

    def is_moved(self):
        return self.__isMoved__

    def is_move_valid(self, row, col, new_row, new_col, board):
        if self.is_friendly_figure(new_row, new_col, board):
            return False

        if row != new_row and col != new_col:
            return False

        return True

    def is_way_clear(self, row, col, new_row, new_col, board):
        # при изменении метода менять его так же и в Queen
        step = 0
        is_col_move = False
        if row == new_row:
            step = 1 if (col < new_col) else -1
            is_col_move = True
        else:
            step = 1 if(row < new_row) else -1

        while col != new_col - step and is_col_move:
            col += step
            if not Rock.is_empty_cell(row, col, board):
                return False

        while row != new_row - step and not is_col_move:
            row += step
            if not Rock.is_empty_cell(row, col, board):
                return False

        return True

    def can_move(self, row, col, new_row, new_col, board):
        if not self.is_move_valid(row, col, new_row, new_col, board):
            return False

        if not self.is_way_clear(row, col, new_row, new_col, board):
            return False

        self.__isMoved__ = True
        return True
