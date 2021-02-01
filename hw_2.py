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

	WIN_STR = 'YOU WIN!'
	LOSE_STR = 'YOU LOSE!'
	DRAW_STR = 'DRAW!'

	items_list = {"rock" : 2, "scissors" : 1, "paper" : 0}
	if user_item in items_list.keys():
		user_value = items_list[f"{user_item}"]
		choosen_item_name, choosen_item_value = random.choices(list(items_list.items()))[0]
		print(choosen_item_name)
		if user_value == choosen_item_value:
			return DRAW_STR
		if user_value == 2 and choosen_item_value == 0:
			return LOSE_STR
		if user_value == 2 and choosen_item_value == 1:
			return WIN_STR
		if user_value == 1 and choosen_item_value == 0:
			return WIN_STR
		if user_value == 1 and choosen_item_value == 2:
			return LOSE_STR
		if user_value == 0 and choosen_item_value == 2:
			return WIN_STR
		if user_value == 0 and choosen_item_value == 1:
			return LOSE_STR
	else:
		return "incorrect item"


print(rock_scissors_paper_game(input("Type: paper or scissors or rock ")))


def survive_without_TP(input_data):
	"""This function calculate enough TP for survive on quarantine or not"""

	TP_USAGE_PER_DAY = 57
	QUARANTINE_LENGTH = 14
	AVG_TP_SIZE = 500

	count_people = input_data["people"]
	count_tp = input_data["tp"]
	if count_people * TP_USAGE_PER_DAY * QUARANTINE_LENGTH <= count_tp * AVG_TP_SIZE:
		print("I guess this people will survive")
	else:
		print("Not enough tp, ALERT NEED MORE TP")


survive_without_TP({"people":6, "tp":10})


def encrypt_func(input_string):
	"""function that encrypts a given input"""

	reverse_input_string = list(reversed(input_string))
	cart_dict = {"a":0, "e":1, "i":2, "o":2, "u": 3}
	final_word = str()
	for letter in reverse_input_string:
		if letter in cart_dict.keys():
			final_word += str(cart_dict[letter])
		else:
			final_word += str(letter)
	return final_word


print(encrypt_func(input("Print some word: ")))