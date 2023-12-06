from logic.chessFigure import ChessFigure


class Pawn(ChessFigure):
    __NAME__ = "Pawn"

    def is_move_valid(self, row, col, new_row, new_col, board):
        if self.is_friendly_figure(new_row, new_col, board):
            return False

        if col != new_col:
            return False

        if self.color == "Black":
            start_pos = 1
            move_distance = 1
        else:
            start_pos = 6
            move_distance = -1

        if new_row == row + move_distance:
            return True

        if row == start_pos and new_row == row + 2 * move_distance:
            return True

        return False

    def can_attack(self, row, col, new_row, new_col, board):
        move_distance = 1 if (self.color == "Black") else -1
        if (Pawn.is_empty_cell(new_row, new_col, board) or
                self.is_friendly_figure(new_row, new_col, board)):
            return False

        if row + move_distance == new_row and abs(new_col - col) == 1:
            return True

        return False

    def is_way_clear(self, row, col, new_row, new_col, board):
        move_distance = 1 if (self.color == "Black") else -1

        if (row + move_distance == new_row and
                Pawn.is_empty_cell(new_row, new_col, board)):
            return True

        if (row + 2 * move_distance == new_row and
                Pawn.is_empty_cell(row + move_distance, col, board) and
                Pawn.is_empty_cell(new_row, new_col, board)):
            return True

        return False

    def can_move(self, row, col, new_row, new_col, board):
        if self.can_attack(row, col, new_row, new_col, board):
            return True

        if not self.is_move_valid(row, col, new_row, new_col, board):
            return False

        if not self.is_way_clear(row, col, new_row, new_col, board):
            return False

        return True
