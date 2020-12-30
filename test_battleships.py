import pytest
from battleships import *

def test_is_sunk1():
    #vertical cruiser is sunk
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(s)==True

def test_is_sunk2():
    #submarine is not sunk
    s = (0, 7, True, 1, set())
    assert is_sunk(s)==False

def test_is_sunk3():
    #horizontal battleship is sunk
    s = (8, 5, True, 4, {(8, 5), (8, 6), (8, 7), (8, 8)})
    assert is_sunk(s) == True

def test_is_sunk4():
    #horizontal cruiser hit but not sunk
    s = (3, 4, True, 3, {(3, 4), (3, 6)})
    assert is_sunk(s) == False

def test_is_sunk5():
    #vertical destroyer sunk
    s = (8, 0, False, 2, {(8, 0), (9, 0)})
    assert is_sunk(s) == True


def test_ship_type1():
    #cruiser
    s = (2, 3, False, 3, set())
    assert ship_type(s)=="cruiser"

def test_ship_type2():
    #battleship
    s = (4, 2, False, 4, set())
    assert ship_type(s)=="battleship"

def test_ship_type3():
    #destroyer
    s = (1, 8, False, 2, set())
    assert ship_type(s)=="destroyer"

def test_ship_type4():
    #destroyer
    s = (5, 8, True, 1, {(5, 8)})
    assert ship_type(s)=="submarine"

def test_ship_type5():
    #battleship (horizontal)
    s = (9, 0, True, 4, {(9, 1), (9, 2), (9, 3)})
    assert ship_type(s)=="battleship"



def test_is_open_sea1():
    #free square
    f = [(0, 0, True, 4, set()),
         (2, 0, True, 3, set()),
         (2, 4, True, 3, set()),
         (4, 0, True, 2, set()),
         (4, 3, True, 2, set()),
         (4, 6, True, 2, set()),
         (6, 0, True, 1, set()),
         (6, 2, True, 1, set()),
         (6, 4, True, 1, set()),
         (6, 6, True, 1, set())]
    assert is_open_sea(6, 6, f)==False

def test_is_open_sea2():
    #occupied square (top left square of ship)
    f = [(0, 0, True, 4, set()),
         (2, 0, True, 3, set()),
         (2, 4, True, 3, set()),
         (4, 0, True, 2, set()),
         (4, 3, True, 2, set()),
         (4, 6, True, 2, set()),
         (6, 0, True, 1, set()),
         (6, 2, True, 1, set()),
         (6, 4, True, 1, set()),
         (6, 6, True, 1, set())]
    assert is_open_sea(4, 0, f)==False

def test_is_open_sea3():
    #vertically adjacent square
    f = [(6, 0, False, 4, set()),
         (1, 0, False, 2, set()),
         (7, 2, True, 1, set()),
         (1, 3, True, 1, set()),
         (5, 3, True, 3, set()),
         (7, 4, True, 3, set()),
         (6, 8, False, 2, set()),
         (4, 7, True, 1, set()),
         (9, 8, True, 1, set()),
         (0, 9, False, 2, set())]
    assert is_open_sea(3, 0, f)==False

def test_is_open_sea4():
    #diagonally adjacent square
    f = [(6, 0, False, 4, set()),
         (1, 0, False, 2, set()),
         (7, 2, True, 1, set()),
         (1, 3, True, 1, set()),
         (5, 3, True, 3, set()),
         (7, 4, True, 3, set()),
         (6, 8, False, 2, set()),
         (4, 7, True, 1, set()),
         (9, 8, True, 1, set()),
         (0, 9, False, 2, set())]
    assert is_open_sea(2, 8, f)==False

def test_is_open_sea5():
    #Occupied square (not top left)
    f = [(6, 0, False, 4, set()),
         (1, 0, False, 2, set()),
         (7, 2, True, 1, set()),
         (1, 3, True, 1, set()),
         (5, 3, True, 3, set()),
         (7, 4, True, 3, set()),
         (6, 8, False, 2, set()),
         (4, 7, True, 1, set()),
         (9, 8, True, 1, set()),
         (0, 9, False, 2, set())]
    assert is_open_sea(9, 0, f)==False

def test_is_open_sea6():
    #horizontally adjacent square
    f = [(6, 0, False, 4, set()),
         (1, 0, False, 2, set()),
         (7, 2, True, 1, set()),
         (1, 3, True, 1, set()),
         (5, 3, True, 3, set()),
         (7, 4, True, 3, set()),
         (6, 8, False, 2, set()),
         (4, 7, True, 1, set()),
         (9, 8, True, 1, set()),
         (0, 9, False, 2, set())]
    assert is_open_sea(2, 1, f)==False

def test_ok_to_place_ship_at1():
    #no overlap, no adjacent squares
    f = [(0, 0, True, 4, set()),
         (2, 0, True, 3, set()),
         (2, 4, True, 3, set()),
         (4, 0, True, 2, set()),
         (4, 3, True, 2, set()),
         (4, 6, True, 2, set()),
         (6, 0, True, 1, set()),
         (6, 2, True, 1, set()),
         (6, 4, True, 1, set())]
    assert ok_to_place_ship_at(6, 6, True, 1, f)==True

def test_ok_to_place_ship_at2():
    #overlap
    f = [(0, 0, True, 4, {}),
         (2, 0, True, 3, {}),
         (2, 4, True, 3, {}),
         (4, 0, True, 2, {}),
         (4, 6, True, 2, {}),
         (6, 0, True, 1, {}),
         (6, 2, True, 1, {}),
         (6, 4, True, 1, {}),
         (6, 6, True, 1, {})]
    assert ok_to_place_ship_at(1, 6, False, 2, f) == False

def test_ok_to_place_ship_at3():
    #runs off bottom of grid
    f = [(0, 5, True, 1, {}),
         (0, 8, True, 1, {}),
         (2, 7, True, 2, {}),
         (3, 2, True, 2, {}),
         (4, 5, True, 2, {}),
         (4, 9, False, 3, {}),
         (5, 1, True, 1, {}),
         (7, 2, True, 4, {}),
         (9, 5, True, 1, {})]
    assert ok_to_place_ship_at(9, 8, False, 3, f) == False

def test_ok_to_place_ship_at4():
    #runs off rhs of grid
    f = [(0, 5, True, 1, {}),
         (0, 8, True, 1, {}),
         (2, 7, True, 2, {}),
         (3, 2, True, 2, {}),
         (4, 5, True, 2, {}),
         (4, 9, False, 3, {}),
         (5, 1, True, 1, {}),
         (7, 2, True, 4, {}),
         (9, 5, True, 1, {})]
    assert ok_to_place_ship_at(9, 9, True, 3, f) == False

def test_ok_to_place_ship_at5():
    #place destroyer that occupies an adjecent square to a battleship
    f = [(0, 1, True, 2, set()),
         (0, 7, False, 4, set()),
         (3, 2, True, 3, set()),
         (4, 0, True, 1, set()),
         (5, 6, True, 1, set()),
         (6, 0, False, 2, set()),
         (6, 2, True, 1, set()),
         (7, 5, True, 3, set()),
         (8, 9, True, 1, set())]
    assert ok_to_place_ship_at(3, 8, False, 2, f) == False


def test_place_ship_at1():
    #placing submarine in open sea
    f = [(0, 0, True, 4, set()),
         (2, 0, True, 3, set()),
         (2, 4, True, 3, set()),
         (4, 0, True, 2, set()),
         (4, 3, True, 2, set()),
         (4, 6, True, 2, set()),
         (6, 0, True, 1, set()),
         (6, 2, True, 1, set()),
         (6, 4, True, 1, set())]
    f1 = [(0, 0, True, 4, set()),
           (2, 0, True, 3, set()),
           (2, 4, True, 3, set()),
           (4, 0, True, 2, set()),
           (4, 3, True, 2, set()),
           (4, 6, True, 2, set()),
           (6, 0, True, 1, set()),
           (6, 2, True, 1, set()),
           (6, 4, True, 1, set()),
           (6, 6, True, 1, set())]
    for ship in f1:
        assert ship in place_ship_at(6, 6, True, 1, f)
    #provide at least five tests in total for place_ship_at by the project submission deadline

def test_place_ship_at2():
    #placing horizontal cruiser in open sea
    f = [(0, 0, True, 4, set()),
         (2, 0, True, 3, set()),
         (4, 0, True, 2, set()),
         (4, 3, True, 2, set()),
         (4, 6, True, 2, set()),
         (6, 0, True, 1, set()),
         (6, 2, True, 1, set()),
         (6, 4, True, 1, set()),
         (6, 6, True, 1, set())]
    f1 = [(0, 0, True, 4, set()),
          (2, 0, True, 3, set()),
          (2, 4, True, 3, set()),
          (4, 0, True, 2, set()),
          (4, 3, True, 2, set()),
          (4, 6, True, 2, set()),
          (6, 0, True, 1, set()),
          (6, 2, True, 1, set()),
          (6, 4, True, 1, set()),
          (6, 6, True, 1, set())]
    for ship in f1:
        assert ship in place_ship_at(2, 4, True, 3, f)

def test_place_ship_at3():
    #placing vertical battleship in open sea
    f = [(1, 5, True, 3, set()),
         (3, 2, True, 3, set()),
         (5, 2, True, 2, set()),
         (5, 5, True, 2, set()),
         (5, 9, True, 1, set()),
         (6, 0, True, 1, set()),
         (7, 5, False, 2, set()),
         (8, 0, True, 1, set()),
         (9, 7, True, 1, set())]
    f1 = [(0, 9, False, 4, set()),
          (1, 5, True, 3, set()),
          (3, 2, True, 3, set()),
          (5, 2, True, 2, set()),
          (5, 5, True, 2, set()),
          (5, 9, True, 1, set()),
          (6, 0, True, 1, set()),
          (7, 5, False, 2, set()),
          (8, 0, True, 1, set()),
          (9, 7, True, 1, set())]
    for ship in f1:
        assert ship in place_ship_at(0, 9, False, 4, f)

def test_place_ship_at4():
    #place vertical destroyer in open sea
    f = [(0, 1, True, 2, set()),
         (0, 7, False, 4, set()),
         (3, 2, True, 3, set()),
         (4, 0, True, 1, set()),
         (5, 6, True, 1, set()),
         (6, 0, False, 2, set()),
         (6, 2, True, 1, set()),
         (7, 5, True, 3, set()),
         (8, 9, True, 1, set())]
    f1 = [(0, 1, True, 2, set()),
          (0, 7, False, 4, set()),
          (3, 2, True, 3, set()),
          (4, 0, True, 1, set()),
          (5, 6, True, 1, set()),
          (6, 0, False, 2, set()),
          (6, 2, True, 1, set()),
          (7, 5, True, 3, set()),
          (8, 9, True, 1, set()),
          (3, 9, False, 2, set())]
    for ship in f1:
        assert ship in place_ship_at(3, 9, False, 2, f)

def test_place_ship_at5():
    #place vertical cruiser in open sea
    f = [(0, 1, True, 2, set()),
         (0, 7, False, 4, set()),
         (3, 2, True, 3, set()),
         (4, 0, True, 1, set()),
         (5, 6, True, 1, set()),
         (6, 0, False, 2, set()),
         (6, 2, True, 1, set()),
         (8, 9, True, 1, set()),
         (3, 9, False, 2, set())]
    f1 = [(0, 1, True, 2, set()),
          (0, 7, False, 4, set()),
          (3, 2, True, 3, set()),
          (4, 0, True, 1, set()),
          (5, 6, True, 1, set()),
          (6, 0, False, 2, set()),
          (6, 2, True, 1, set()),
          (7, 5, False, 3, set()),
          (8, 9, True, 1, set()),
          (3, 9, False, 2, set())]
    for ship in f1:
        assert ship in place_ship_at(7, 5, False, 3, f)

def test_check_if_hits1():
    #hit to top left square of battleship
    f = [(0, 0, True, 4, set()),
         (2, 0, True, 3, set()),
         (2, 4, True, 3, set()),
         (4, 0, True, 2, set()),
         (4, 3, True, 2, set()),
         (4, 6, True, 2, set()),
         (6, 0, True, 1, set()),
         (6, 2, True, 1, set()),
         (6, 4, True, 1, set()),
         (6, 6, True, 1, set())]
    assert check_if_hits(0, 0, f)==True
    #provide at least five tests in total for check_if_hits by the project submission deadline

def test_check_if_hits2():
    #no hit (adjacent)
    f = [(0, 0, False, 2, set()),
         (1, 3, True, 4, set()),
         (1, 9, True, 1, set()),
         (3, 3, True, 3, set()),
         (4, 7, False, 2, set()),
         (5, 2, True, 2, set()),
         (6, 0, False, 3, set()),
         (7, 2, True, 1, set()),
         (7, 5, True, 1, set()),
         (9, 8, True, 1, set())]
    assert check_if_hits(0, 5, f)==False

def test_check_if_hits3():
    #hit (not top left square)
    f = [(0, 0, False, 2, set()),
         (1, 3, True, 4, set()),
         (1, 9, True, 1, set()),
         (3, 3, True, 3, set()),
         (4, 7, False, 2, set()),
         (5, 2, True, 2, set()),
         (6, 0, False, 3, set()),
         (7, 2, True, 1, set()),
         (7, 5, True, 1, set()),
         (9, 8, True, 1, set())]
    assert check_if_hits(3, 5, f)==True

def test_check_if_hits4():
    #hit to vertical cruiser (not top left square)
    f = [(0, 0, False, 2, set()),
         (1, 3, True, 4, set()),
         (1, 9, True, 1, set()),
         (3, 3, True, 3, set()),
         (4, 7, False, 2, set()),
         (5, 2, True, 2, set()),
         (6, 0, False, 3, set()),
         (7, 2, True, 1, set()),
         (7, 5, True, 1, set()),
         (9, 8, True, 1, set())]
    assert check_if_hits(8, 0, f)==True

def test_check_if_hits5():
    #hit to horizontal destroyer (not top left square)
    f = [(0, 0, False, 2, set()),
         (1, 3, True, 4, set()),
         (1, 9, True, 1, set()),
         (3, 3, True, 3, set()),
         (4, 7, False, 2, set()),
         (5, 2, True, 2, set()),
         (6, 0, False, 3, set()),
         (7, 2, True, 1, set()),
         (7, 5, True, 1, set()),
         (9, 8, True, 1, set())]
    assert check_if_hits(5, 3, f)==True

def test_hit1():
    #hit to submarine on top left square
    f = [(0, 0, True, 4, set()),
         (2, 0, True, 3, set()),
         (2, 4, True, 3, set()),
         (4, 0, True, 2, set()),
         (4, 3, True, 2, set()),
         (4, 6, True, 2, set()),
         (6, 0, True, 1, set()),
         (6, 2, True, 1, set()),
         (6, 4, True, 1, set()),
         (6, 6, True, 1, set())]
    f_1 = [(0, 0, True, 4, set()),
           (2, 0, True, 3, set()),
           (2, 4, True, 3, set()),
           (4, 0, True, 2, set()),
           (4, 3, True, 2, set()),
           (4, 6, True, 2, set()),
           (6, 0, True, 1, set()),
           (6, 2, True, 1, set()),
           (6, 4, True, 1, set()),
           (6, 6, True, 1, {(6,6)})]
    assert hit(6, 6, f)==(f_1, f_1[9])

def test_hit2():
    #hit to horizontal destroyer on non-top left square
    f = [(0, 0, True, 4, set()),
         (2, 0, True, 3, set()),
         (2, 4, True, 3, set()),
         (4, 0, True, 2, set()),
         (4, 3, True, 2, set()),
         (4, 6, True, 2, set()),
         (6, 0, True, 1, set()),
         (6, 2, True, 1, set()),
         (6, 4, True, 1, set()),
         (6, 6, True, 1, set())]
    f_1 = [(0, 0, True, 4, set()),
           (2, 0, True, 3, set()),
           (2, 4, True, 3, set()),
           (4, 0, True, 2, set()),
           (4, 3, True, 2, {(4, 4)}),
           (4, 6, True, 2, set()),
           (6, 0, True, 1, set()),
           (6, 2, True, 1, set()),
           (6, 4, True, 1, set()),
           (6, 6, True, 1, set())]
    assert hit(4, 4, f)==(f_1, f_1[4])

def test_hit3():
    #hit to vertical battleship on non-top left square
    f = [(1, 2, False, 2, set()),
         (2, 6, True, 3, set()),
         (4, 0, True, 1, set()),
         (4, 3, True, 1, set()),
         (4, 7, True, 3, set()),
         (6, 2, True, 2, set()),
         (6, 6, True, 1, set()),
         (6, 9, False, 4, set()),
         (8, 4, False, 2, set()),
         (9, 1, True, 1, set())]
    f_1 = [(1, 2, False, 2, set()),
           (2, 6, True, 3, set()),
           (4, 0, True, 1, set()),
           (4, 3, True, 1, set()),
           (4, 7, True, 3, set()),
           (6, 2, True, 2, set()),
           (6, 6, True, 1, set()),
           (6, 9, False, 4, {(7, 9)}),
           (8, 4, False, 2, set()),
           (9, 1, True, 1, set())]
    assert hit(7, 9, f)==(f_1, f_1[7])

def test_hit4():
    #hit to horizontal destroyer on non-top left square
    f = [(0, 0, False, 2, set()),
         (1, 3, True, 4, set()),
         (1, 9, True, 1, set()),
         (3, 3, True, 3, set()),
         (4, 7, False, 2, {(4, 7)}),
         (5, 2, True, 2, set()),
         (6, 0, False, 3, set()),
         (7, 2, True, 1, set()),
         (7, 5, True, 1, set()),
         (9, 8, True, 1, set())]
    f_1 = [(0, 0, False, 2, set()),
           (1, 3, True, 4, set()),
           (1, 9, True, 1, set()),
           (3, 3, True, 3, set()),
           (4, 7, False, 2, {(4, 7), (5, 7)}),
           (5, 2, True, 2, set()),
           (6, 0, False, 3, set()),
           (7, 2, True, 1, set()),
           (7, 5, True, 1, set()),
           (9, 8, True, 1, set())]
    assert hit(5, 7, f)==(f_1, f_1[4])

def test_hit5():
    #hit to horizontal destroyer on non-top left square
    f = [(0, 0, False, 2, set()),
         (1, 3, True, 4, set()),
         (1, 9, True, 1, set()),
         (3, 3, True, 3, set()),
         (4, 7, False, 2, {(4, 7)}),
         (5, 2, True, 2, set()),
         (6, 0, False, 3, set()),
         (7, 2, True, 1, set()),
         (7, 5, True, 1, set()),
         (9, 8, True, 1, set())]
    f_1 = [(0, 0, False, 2, set()),
           (1, 3, True, 4, set()),
           (1, 9, True, 1, set()),
           (3, 3, True, 3, {(3, 3)}),
           (4, 7, False, 2, {(4, 7)}),
           (5, 2, True, 2, set()),
           (6, 0, False, 3, set()),
           (7, 2, True, 1, set()),
           (7, 5, True, 1, set()),
           (9, 8, True, 1, set())]
    assert hit(3, 3, f)==(f_1, f_1[3])

def test_are_unsunk_ships_left1():
    # provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
    #Just one submarine sunk
    f = [(0, 0, True, 4, set()),
         (2, 0, True, 3, set()),
         (2, 4, True, 3, set()),
         (4, 0, True, 2, set()),
         (4, 3, True, 2, set()),
         (4, 6, True, 2, set()),
         (6, 0, True, 1, set()),
         (6, 2, True, 1, set()),
         (6, 4, True, 1, set()),
         (6, 4, True, 1, set()),
         (6, 6, True, 1, {(6, 6)})]
    assert are_unsunk_ships_left(f)==True

def test_are_unsunk_ships_left2():
    # provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
    #Everything sunk
    f = f = [(1, 2, False, 2, {(1, 2), (2, 2)}),
             (2, 6, True, 3, {(2, 6), (2, 7), (2, 8)}),
             (4, 0, True, 1, {(4, 0)}),
             (4, 3, True, 1, {(4, 3)}),
             (4, 7, True, 3, {(4, 7), (4, 8), (4, 9)}),
             (6, 2, True, 2, {(6, 2), (6, 3)}),
             (6, 6, True, 1, {(6, 6)}),
             (6, 9, False, 4, {(6, 9), (7, 9), (8, 9), (9, 9)}),
             (8, 4, False, 2, {(8, 4), (9, 4)}),
             (9, 1, True, 1, {(9, 1)})]
    assert are_unsunk_ships_left(f)==False

def test_are_unsunk_ships_left3():
    #no hits
    f = [(0, 0, False, 2, set()),
         (1, 3, True, 4, set()),
         (1, 9, True, 1, set()),
         (3, 3, True, 3, set()),
         (4, 7, False, 2, set()),
         (5, 2, True, 2, set()),
         (6, 0, False, 3, set()),
         (7, 2, True, 1, set()),
         (7, 5, True, 1, set()),
         (9, 8, True, 1, set())]
    assert are_unsunk_ships_left(f)==True

def test_are_unsunk_ships_left4():
    #top left square of every ship hit
    f = [(0, 0, False, 2, {(0, 0)}),
         (1, 3, True, 4, {(1, 3)}),
         (1, 9, True, 1, {(1, 9)}),
         (3, 3, True, 3, {(3, 3)}),
         (4, 7, False, 2, {(4, 7)}),
         (5, 2, True, 2, {(5, 2)}),
         (6, 0, False, 3, {(6, 0)}),
         (7, 2, True, 1, {(7, 2)}),
         (7, 5, True, 1, {(7, 5)}),
         (9, 8, True, 1, {(9, 8)})]
    assert are_unsunk_ships_left(f)==True

def test_are_unsunk_ships_left5():
    #single non-top left square not hit
    f = [(0, 0, False, 2, {(0, 0), (1, 0)}),
         (1, 3, True, 4, {(1, 3), (1, 4), (1, 5), (1, 6)}),
         (1, 9, True, 1, {(1, 9)}),
         (3, 3, True, 3, {(3, 3), (3, 4), (3, 5)}),
         (4, 7, False, 2, {(4, 7), (5, 7)}),
         (5, 2, True, 2, {(5, 2), (5, 3)}),
         (6, 0, False, 3, {(6, 0), (7, 0)}),
         (7, 2, True, 1, {(7, 2)}),
         (7, 5, True, 1, {(7, 5)}),
         (9, 8, True, 1, {(9, 8)})]
    assert are_unsunk_ships_left(f)==True

def test_update_board_hit1():
    #hit to (0, 0)
    board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."] for i in range(10)]
    updated = update_board_hit(0, 0, board)
    assert updated[0][0]=="*"

def test_update_board_miss1():
    #miss to (1, 3)
    board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."] for i in range(10)]
    updated = update_board_miss(1, 3, board)
    assert updated[1][3]=="-"

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

def test_is_valid_input1():
    #valid input of the form "x y" where 0<=x<=9 and 0<=y<=9
    assert is_valid_input(["0", "9"])==True

def test_is_valid_input2():
    #floating point values
    assert is_valid_input(["1.9", "7"])==False

def test_is_valid_input3():
    #string
    assert is_valid_input(["Hello", "there"])==False

def test_is_valid_input4():
    #too many integers
    assert is_valid_input(["1", "2", "3"])==False

def test_is_valid_input5():
    #integer greater than 9
    assert is_valid_input(["1", "11"])==False

def test_is_valid_input6():
    #integer less than 0
    assert is_valid_input(["-3", "1"])==False


