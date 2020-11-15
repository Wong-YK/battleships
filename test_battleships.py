import pytest
from battleships import *

def test_is_sunk1():
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(s)
    #add at least four more tests for is_sunk by the project submission deadline

def test_ship_type1():
    #add at least one test for ship_type by the deadline of session 7 assignment
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert shiptype(s)=="cruiser"
    #provide at least five tests in total for ship_type by the project submission deadline

def test_is_open_sea1():
    #add at least one test for open_sea by the deadline of session 7 assignment
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
    assert is_open_sea(0, 0, f)==False
    #provide at least five tests in total for open_sea by the project submission deadline

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
    
