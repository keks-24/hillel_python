import os

OS_PATH = os.getcwd()


"""
reveal cancel as appetite fountain creep conglomerate
building mathematics price jelly arise manufacture
rich staircase iron bait coverage deserve curve deter rich staircase iron bait coverage deserve curve deter
neck mill bond sailor fee price
"""


def count_words_with_condition(line):
	amount_words_to_del = []
	for word in line.split(' '):
		if 3 <= len(word) <= 5:
			amount_words_to_del.append(word)
	if not len(amount_words_to_del) % 2 == 0:
		return amount_words_to_del[0:-1]
	return amount_words_to_del


def delete_words_from_file():
	path_file = f'{OS_PATH}/files/1.txt'

	with open(path_file, 'r') as fr:
		lines = fr.readlines()

	result = []
	for line in lines:
		new_line = []
		for word in line.rstrip().split(' '):
			if word not in count_words_with_condition(line.rstrip()):
				new_line.append(word)
		final_line = ' '.join(new_line)
		print(final_line)
		result.append(final_line)
	with open(path_file, 'w') as fw:
		fw.write('\n'.join(result) + '\n')


delete_words_from_file()
