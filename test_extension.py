import pytest
from extension import *

def test_update_board_hit1():
    #hit to (0, 0)
    board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."] for i in range(10)]
    update_board_hit(0, 0, board)
    assert board[0][0]=="*"

def test_update_board_miss1():
    #miss to (1, 3)
    board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."] for i in range(10)]
    update_board_miss(1, 3, board)
    assert board[1][3]=="-"

def test_update_board_sink1():
    #sink a cruiser
    board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."] for i in range(10)]
    ship_sunk = (1, 0, True, 3, {(1, 0), (1, 1), (1, 2)})
    update_board_sink(ship_sunk, board)
    assert board[1][0]=="C" and board[1][1]=="C" and board[1][2]=="C"

def test_update_board_sink2():
    #sink a submarine
    board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."] for i in range(10)]
    ship_sunk = (5, 4, True, 1, {(5, 4)})
    update_board_sink(ship_sunk, board)
    assert board[5][4]=="S"