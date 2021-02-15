import os

OS_PATH = os.getcwd()


def open_file(path):
	"""function that open and read whole file"""
	with open(path, 'r') as fr:
		lines = [line.rstrip() for line in fr]
	return lines


def write_file(path, result):
	"""function that write result to file"""
	with open(path, 'w') as fw:
		fw.write('\n'.join(result) + '\n')


"""
reveal cancel as appetite fountain creep conglomerate
building mathematics price jelly arise manufacture
rich staircase iron bait coverage deserve curve deter rich staircase iron bait coverage deserve curve deter
neck mill bond sailor fee price
"""


def count_words_with_condition(line):
	"""function that find needed words in lines"""
	amount_words_to_del = []
	for word in line.split(' '):
		if 3 <= len(word) <= 5:
			amount_words_to_del.append(word)
	if not len(amount_words_to_del) % 2 == 0:
		return amount_words_to_del[0:-1]
	return amount_words_to_del


def delete_words_from_file():
	"""function that erase words from line"""
	path_file = f'{OS_PATH}/files/1.txt'

	lines = open_file(path_file)

	result = []
	for line in lines:
		new_line = []
		for word in line.split(' '):
			if word not in count_words_with_condition(line):
				new_line.append(word)
		final_line = ' '.join(new_line)
		print(final_line)
		result.append(final_line)
	write_file(path_file, result)


# delete_words_from_file()


# ============================ TASK 2


def phone_review():
	path_file = f'{OS_PATH}/files/2.txt'
	lines = open_file(path_file)
	result = []
	for line in lines:
		split_line = line.split(' ')
		if split_line[1].startswith("C") or split_line[1].startswith("K"):
			result.append(line)
	write_file(f'{OS_PATH}/files/new_phone_file.txt', result)


# phone_review()


