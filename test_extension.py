import pytest
from extension import *

def test_update_board_hit1():
    #hit to (0, 0)
    board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."] for i in range(10)]
    update_board_hit(0, 0, board)
    assert board[0][0]=="*"

def test_update_board_hit2():
    #hit to (6, 2)
    board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."] for i in range(10)]
    update_board_hit(6, 2, board)
    assert board[6][2]=="*"

def test_update_board_miss1():
    #miss to (1, 3)
    board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."] for i in range(10)]
    update_board_miss(1, 3, board)
    assert board[1][3]=="-"

def test_update_board_miss2():
    #miss to (9, 3)
    board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."] for i in range(10)]
    update_board_miss(9, 3, board)
    assert board[9][3]=="-"

def test_update_board_sink1():
    #cruiser sunk
    board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."] for i in range(10)]
    ship_sunk = (1, 0, True, 3, {(1, 0), (1, 1), (1, 2)})
    update_board_sink(ship_sunk, board)
    assert board[1][0]=="C" and board[1][1]=="C" and board[1][2]=="C"

def test_update_board_sink2():
    #submarine sunk
    board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."] for i in range(10)]
    ship_sunk = (5, 4, True, 1, {(5, 4)})
    update_board_sink(ship_sunk, board)
    assert board[5][4]=="S"

def test_update_board_sink3():
    #battleship sunk
    board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."] for i in range(10)]
    ship_sunk = (1, 6, False, 4, {(1, 6), (2, 6), (3, 6), (4, 6)})
    update_board_sink(ship_sunk, board)
    assert board[1][6]=="B" and board[2][6]=="B" and board[3][6]=="B" and board[4][6]=="B"

def test_update_board_sink4():
    #destroyer sunk
    board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."] for i in range(10)]
    ship_sunk = (8, 8, True, 2, {(8, 8), (8, 9)})
    update_board_sink(ship_sunk, board)
    assert board[8][8]=="D" and board[8][9]=="D"