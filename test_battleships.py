import pytest
from battleships import *

def test_is_sunk1():
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(s)==True
    #add at least four more tests for is_sunk by the project submission deadline

def test_ship_type1():
    #add at least one test for ship_type by the deadline of session 7 assignment
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert ship_type(s)=="cruiser"
    #provide at least five tests in total for ship_type by the project submission deadline

def test_is_open_sea1():
    f = [(0, 0, True, 4, {}),
         (2, 0, True, 3, {}),
         (2, 4, True, 3, {}),
         (4, 0, True, 2, {}),
         (4, 3, True, 2, {}),
         (4, 6, True, 2, {}),
         (6, 0, True, 1, {}),
         (6, 2, True, 1, {}),
         (6, 4, True, 1, {}),
         (6, 6, True, 1, {})]
    assert is_open_sea(6, 6, f)==False

def test_is_open_sea2():
    #occupied square (top left square of ship)
    f = [(0, 0, True, 4, {}),
         (2, 0, True, 3, {}),
         (2, 4, True, 3, {}),
         (4, 0, True, 2, {}),
         (4, 3, True, 2, {}),
         (4, 6, True, 2, {}),
         (6, 0, True, 1, {}),
         (6, 2, True, 1, {}),
         (6, 4, True, 1, {}),
         (6, 6, True, 1, {})]
    assert is_open_sea(4, 0, f)==False

def test_is_open_sea3():
    #vertically adjacent square
    f = [(6, 0, False, 4, {}),
         (1, 0, False, 2, {}),
         (7, 2, True, 1, {}),
         (1, 3, True, 1, {}),
         (5, 3, True, 3, {}),
         (7, 4, True, 3, {}),
         (6, 1, False, 2, {}),
         (4, 7, True, 1, {}),
         (9, 8, True, 1, {}),
         (0, 9, False, 2, {})]
    assert is_open_sea(3, 0, f)==False

def test_is_open_sea4():
    #diagonally adjacent square
    f = [(6, 0, False, 4, {}),
         (1, 0, False, 2, {}),
         (7, 2, True, 1, {}),
         (1, 3, True, 1, {}),
         (5, 3, True, 3, {}),
         (7, 4, True, 3, {}),
         (6, 1, False, 2, {}),
         (4, 7, True, 1, {}),
         (9, 8, True, 1, {}),
         (0, 9, False, 2, {})]
    assert is_open_sea(2, 8, f)==False

def test_is_open_sea5():
    #Occupied square (not top left)
    f = [(6, 0, False, 4, {}),
         (1, 0, False, 2, {}),
         (7, 2, True, 1, {}),
         (1, 3, True, 1, {}),
         (5, 3, True, 3, {}),
         (7, 4, True, 3, {}),
         (6, 1, False, 2, {}),
         (4, 7, True, 1, {}),
         (9, 8, True, 1, {}),
         (0, 9, False, 2, {})]
    assert is_open_sea(9, 0, f)==False

def test_ok_to_place_ship_at1():
    #no overlap, no adjacent squares
    f = [(0, 0, True, 4, {}),
         (2, 0, True, 3, {}),
         (2, 4, True, 3, {}),
         (4, 0, True, 2, {}),
         (4, 3, True, 2, {}),
         (4, 6, True, 2, {}),
         (6, 0, True, 1, {}),
         (6, 2, True, 1, {}),
         (6, 4, True, 1, {})]
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


def test_place_ship_at1():
    #placing submarine in open sea
    f = [(0, 0, True, 4, {}),
         (2, 0, True, 3, {}),
         (2, 4, True, 3, {}),
         (4, 0, True, 2, {}),
         (4, 3, True, 2, {}),
         (4, 6, True, 2, {}),
         (6, 0, True, 1, {}),
         (6, 2, True, 1, {}),
         (6, 4, True, 1, {})]
    f1 = [(0, 0, True, 4, {}),
           (2, 0, True, 3, {}),
           (2, 4, True, 3, {}),
           (4, 0, True, 2, {}),
           (4, 3, True, 2, {}),
           (4, 6, True, 2, {}),
           (6, 0, True, 1, {}),
           (6, 2, True, 1, {}),
           (6, 4, True, 1, {}),
           (6, 6, True, 1, {})]
    for ship in f1:
        assert ship in place_ship_at(6, 6, True, 1, f)
    #provide at least five tests in total for place_ship_at by the project submission deadline

def test_place_ship_at2():
    #placing cruiser in open sea
    f = [(0, 0, True, 4, {}),
         (2, 0, True, 3, {}),
         (4, 0, True, 2, {}),
         (4, 3, True, 2, {}),
         (4, 6, True, 2, {}),
         (6, 0, True, 1, {}),
         (6, 2, True, 1, {}),
         (6, 4, True, 1, {}),
         (6, 6, True, 1, {})]
    f1 = [(0, 0, True, 4, {}),
          (2, 0, True, 3, {}),
          (2, 4, True, 3, {}),
          (4, 0, True, 2, {}),
          (4, 3, True, 2, {}),
          (4, 6, True, 2, {}),
          (6, 0, True, 1, {}),
          (6, 2, True, 1, {}),
          (6, 4, True, 1, {}),
          (6, 6, True, 1, {})]
    for ship in f1:
        assert ship in place_ship_at(2, 4, True, 3, f)

def test_place_ship_at3():
    #placing battleship in open sea
    f = [(1, 5, True, 3, {}),
         (3, 2, True, 3, {}),
         (5, 2, True, 2, {}),
         (5, 5, True, 2, {}),
         (5, 9, True, 1, {}),
         (6, 0, True, 1, {}),
         (7, 5, False, 2, {}),
         (8, 0, True, 1, {}),
         (9, 7, True, 1, {})]
    f1 = [(0, 9, False, 4, {}),
          (1, 5, True, 3, {}),
          (3, 2, True, 3, {}),
          (5, 2, True, 2, {}),
          (5, 5, True, 2, {}),
          (5, 9, True, 1, {}),
          (6, 0, True, 1, {}),
          (7, 5, False, 2, {}),
          (8, 0, True, 1, {}),
          (9, 7, True, 1, {})]
    for ship in f1:
        assert ship in place_ship_at(0, 9, False, 4, f)

def test_check_if_hits1():
    #add at least one test for check_if_hits by the deadline of session 7 assignment
    #hit to top left square of battleship
    f = [(0, 0, True, 4, {}),
         (2, 0, True, 3, {}),
         (2, 4, True, 3, {}),
         (4, 0, True, 2, {}),
         (4, 3, True, 2, {}),
         (4, 6, True, 2, {}),
         (6, 0, True, 1, {}),
         (6, 2, True, 1, {}),
         (6, 4, True, 1, {}),
         (6, 4, True, 1, {}),
         (6, 6, True, 1, {})]
    assert check_if_hits(0, 0, f)==True
    #provide at least five tests in total for check_if_hits by the project submission deadline

def test_hit1():
    #add at least one test for hit by the deadline of session 7 assignment
    #hit to submarine
    f = [(0, 0, True, 4, {}),
         (2, 0, True, 3, {}),
         (2, 4, True, 3, {}),
         (4, 0, True, 2, {}),
         (4, 3, True, 2, {}),
         (4, 6, True, 2, {}),
         (6, 0, True, 1, {}),
         (6, 2, True, 1, {}),
         (6, 4, True, 1, {}),
         (6, 4, True, 1, {}),
         (6, 6, True, 1, {})]
    s = (6, 6, True, 1, {})
    f_1 = [(0, 0, True, 4, {}),
          (2, 0, True, 3, {}),
          (2, 4, True, 3, {}),
          (4, 0, True, 2, {}),
          (4, 3, True, 2, {}),
          (4, 6, True, 2, {}),
          (6, 0, True, 1, {}),
          (6, 2, True, 1, {}),
          (6, 4, True, 1, {}),
          (6, 4, True, 1, {}),
          (6, 6, True, 1, {(6,6)})]
    assert type(hit(0, 0, f))==(f_1, s)
    #provide at least five tests in total for hit by the project submission deadline

def test_are_unsunk_ships_left1():
    #add at least one test for are_unsunk_ships_left by the deadline of session 7 assignment
    #just one submarine sunk
    f = [(0, 0, True, 4, {}),
         (2, 0, True, 3, {}),
         (2, 4, True, 3, {}),
         (4, 0, True, 2, {}),
         (4, 3, True, 2, {}),
         (4, 6, True, 2, {}),
         (6, 0, True, 1, {}),
         (6, 2, True, 1, {}),
         (6, 4, True, 1, {}),
         (6, 4, True, 1, {}),
         (6, 6, True, 1, {(6, 6)})]
    assert are_unsunk_ships_left(f)==True
    #provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
    
