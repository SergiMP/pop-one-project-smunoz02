# The Three Musketeers Game with Save Game Option three_musketeers_with_files.py

import random
import os
import pickle 


LEFT = 'LEFT'
RIGHT = 'RIGHT'
UP = 'UP'
DOWN = 'DOWN'
M = 'M'
R = 'R'
_ = '_'

def create_board():
	global board
	"""Creates the initial Three Musketeers board and makes it globally
	   available (That is, it doesn't have to be passed around as a
	   parameter.) 'M' represents a Musketeer, 'R' represents one of
	   Cardinal Richleau's men, and '-' denotes an empty space."""
	board = [ [R, R, R, R, M],
		  [R, R, R, R, R],
		  [R, R, M, R, R],
		  [R, R, R, R, R],
		  [M, R, R, R, R] ]
			  

def set_board(new_board):
	"""Replaces the global board with new_board."""
	global board
	board = new_board
	

def get_board():
	"""Just returns the board. Possibly useful for unit tests."""
	return board

def string_to_location(s):
	"""Given a two-character string (such as 'A5'), returns the designated
	   location as a 2-tuple (such as (0, 4)).
	   The function should raise ValueError exception if the input
	   is outside of the correct range (between 'A' and 'E' for s[0] and
	   between '1' and '5' for s[1]
	"""
	s = s.capitalize()
	rows = {'A':0,'B':1,'C':2,'D':3,'E':4}
	columns = {'1':0, '2':1, '3':2, '4':3, '5':4}
	if (s[0] in set(rows.keys()) and s[1] in set(columns.keys())):
		location_tuple = (rows[s[0]],columns[s[1]])
		return location_tuple
	else:  
		raise ValueError('The selected location is out of range.')

def location_to_string(location):
	"""Returns the string representation of a location.
	Similarly to the previous function, this function should raise
	ValueError exception if the input is outside of the correct range
	"""
	i,j = location 
	rows = {0:"A" ,1:"B" ,2:"C" ,3:"D" ,4:"E" }
	columns = {0:"1" ,1:"2" ,2:"3" ,3:"4" ,4:"5" }
	if i in set(rows.keys()) and j in set(columns.keys()):
		location_string = (rows[i],columns[j])
		return "".join(location_string)
	else:
		raise ValueError('The selected location is out of range.')


def at(location):
	"""Returns the contents of the board at the given location.
	You can assume that input will always be in correct range."""
	return board[location[0]][location[1]]

def all_locations():
	"""Returns a list of all 25 locations on the board."""
	all_locations = []
	for row in range(5):
		for column in range(5):
			all_locations.append((row,column))
	return all_locations

def adjacent_location(location, direction):
	"""Return the location next to the given one, in the given direction.
	   Does not check if the location returned is legal on a 5x5 board.
	   You can assume that input will always be in correct range."""
	direction = direction.upper()
	row_value = {UP: -1, DOWN: 1, LEFT: 0, RIGHT: 0}
	column_value ={UP: 0, DOWN: 0, LEFT: -1, RIGHT: 1}
	row, column = location
	return (row + row_value[direction],column + column_value[direction])

def is_legal_move_by_musketeer(location, direction):
	"""Tests if the Musketeer at the location can move in the direction.
	You can assume that input will always be in correct range. Raises
	ValueError exception if at(location) is not 'M'"""
	legal = (at(location) == 'M'and at(adjacent_location(location,direction)) == 'R' and adjacent_location(location,direction) in all_locations())
	if legal:
		return True 
	else: 
		raise ValueError("The Musketeer can't perform the selected move.")
		
		
def is_legal_move_by_enemy(location, direction):
	"""Tests if the enemy at the location can move in the direction.
	You can assume that input will always be in correct range. Raises
	ValueError exception if at(location) is not 'R'"""
	if at(location) == R and at(adjacent_location(location,direction)) == _:
		return "It is a legal move"
	else:
		raise ValueError("The enemy can't perform the selected move.")	


def is_legal_move(location, direction):
	"""Tests whether it is legal to move the piece at the location
	in the given direction.
	You can assume that input will always be in correct range."""
	if at(location) == M:
		return is_legal_move_by_musketeer(location, direction)
	elif at(location) == R:
		return is_legal_move_by_enemy(location, direction)
	else:
		return False
		
### USER DEFINED FUNCTIONS:
		
def location_moves(location):
	"""We have created this function so we could reuse its return value in other
	functions such can_move_piece_at() and possible_moves_from() and avoid code repetition.
	Returns a list containing both locations and legal moves from that location.
	"""
	directions = [UP, DOWN, LEFT, RIGHT]
	legal_moves = []
	for move in directions:
		try:
			if is_legal_move(location,move):
				legal_moves.append([location,move])
		except (ValueError, IndexError, TypeError) as e :
			pass
	return legal_moves
	
def locations_for_player(player):
	"""Returns a list of all the locations where the given players (M or R) are located"""
	locations = [location for location in all_locations() if at(location) == player]
	return locations
	
###
	


def can_move_piece_at(location):
	"""Tests whether the player at the location has at least one move available.
	You can assume that input will always be in correct range.
	"""
	return len(location_moves(location)) >= 1

			
def has_some_legal_move_somewhere(who):
	"""Tests whether a legal move exists for player "who" (which must
	be either 'M' or 'R'). Does not provide any information on where
	the legal move is.
	You can assume that input will always be in correct range.
	"""
	legal = [location for location in locations_for_player(who) if can_move_piece_at(location) == True]
	return len(legal) >= 1 


def possible_moves_from(location):
	"""Returns a list of directions ('left', etc.) in which it is legal
	   for the player at location to move. If there is no player at
	   location, returns the empty list, [].
	   You can assume that input will always be in correct range."""
	possible_moves = [move[1] for move in location_moves(location)]
	return possible_moves


def is_legal_location(location):
	"""Tests if the location is legal on a 5x5 board.
	You can assume that input will always be a pair of integers.
	
	By legal we understand "the location exist within the board" and by a
	"pair of integers" we understand the input is a tuple.
	
	Since we have listed all the possible locations in all_locations()
	we will just check if the selected location exist in all_locations()
	"""
	return location in all_locations()
	
	
def is_within_board(location, direction):
	"""Tests if the move stays within the boundaries of the board.
	You can assume that input will always be in correct range."""
	return adjacent_location(location,direction) in	 all_locations()


def all_possible_moves_for(player):
	"""Returns every possible move for the player ('M' or 'R') as a list
	   (location, direction) tuples.
	   You can assume that input will always be in correct range."""
	nested_list = [location_moves(location) for location in locations_for_player(player)]
	moves = [item for sublist in nested_list for item in sublist]
	return moves
	
	 
def make_move(location, direction):
	"""Moves the piece in location in the indicated direction.
	Doesn't check if the move is legal. You can assume that input will always
	be in correct range.
	we need to consider both old and new location. The old location has to be updated to
	"_" and the new one to the contents of at(old_location)"""
	global board
	old_location = location
	new_location = adjacent_location(location,direction)
	board[new_location[0]][new_location[1]] = at(old_location)
	board[old_location[0]][old_location[1]] = _
	

def choose_computer_move(who):
	"""The computer chooses a move for a Musketeer (who = 'M') or an
	   enemy (who = 'R') and returns it as the tuple (location, direction),
	   where a location is a (row, column) tuple as usual.
	   You can assume that input will always be in correct range."""
	selection = random.sample(all_possible_moves_for(who),1)
	move = ((selection[0][0],selection[0][1]))
	return move
	   

def is_enemy_win():
	"""Returns True if all 3 Musketeers are in the same row or column."""
	musketeers = locations_for_player(M)
	same_row = musketeers[0][0] == musketeers[1][0] == musketeers[2][0]
	same_column = musketeers[0][1] == musketeers[1][1] == musketeers[2][1]
	return same_row or same_column

#---------- Communicating with the user ----------
#----you do not need to modify code below unless you find a bug
#----a bug in it before you move to stage 3

def print_board():
	print("    1  2  3  4	5")
	print("------------------")
	ch = "A"
	for i in range(0, 5):
		print(ch, "|", end = " ")
		for j in range(0, 5):
			print(board[i][j] + " ", end = " ")
		print()
		ch = chr(ord(ch) + 1)
	print()

def print_instructions():
	print()
	print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.
If you wish to quit this amazing game please type Q.""")
	print()

def choose_users_side():
	"""Returns 'M' if user is playing Musketeers, 'R' otherwise."""
	user = ""
	while user != M and user != R:
		answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
		answer = answer.strip()
		if answer != "":
			user = answer.upper()[0]
	return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""
    directions = {'L': 'left', 'R': 'right', 'U': 'up', 'D': 'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if move in ("Q","QUIT"):
    	quit_game()
    if (len(move) >= 3
        and move[0] in 'ABCDE'
        and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        try:
            if is_legal_move(location, direction):
                return (location, direction)
        except ValueError:
            print('That movement is illegal, please enter a new Location and a new direction.')
            return get_users_move()
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
	"""Gets the Musketeer's move (from either the user or the computer)
	   and makes it."""
	if users_side in ("q","Q"):
		quit_game()
	if users_side == M:
		(location, direction) = get_users_move()
		if at(location) == M:
			if is_legal_move(location, direction):
				make_move(location, direction)
				describe_move("Musketeer", location, direction)
		else:
			print("You can't move there!")
			return move_musketeer(users_side)
	else: # Computer plays Musketeer
		(location, direction) = choose_computer_move(M)
		make_move(location, direction)
		describe_move("Musketeer", location, direction)

def move_enemy(users_side):
	"""Gets the enemy's move (from either the user or the computer)
	   and makes it."""
	if users_side == R:
		(location, direction) = get_users_move()
		if at(location) == R:
			if is_legal_move(location, direction):
				make_move(location, direction)
				describe_move("Enemy", location, direction)
		else:
			print("You can't move there!")
			return move_enemy(users_side)
	else: # Computer plays enemy
		(location, direction) = choose_computer_move(R)
		make_move(location, direction)
		describe_move("Enemy", location, direction)
		return board

def describe_move(who, location, direction):
	"""Prints a sentence describing the given move."""
	new_location = adjacent_location(location, direction)
	print(who, 'moves', direction, 'from',\
		  location_to_string(location), 'to',\
		  location_to_string(new_location) + ".\n")

	
def save_game():
	global board
	with open("saved_game.py","wb") as data:
		pickle.dump(board,data)
	quit()
	
def load_game():
	global board
	with open('saved_game.py','rb') as data:
		board = pickle.load(data)
	start()
	
def delete_start():
	os.remove("saved_game.py")
	start()
		
def is_file():
	return os.path.isfile('./saved_game.py')

def quit_game():
	user_choice = {1: save_game, 2: quit}
	print("Oh you are leaving us now?. We hope we'll see you soon.")
	print("Would you like to: ")
	print("1. Test if the student can create a 'save file'.")
	print("2. Test if the student can break other things than his leg, i.e a loop.")
	selection = input("Please select 1 to save the game or 2 to quit. ")
	try:
		choice = int(selection)
	except ValueError:
		print("Please focus and select a valid option. Try again... ")
		return selection
	if choice > 2:
		print("Please focus and select a valid option. Try again... ")
		return selection
	return user_choice[choice]()
	

def options():
    print("There is a saved game file available. Would you like to: ")
    print("1. Load that game, I was on fire... ")
    print("2. I need a fresh start in my life, delete it and load a new game. ")
    print("3. Ask me again next time, just start a new game for now. ")
    choice = input("Please select one option: 1 2 3  ")
    try:
        return int(choice)
    except ValueError:
        print('That is not a valid option. Please try again. ')
        return choice
        
def choice(choices):
	selected = {1: load_game ,2: delete_start ,3: start}
	return selected[choices]()

        
def start():
	"""Plays the Three Musketeers Game."""
	choice(options())
	global users_side
	users_side = choose_users_side()
	board = create_board()
	print_instructions()
	print_board()
	while True:
		if has_some_legal_move_somewhere(M):
			board = move_musketeer(users_side)
			print_board()
			if is_enemy_win():
				print("Cardinal Richleau's men win!")
				break
		else:
			print("The Musketeers win!")
			break
		if has_some_legal_move_somewhere(R):
			board = move_enemy(users_side)
			print_board()
		else:
			print("The Musketeers win!")
			break
			

if __name__ == '__main__':
	start()
