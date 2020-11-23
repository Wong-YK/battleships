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
    assert (is_open_sea(4, 0, f) and is_open_sea(4, 1, f))==False

def test_is_open_sea3():
    f = [(6, 0, False, 4, {}),
         (7, 2, True, 3, {}),
         (3, 2, True, 3, {}),
         (8, 4, True, 2, {}),
         (5, 4, True, 2, {}),
         (2, 4, True, 2, {}),
         (2, 9, True, 1, {}),
         (6, 7, True, 1, {}),
         (6, 5, True, 1, {}),
         (6, 3, True, 1, {})]
    assert (is_open_sea(3, 2, f) and is_open_sea(4, 2, f) and is_open_sea(5, 2, f))==False

def test_is_open_sea4():
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
    coords = [(1, 3), (1, 4), (1, 5), (1, 6), (1,7),
              (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
              (3, 3), (3, 4), (3, 5), (3, 6), (3, 7)]
    for coord in coords:
        assert is_open_sea(coord[0], coord[1], f)==False

def test_ok_to_place_ship_at1():
    #add at least one test for ok_to_place_ship_at by the deadline of session 7 assignment
    f = [(0, 0, True, 4, {}),
         (2, 0, True, 3, {}),
         (2, 4, True, 3, {}),
         (4, 0, True, 2, {}),
         (4, 3, True, 2, {}),
         (4, 6, True, 2, {}),
         (6, 0, True, 1, {}),
         (6, 2, True, 1, {}),
         (6, 4, True, 1, {})]
    assert type(ok_to_place_ship_at(6, 6, True, 1, f))==True
    #provide at least five tests in total for ok_to_place_ship_at by the project submission deadline

def test_place_ship_at1():
    #add at least one test for place_ship_at by the deadline of session 7 assignment
    f = [(0, 0, True, 4, {}),
         (2, 0, True, 3, {}),
         (2, 4, True, 3, {}),
         (4, 0, True, 2, {}),
         (4, 3, True, 2, {}),
         (4, 6, True, 2, {}),
         (6, 0, True, 1, {}),
         (6, 2, True, 1, {}),
         (6, 4, True, 1, {})]
    f_1 = [(0, 0, True, 4, {}),
           (2, 0, True, 3, {}),
           (2, 4, True, 3, {}),
           (4, 0, True, 2, {}),
           (4, 3, True, 2, {}),
           (4, 6, True, 2, {}),
           (6, 0, True, 1, {}),
           (6, 2, True, 1, {}),
           (6, 4, True, 1, {}),
           (6, 6, True, 1, {})]
    assert place_ship_at(6, 0, True, 1, f)==f_1
    #provide at least five tests in total for place_ship_at by the project submission deadline

def test_check_if_hits1():
    #add at least one test for check_if_hits by the deadline of session 7 assignment
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
    
