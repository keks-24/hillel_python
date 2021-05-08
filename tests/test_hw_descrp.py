import pytest
from hw_2 import rock_scissors_paper_game, encrypt_func

# просто попробовал как работает параметризированный тест
# @pytest.mark.parametrize("item,expected", [("rock", "YOU WIN!"),
# 										   ("paper", "YOU WIN!"),
# 										   ("scissors", "YOU WIN!"),
# 										   ("hfkds","incorrect item")])
# def test_rock_scissors_paper_game(item, expected):
# 	assert rock_scissors_paper_game(item) == expected


def test_encrypt_func():
	assert encrypt_func('aeiou') == '32210'
	assert encrypt_func('bad') == 'd0b'
	assert encrypt_func('bad') == 'd0b'


