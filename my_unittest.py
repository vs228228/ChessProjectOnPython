import unittest
from logic.mainLogic import Board
from logic.king import King
from logic.knight import Knight
from logic.bishop import Bishop
from logic.queen import Queen
from logic.pawn import Pawn
from logic.rock import Rock


class TestBoard1(Board):
    def __init__(self):
        # super.__init__()
        self.board = [[None] * 8 for _ in range(8)]
        self.board[3][3] = Rock("White")
        self.board[3][6] = Rock("Black")
        self.board[6][3] = Rock("Black")
        self.board[1][3] = Rock("Black")
        self.board[3][1] = Rock("Black")
        self.board[1][6] = Rock("Black")
        self.isWhite = True


class TestBoard2(Board):
    def __init__(self):
        # super.__init__()
        self.board = [[None] * 8 for _ in range(8)]
        self.board[3][3] = Bishop("White")
        self.board[6][6] = Pawn("Black")
        self.board[1][1] = Pawn("Black")
        self.board[1][5] = Pawn("Black")
        self.board[5][1] = Pawn("Black")
        self.board[6][0] = Bishop("Black")
        self.isWhite = True


class TestBoard3(Board):
    def __init__(self):
        # super.__init__()
        self.board = [[None] * 8 for _ in range(8)]
        self.board[1][1] = Pawn("White")
        self.board[1][3] = Pawn("White")
        self.board[2][4] = Pawn("Black")
        self.board[2][2] = Pawn("White")
        self.board[2][3] = Pawn("White")
        self.board[6][6] = Pawn("Black")
        self.isWhite = True


class TestBoard4(Board):
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        self.board[4][4] = Knight("Black")
        self.board[2][5] = Knight("White")
        self.board[4][6] = Knight("White")
        self.isWhite = False


class TestBoard5(Board):
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        self.board[4][4] = King("Black")
        self.board[3][3] = Pawn("Black")
        self.board[5][5] = Pawn("White")
        self.isWhite = False


class TestBoard6(Board):
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        self.board[4][4] = Queen("White")
        self.board[6][6] = Pawn("Black")
        self.board[1][1] = Pawn("White")
        self.board[5][3] = Pawn("Black")
        self.board[3][5] = Pawn("White")
        self.board[4][6] = Pawn("Black")
        self.board[4][2] = Pawn("White")
        self.board[2][4] = Pawn("White")
        self.board[6][4] = Pawn("Black")
        self.isWhite = True


class TestingBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.board1 = TestBoard1()
        self.board2 = TestBoard2()
        self.board3 = TestBoard3()
        self.board4 = TestBoard4()
        self.board5 = TestBoard5()
        self.board6 = TestBoard6()

    # def test_1(self):
    #     self.assertEqual(self.board.can_move_figure(1, 1, 2, 1), True)
    #
    # def test_2(self):
    #     self.assertEqual(self.board.can_move_figure(1, 5, 2, 5), True)
    #
    # def test_3(self):
    #     self.assertEqual(self.board.can_move_figure(0, 0, 1, 3), False)
    #
    # def test_4(self):
    #     self.assertEqual(self.board.can_move_figure(0, 1, 2, 2), True)
    #
    # def test_5(self):
    #     self.assertEqual(self.board.can_move_figure(5, 5, 5, 5), False)
    #
    # def test_6(self):
    #     self.assertEqual(self.board1.can_move_figure(3, 3, 5, 3), True)
    #
    # # def test_7(self):
    # #     self.assertEqual(self.board.can_move_figure(3, 3, 5, 5), True)
    # #
    # # def test_8(self):
    # #     self.assertEqual(self.board2.can_move_figure(4,6,4,4), True)

    def test_Rock_1(self):
        self.assertEqual(self.board1.can_move_figure(3, 3, 5, 3), True)

    def test_Rock_2(self):
        self.assertEqual(self.board1.can_move_figure(3, 3, 3, 5), True)

    def test_Rock_3(self):
        self.assertEqual(self.board1.can_move_figure(3, 3, 3, 3), False)

    def test_Rock_4(self):
        self.assertEqual(self.board1.can_move_figure(3, 3, 4, 4), False)

    def test_Rock_5(self):
        self.assertEqual(self.board1.can_move_figure(3, 3, 3, 6), True)

    def test_Rock_6(self):
        self.assertEqual(self.board1.can_move_figure(3, 3, 6, 3), True)

    def test_Rock_7(self):
        self.assertEqual(self.board1.can_move_figure(3, 3, 3, 7), False)

    def test_Rock_8(self):
        self.assertEqual(self.board1.can_move_figure(3, 3, 7, 3), False)

    def test_Rock_9(self):
        self.assertEqual(self.board1.can_move_figure(3, 3, 3, 1), True)

    def test_Rock_10(self):
        self.assertEqual(self.board1.can_move_figure(3, 3, 1, 3), True)

    def test_Rock_11(self):
        self.assertEqual(self.board1.can_move_figure(3, 3, 3, 0), False)

    def test_Rock_12(self):
        self.assertEqual(self.board1.can_move_figure(3, 3, 0, 3), False)

    def test_Rock_13(self):
        self.board1.isWhite = False
        self.assertEqual(self.board1.can_move_figure(1, 3, 2, 3), True)

    def test_Rock_14(self):
        self.board1.isWhite = False
        self.assertEqual(self.board1.can_move_figure(1, 3, 1, 5), True)

    def test_Rock_15(self):
        self.assertEqual(self.board1.can_move_figure(1, 3, 1, 6), False)

    def test_Bishop_1(self):
        self.assertEqual(self.board2.can_move_figure(3, 3, 5, 5), True)

    def test_Bishop_2(self):
        self.assertEqual(self.board2.can_move_figure(3, 3, 1, 1), True)

    def test_Bishop_3(self):
        self.assertEqual(self.board2.can_move_figure(3, 3, 4, 2), True)

    def test_Bishop_4(self):
        self.assertEqual(self.board2.can_move_figure(3, 3, 1, 5), True)

    def test_Bishop_5(self):
        self.assertEqual(self.board2.can_move_figure(3, 3, 3, 3), False)

    def test_Bishop_6(self):
        self.assertEqual(self.board2.can_move_figure(3, 3, 3, 4), False)

    def test_Bishop_7(self):
        self.assertEqual(self.board2.can_move_figure(3, 3, 4, 3), False)

    def test_Bishop_8(self):
        self.assertEqual(self.board2.can_move_figure(3, 3, 6, 6), True)

    def test_Bishop_9(self):
        self.assertEqual(self.board2.can_move_figure(3, 3, 7, 7), False)

    def test_Bishop_10(self):
        self.assertEqual(self.board2.can_move_figure(3, 3, 1, 1), True)

    def test_Bishop_11(self):
        self.assertEqual(self.board2.can_move_figure(3, 3, 0, 0), False)

    def test_Bishop_12(self):
        self.assertEqual(self.board2.can_move_figure(3, 3, 1, 5), True)

    def test_Bishop_13(self):
        self.assertEqual(self.board2.can_move_figure(3, 3, 0, 6), False)

    def test_Bishop_14(self):
        self.assertEqual(self.board2.can_move_figure(3, 3, 5, 1), True)

    def test_Bishop_15(self):
        self.assertEqual(self.board2.can_move_figure(3, 3, 6, 0), False)

    def test_Bishop_16(self):
        self.assertEqual(self.board2.can_move_figure(6, 0, 5, 1), False)

    # def test_Pawn_1(self):
    #     self.assertEqual(self.board3.can_move_figure(1, 1, 2, 1), True)
    #
    # def test_Pawn_2(self):
    #     self.assertEqual(self.board3.can_move_figure(1, 1, 3, 1), True)
    #
    # def test_Pawn_3(self):
    #     self.assertEqual(self.board3.can_move_figure(1, 3, 2, 4), True)
    #
    # def test_Pawn_4(self):
    #     self.assertEqual(self.board3.can_move_figure(1, 3, 2, 2), False)
    #
    # def test_Pawn_5(self):
    #     self.assertEqual(self.board3.can_move_figure(1, 1, 2, 3), False)
    #
    # def test_Pawn_6(self):
    #     self.assertEqual(self.board3.can_move_figure(1, 1, 2, 2), False)
    #
    # def test_Pawn_7(self):
    #     self.assertEqual(self.board3.can_move_figure(1, 1, 2, 0), False)
    #
    # def test_Pawn_8(self):
    #     self.assertEqual(self.board3.can_move_figure(1, 1, 3, 0), False)
    #
    # def test_Pawn_9(self):
    #     self.assertEqual(self.board3.can_move_figure(1, 1, 1, 0), False)
    #
    # def test_Pawn_10(self):
    #     self.assertEqual(self.board3.can_move_figure(1, 1, 5, 1), False)
    #
    # def test_Pawn_11(self):
    #     self.assertEqual(self.board3.can_move_figure(2, 4, 0, 4), False)
    #
    # def test_Pawn_12(self):
    #     self.assertEqual(self.board3.can_move_figure(2, 4, 1, 4), True)
    #
    # def test_Pawn_13(self):
    #     self.assertEqual(self.board3.can_move_figure(2, 2, 1, 1), False)
    #
    # def test_Pawn_14(self):
    #     self.assertEqual(self.board3.can_move_figure(6, 6, 5, 6), True)
    #
    # def test_Pawn_15(self):
    #     self.assertEqual(self.board3.can_move_figure(2, 4, 1, 3), True)
    #
    # def test_Pawn_16(self):
    #     self.assertEqual(self.board3.can_move_figure(6, 6, 4, 6), True)
    #
    # def test_Pawn_17(self):
    #     self.assertEqual(self.board3.can_move_figure(6, 6, 3, 6), False)
    #
    # def test_Pawn_18(self):
    #     self.assertEqual(self.board3.can_move_figure(6, 6, 6, 4), False)
    #
    # def test_Pawn_19(self):
    #     self.assertEqual(self.board3.can_move_figure(6, 6, 6, 6), False)

    def test_Knight_1(self):
        self.assertEqual(self.board4.can_move_figure(4, 4, 2, 3), True)

    def test_Knight_2(self):
        self.assertEqual(self.board4.can_move_figure(4, 4, 3, 2), True)

    def test_Knight_3(self):
        self.assertEqual(self.board4.can_move_figure(4, 4, 6, 5), True)

    def test_Knight_4(self):
        self.assertEqual(self.board4.can_move_figure(4, 4, 5, 6), True)

    def test_Knight_5(self):
        self.assertEqual(self.board4.can_move_figure(4, 4, 6, 3), True)

    def test_Knight_6(self):
        self.assertEqual(self.board4.can_move_figure(4, 4, 3, 6), True)

    def test_Knight_7(self):
        self.assertEqual(self.board4.can_move_figure(4, 4, 5, 2), True)

    def test_Knight_8(self):
        self.assertEqual(self.board4.can_move_figure(4, 4, 2, 5), True)

    def test_Knight_9(self):
        self.assertEqual(self.board4.can_move_figure(2, 5, 4, 6), False)

    def test_Knight_10(self):
        self.assertEqual(self.board4.can_move_figure(4, 4, 4, 4), False)

    def test_Knight_11(self):
        self.assertEqual(self.board4.can_move_figure(4, 4, 5, 5), False)

    def test_Knight_12(self):
        self.assertEqual(self.board4.can_move_figure(4, 4, 2, 0), False)

    def test_Knight_13(self):
        self.assertEqual(self.board4.can_move_figure(4, 4, 0, 2), False)

    def test_King_1(self):
        self.assertEqual(self.board5.can_move_figure(4, 4, 3, 3), False)

    def test_King_2(self):
        self.assertEqual(self.board5.can_move_figure(4, 4, 3, 4), True)

    def test_King_3(self):
        self.assertEqual(self.board5.can_move_figure(4, 4, 3, 5), True)

    def test_King_4(self):
        self.assertEqual(self.board5.can_move_figure(4, 4, 4, 3), True)

    def test_King_5(self):
        self.assertEqual(self.board5.can_move_figure(4, 4, 4, 4), False)

    def test_King_6(self):
        self.assertEqual(self.board5.can_move_figure(4, 4, 4, 5), True)

    def test_King_7(self):
        self.assertEqual(self.board5.can_move_figure(4, 4, 5, 3), True)

    def test_King_8(self):
        self.assertEqual(self.board5.can_move_figure(4, 4, 5, 4), True)

    def test_King_9(self):
        self.assertEqual(self.board5.can_move_figure(4, 4, 5, 5), True)

    def test_King_10(self):
        self.assertEqual(self.board5.can_move_figure(4, 4, 0, 0), False)

    def test_King_11(self):
        self.assertEqual(self.board5.can_move_figure(4, 4, 2, 4), False)

    def test_King_12(self):
        self.assertEqual(self.board5.can_move_figure(4, 4, 4, 2), False)

    def test_Queen_1(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 5, 5), True)

    def test_Queen_2(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 3, 3), True)

    def test_Queen_3(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 5, 4), True)

    def test_Queen_4(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 4, 5), True)

    def test_Queen_5(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 6, 6), True)

    def test_Queen_6(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 7, 7), False)

    def test_Queen_7(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 1, 1), False)

    def test_Queen_8(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 0, 0), False)

    def test_Queen_9(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 5, 3), True)

    def test_Queen_10(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 6, 2), False)

    def test_Queen_11(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 3, 5), False)

    def test_Queen_12(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 2, 6), False)

    def test_Queen_13(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 4, 6), True)

    def test_Queen_14(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 4, 7), False)

    def test_Queen_15(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 4, 2), False)

    def test_Queen_16(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 4, 1), False)

    def test_Queen_17(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 7, 2), False)

    def test_Queen_18(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 4, 4), False)

    def test_Queen_19(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 2, 4), False)

    def test_Queen_20(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 1, 4), False)

    def test_Queen_21(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 6, 4), True)

    def test_Queen_22(self):
        self.assertEqual(self.board6.can_move_figure(4, 4, 7, 4), False)

