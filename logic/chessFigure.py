class ChessFigure:
    __NAME__ = "SomeFigure"

    def __init__(self, color):
        self.color = color

    # Метод проверяет возможные препядствия на пути
    def is_way_clear(self, row, col, new_row, new_col, board):
        pass

    # Метод проверяет валидность хода (с учетом is_way_clear)
    def can_move(self, row, col, new_row, new_col, board):
        pass

    def get_color(self):
        return self.color

    def get_name(self):
        return self.__NAME__

    def is_friendly_figure(self, new_row, new_col, board):
        if board[new_row][new_col] is None:
            return False
        if board[new_row][new_col].get_color() == self.color:
            return True
        return False

    def is_move_valid(self, row, col, new_row, new_col, board):
        pass

    @staticmethod
    def is_empty_cell(row, col, board):
        if board[row][col] is None:
            return True

        return False
