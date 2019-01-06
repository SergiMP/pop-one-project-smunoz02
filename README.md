# pop-one-project-smunoz02

Project for POP I assignment.

I have been working regularly on the project for the past three weeks whenever work and family commitments allowed.
When pushing the code to GITHUB I realized that my previous GITHUB account has been linked to the one for the project.
I have seen in the forum that this can happen and that is ok, but in case there is an issue please let me know.

The first part of the assignment is completed and passes all the test.

For the second part where we have to  implement a "Save status" we have created the options and the file with the information stored, but we haven't managed to upload the status to the new game.

We thought of creating a saved_game() function, where we would load the main variables and copy the main loop of the start() function.

```def start_saved_game():

  load board
  load users_side
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
 ```
However we couldn't fix the code dependencies and the different errors we had so we will have to keep working on this file after the deadline for this project has lapsed.
