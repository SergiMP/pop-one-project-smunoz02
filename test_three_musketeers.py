import pytest
import copy
from three_musketeers  import *

LEFT = 'LEFT'
RIGHT = 'RIGHT'
UP = 'UP'
DOWN = 'DOWN'
M = 'M'
R = 'R'
_ = '_'

board = [ [R, R, R, R, M],
		  [R, R, R, R, R],
		  [R, R, M, R, R],
		  [R, R, R, R, R],
		  [M, R, R, R, R] ]

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]
            
board2 =  [ [_, R, _, M, _],
            [_, _, R, M, _],
            [_, R, _, R, _],
            [_, R, M, _, R],
            [_, _, _, R, _] ]  
            
board3 =  [ [_, R, _, M, _],
            [_, _, R, M, _],
            [_, R, _, M, _],
            [_, R, R, _, R],
            [_, _, _, R, _] ] 

board4 =  [ [_, R, _, _, _],
            [_, _, M, M, M],
            [_, R, _, R, _],
            [_, R, R, _, R],
            [_, _, _, R, _] ] 

board5 =  [ [_, _, _, _, _],
            [M, _, _, M, M],
            [_, _, _, _, _],
            [_, _, _, _, _],
            [_, _, _, _, _] ] 

def test_create_board():
    '''Test for appropiated size of the board and appropiated initial values.'''
    assert len(board) == 5
    for array in board:
        assert len(array) == 5
    assert board[0] == [R,R,R,R,M]
    assert board[1] == [R,R,R,R,R]
    assert board[2] == [R,R,M,R,R]
    assert board[3] == [R,R,R,R,R]
    assert board[4] == [M,R,R,R,R]
    
def test_set_board():
    '''Test that set board replaces the current board and returns the correct object'''
    first_board = get_board(board1)
    assert first_board[0][0] == _
    assert first_board[0][3] == M
    assert first_board[2][1] == R
    second_board = set_board(board2)
    assert second_board[0][0] == _
    assert second_board[0][3] == M
    assert second_board[2][1] == R
    assert first_board != second_board

def test_get_board():
    '''Test that the functions return an appropiated object i.e type and length'''
    board = get_board(board1)
    assert len(board) == 5
    assert board == board1 and board != board2
    assert isinstance(board,list)
    assert type(board) != str
    board_two = get_board(board2)
    assert board != board_two
    
def test_string_to_location():
    '''Test error exceptions and return values for correct input.'''
    with pytest.raises(ValueError):
        string_to_location('X3')
        string_to_location("I love you madly,deeply :)")
        string_to_location(A4)
    assert string_to_location('A1') == (0,0)
    assert string_to_location("B2") == (1,1)
    assert string_to_location("d3") == (3,2)
    
def test_location_to_string():
    '''Test error exceptions and return value for appropiated input.'''
    with pytest.raises(ValueError):
        location_to_string(("A","1"))
        location_to_string(('10','0'))
        location_to_string((10,0))
    assert location_to_string((0,0)) == "A1"
    assert location_to_string((1,0)) != "A1"
    assert location_to_string((1,0)) == "B1"

def test_at():
    '''Test that the contents of the board are returned'''
    set_board(board)
    assert at((0,0)) != M
    assert at((1,0)) == R
    assert at((0,4)) == M
    set_board(board2)
    assert at((0,0)) == _
    assert at((1,0)) != R
    assert at((0,0)) != M
    assert type(at((0,0))) == str

def test_all_locations():
    '''Test that the returned object has the appropiated size, the range of values for the tuples 
    and that is a list. '''
    assert len(all_locations()) == 25
    assert isinstance(all_locations(),list)
    assert type(all_locations()[0]) == tuple
    assert all_locations()[0] == (0,0)
    assert all_locations()[-1] == (4,4)
    
def test_adjacent_location():
    '''As indicated the input is assumed to be correct. We test that the correct adjacent
    location is returned by the function.(As indicated on the exercice we assumed a correct input.)'''
    assert adjacent_location((0,0),DOWN) == (1,0)
    assert adjacent_location((0,0),RIGHT) == (0,1)
    assert adjacent_location((4,2),UP) == (3,2)
    assert adjacent_location((4,2),LEFT) == (4,1)
    assert adjacent_location((4,2),LEFT) != (4,2)
    assert adjacent_location((0,0),RIGHT) != (0,0)
    assert adjacent_location((4,2),UP) != (4,2)
    assert adjacent_location((4,2),LEFT) != (4,2)
    

def test_is_legal_move_by_musketeer():
    '''Test that both,the appropiated ValueError is raised and the legal move is returned.'''
    set_board(board)
    assert is_legal_move_by_musketeer((0,4),LEFT)
    assert is_legal_move_by_musketeer((0,4),DOWN)
    assert is_legal_move_by_musketeer((2,2),LEFT)
    assert is_legal_move_by_musketeer((2,2),DOWN)
    assert is_legal_move_by_musketeer((2,2),UP)
    assert is_legal_move_by_musketeer((2,2),RIGHT)
    assert is_legal_move_by_musketeer((4,0),UP)
    assert is_legal_move_by_musketeer((4,0),RIGHT)    
    with pytest.raises(ValueError):
        assert is_legal_move_by_musketeer((0,0),LEFT)
        assert is_legal_move_by_musketeer((4,4),RIGHT)
        assert is_legal_move_by_musketeer((1,0),LEFT)
    set_board(board2)
    with pytest.raises(ValueError):
        assert is_legal_move_by_musketeer((0,0),UP)
        assert is_legal_move_by_musketeer((4,4),DOWN)
        assert is_legal_move_by_musketeer((1,0),LEFT)
        assert is_legal_move_by_musketeer((1,4),RIGHT)
        assert is_legal_move_by_musketeer((0,3),RIGHT)    
    assert is_legal_move_by_musketeer((1,3),LEFT)
    assert is_legal_move_by_musketeer((3,2),LEFT)
    
def test_is_legal_move_by_enemy():
    '''Test that both,the appropiated ValueError is raised and the legal move is returned.'''
    set_board(board)
    with pytest.raises(ValueError):
        assert is_legal_move_by_enemy((0,0),RIGHT)
        assert is_legal_move_by_enemy((0,0),DOWN)
        assert is_legal_move_by_enemy((4,4),UP)
        assert is_legal_move_by_enemy((4,4),LEFT)
        assert is_legal_move_by_enemy((3,4),LEFT) 
    set_board(board2)
    with pytest.raises(ValueError):
        assert is_legal_move_by_enemy((0,3),RIGHT)
        assert is_legal_move_by_enemy((4,3),UP)
    assert is_legal_move_by_enemy((0,1),LEFT)
    assert is_legal_move_by_enemy((0,1),RIGHT)
    assert is_legal_move_by_enemy((1,2),UP)
    assert is_legal_move_by_enemy((1,2),DOWN)

def test_is_legal_move():
    '''Test that possible movements for both Musketeers and Enemies are evaluated correctly.'''
    set_board(board1)
    assert is_legal_move((2,2),UP)
    assert is_legal_move((2,2),LEFT)
    assert is_legal_move((2,2),RIGHT)
    with pytest.raises(ValueError):
        assert is_legal_move((2,2),DOWN) 
        assert is_legal_move((1,3),RIGHT)
    set_board(board2)
    assert is_legal_move((0,1),LEFT)
    assert is_legal_move((1,2),UP)
    assert is_legal_move((1,3),LEFT)
    assert is_legal_move((3,2),LEFT)
    assert is_legal_move((0,0),RIGHT) == False
    assert is_legal_move((4,0),UP) == False 
    with pytest.raises(ValueError):
        assert is_legal_move((0,3),UP) 
        assert is_legal_move((0,3),LEFT)
        assert is_legal_move((3,2),RIGHT)
        
def test_location_moves():
    '''Test if the object returned is a list regardles of the input received.'''
    set_board(board)
    assert len(location_moves((2,2))) == 4
    assert len(location_moves((0,4))) == 2
    assert len(location_moves((4,0))) == 2
    set_board(board2)
    assert location_moves(('1','1')) == []
    assert isinstance(location_moves((0,0)),list)
    assert location_moves((-1,-1)) == []
    assert len(location_moves((0,0))) == 0
    with pytest.raises(NameError):
        assert location_moves((this_wont,work))
        assert location_moves((neither_will,this))
    
def test_locations_for_player():
    '''Test that the correct object is returned and that its values are correct.'''
    set_board(board)
    assert len(locations_for_player(M)) == 3
    assert len(locations_for_player(R)) == 22
    set_board(board2)
    assert isinstance(locations_for_player(M),list)
    assert isinstance(locations_for_player(M)[0],tuple)
    assert isinstance(locations_for_player(R)[0],tuple)
    assert len(locations_for_player(M)) == 3
    assert len(locations_for_player(R)) == 7
    
def test_can_move_piece_at():
    '''Test is there is still one movement available.'''
    set_board(board4)
    assert can_move_piece_at((1,3)) == True 
    assert can_move_piece_at((1,2)) == False 
    assert can_move_piece_at((1,4)) == False    
    set_board(board2)
    assert can_move_piece_at((0,3)) == False 
    assert can_move_piece_at((1,3)) == True 
    assert can_move_piece_at((3,3)) == False
    assert can_move_piece_at((4,3)) == True 
    assert can_move_piece_at((0,0)) == False

def test_has_some_legal_move_somewhere():
    '''Test whether the player can still make a movement by returning the appropiated object'''
    set_board(board5)
    assert has_some_legal_move_somewhere(M) == False
    assert has_some_legal_move_somewhere(R) == False
    assert type(has_some_legal_move_somewhere(R)) == bool
    set_board(board1)
    assert has_some_legal_move_somewhere(M) == True
    assert has_some_legal_move_somewhere(R) == True

def test_possible_moves_from():
    '''Test that the correct object is returned for different kinds of input in the correct range.'''
    set_board(board)
    assert len(possible_moves_from((0,4))) == 2 
    assert len(possible_moves_from((2,2))) == 4
    assert len(possible_moves_from((4,0))) == 2 
    assert len(possible_moves_from((0,0))) == 0
    assert len(possible_moves_from((0,2))) == 0
    assert len(possible_moves_from((2,1))) == 0
    set_board(board1)
    assert isinstance(possible_moves_from((0,0)),list)
    assert len(possible_moves_from((0,0))) == 0 
    assert len(possible_moves_from((1,3))) == 2

def test_is_legal_location():
    '''Test that a boolean object is returned and that it is correct for both legal/ilegal locations'''
    assert is_legal_location((0,0))
    assert is_legal_location((-1,4)) == False
    assert is_legal_location((4,0))
    assert is_legal_location((4,4))
    assert is_legal_location(("3",3)) == False
    assert is_legal_location(("3",3.0)) == False
    assert is_legal_location(("3","3.0")) == False

def test_is_within_board():
    '''Test if the movement is within the board range.'''
    assert is_within_board((0,3),UP) == False
    assert is_within_board((0,3),DOWN) == True
    assert is_within_board((0,3),RIGHT) == True
    assert is_within_board((0,0),UP) == False
    assert is_within_board((0,0),LEFT) == False
    
def test_all_possible_moves_for():
    '''Test that the appropiated object is returned for both players and that all possible
    movements are taken into account (uses board1)'''
    set_board(board)
    assert len(all_possible_moves_for((M))) == 8
    assert len(all_possible_moves_for((R))) == 0
    set_board(board1)
    assert isinstance(all_possible_moves_for((M)),list)
    assert len(all_possible_moves_for((M))) == 5
    assert len(all_possible_moves_for(R)) == 12 

def test_make_move():
    '''Test that both new and old locations are updated.(uses board1)'''
    original_board = copy.deepcopy(board1)
    modified_board = board1
    make_move((1,3),LEFT) == M
    assert original_board[1][3] != modified_board[1][3]
    assert modified_board[1][3] == _
    assert modified_board[1][2] == M

def test_choose_computer_move():
    '''Test that the correct object is returned, and also that its elements are correct.'''
    assert len(choose_computer_move(M)) == 2
    assert choose_computer_move(M) != choose_computer_move(R)
    assert isinstance(choose_computer_move(R),tuple)
    assert isinstance(choose_computer_move(M)[0],tuple)
    assert isinstance(choose_computer_move(R)[1],str)
    assert choose_computer_move(R)[0] in all_locations()
    assert is_legal_move(choose_computer_move(R)[0],choose_computer_move(R)[1])
    
    
def test_is_enemy_win():
    '''Test that the functions returns the correct object and works in both win/not win situations.'''
    set_board(board3)
    assert isinstance(is_enemy_win(),bool)
    assert is_enemy_win() == True
    set_board(board1)
    assert is_enemy_win() == False
    set_board(board)
    assert is_enemy_win() == False
    
     

