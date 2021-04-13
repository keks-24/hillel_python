import pytest
import hw_descriptors.hw_descrp
from hw_2 import rock_scissors_paper_game, encrypt_func
# conftest


@pytest.mark.parametrize("item,expected", [("rock", "YOU WIN!"),
										   ("paper", "YOU WIN!"),
										   ("scissors", "YOU WIN!"),
										   ("hfkds","incorrect item")])
def test_rock_scissors_paper_game(item, expected):
	assert rock_scissors_paper_game(item) == expected


def encrypt_func(input_string):
	"""function that encrypts a given input by two steps, reverse word and replace in it letters"""

	reverse_input_string = reversed(input_string)
	cart_dict = {"a":0, "e":1, "i":2, "o":2, "u": 3}
	final_word = str()
	for letter in reverse_input_string:
		if letter in cart_dict.keys():
			final_word += str(cart_dict[letter])
		else:
			final_word += str(letter)
	return final_word

def test_encrypt_func():
	assert encrypt_func('aeiou') == '32210'
	assert encrypt_func('bad') == 'd0b'
	assert encrypt_func('bad') == 'bad'


