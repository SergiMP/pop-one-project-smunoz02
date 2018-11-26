import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    #eventually add at least two more test cases

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M
    #eventually add some board2 and at least 3 tests with it

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    #eventually add at least one more test with another board

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    assert string_to_location('A1') == (0,0)
    #eventually add at least one more exception test and two more
    #test with correct inputs

def test_location_to_string():
    string = location_to_string(location)
    s0 = ("a","b","c","e")
    s1 = (range(1,6))
    assert (string[0] in s0) and (string[1] in s1)
    # Replace with tests

def test_at():
    result = at(location)
    assert isinstance(result,str)
    # Replace with tests

def test_all_locations():
    locations = all_locations(location)
    assert len(location) == 25
    # Replace with tests

def test_adjacent_location():
    y = adjacent_location(location)
    assert y == (board1[0],board1[1])
    # Replace with tests

def test_is_legal_move_by_musketeer():
    legal_moves = ()
    assert is_legal_move_by_musketeer(move) in legal_moves
    # Replace with tests

def test_is_legal_move_by_enemy():
    legal_moves = ()
    assert is_legal_move_by_enemy(move) in legal_moves
    # Replace with tests

def test_is_legal_move():
    legal_moves = {"M": () ,"R": () }
    assert legal_move(location,direction) in legal_moves["M"]
    # Replace with tests

def test_can_move_piece_at():
    locations = [()]
    assert can_move_piece_at(location) in locations    
    # Replace with tests

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    directions = []
    assert possible_moves_from(location) in directions
    # Replace with tests

def test_is_legal_location():
    legal_locations = ()
    assert legal_location(location) in legal_locations
    # Replace with tests

def test_is_within_board():
    boundaries = ()
    assert is_within_board(location, direction) in boundaries
    # Replace with tests

def test_all_possible_moves_for():
    assert isinstance(all_possible_moves_for(player),list)
    # Replace with tests

def test_make_move():
    previous_position = location
    assert previous_position != make_move(location, direction)
    # Replace with tests

def test_choose_computer_move():
    assert None != choose_computer_move(who)
    # Replace with tests; should work for both 'M' and 'R'

def test_is_enemy_win():
    assert isinstance(is_enemy_win(),bool)
    # Replace with tests
