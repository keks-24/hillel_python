# 1) Write a function that emulates the game "rock, scissors, paper"
# At the entrance, your function accepts your version printed from the console, the computer makes a decision randomly.

# 2)Try to imagine a world in which you might have to stay home for (Corona virus) 14 days at any given time.
# Do you have enough toilet paper(TP) to make it through?
# Although the number of squares per roll of TP varies significantly, we'll assume each roll has 500 sheets,
# and the average person uses 57 sheets per day.

# Create a function that will receive a dictionary with two key/values:
# "people" ⁠— Number of people in the household.
# "tp" ⁠— Number of rolls.
# Return a statement telling the user if they need to buy more TP!

# 3) Make a function that encrypts a given input with these steps:
# Input: "apple"
# Step 1: Reverse the input: "elppa"
# Step 2: Replace all vowels using the following chart:
# a => 0
# e => 1
# i => 2
# o => 2
# u => 3
# # "1lpp0"
# Example:
# encrypt("banana") ➞ "0n0n0baca"
# encrypt("karaca") ➞ "0c0r0kaca"
# encrypt("burak") ➞ "k0r3baca"
# encrypt("alpaca") ➞ "0c0pl0aca"


# **4)Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns whether the game is a win
# for "X", "O", or a "Draw", where "X" and "O" represent themselves on the matrix, and "E" represents an empty spot.
# Example:
# tic_tac_toe([
#     ["X", "O", "X"],
#     ["O", "X", "O"],
#     ["O", "X", "X"]
# ]) ➞ "X"
#
# tic_tac_toe([
#     ["O", "O", "O"],
#     ["O", "X", "X"],
#     ["E", "X", "X"]
# ]) ➞ "O"
#
# tic_tac_toe([
#     ["X", "X", "O"],
#     ["O", "O", "X"],
#     ["X", "X", "O"]
# ]) ➞ "Draw"


import random

def rock_scissors_paper_game(user_item):
	"""function that emulates the game "rock, scissors, paper"""
	win_str = 'YOU WIN!'
	lose_str = 'YOU LOSE!'
	draw_str = 'DRAW!'

	items_list = {"rock" : 2, "scissors" : 1, "paper" : 0}
	if user_item in items_list.keys():
		user_value = items_list[f"{user_item}"]
		choosen_item_name, choosen_item_value = random.choices(list(items_list.items()))[0]
		print(choosen_item_name)
		if user_value == choosen_item_value:
			return draw_str
		if user_value == 2 and choosen_item_value == 0:
			return lose_str
		if user_value == 2 and choosen_item_value == 1:
			return win_str
		if user_value == 1 and choosen_item_value == 0:
			return win_str
		if user_value == 1 and choosen_item_value == 2:
			return lose_str
		if user_value == 0 and choosen_item_value == 2:
			return win_str
		if user_value == 0 and choosen_item_value == 1:
			return lose_str
	else:
		return "incorrect item"


print(rock_scissors_paper_game(input("Type: paper or scissors or rock ")))