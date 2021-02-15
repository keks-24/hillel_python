import os
import pprint

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
	"""function that find surnames which started on 'C' and 'K'"""
	path_file = f'{OS_PATH}/files/2.txt'
	lines = open_file(path_file)
	result = []
	for line in lines:
		split_line = line.split(' ')
		if split_line[1].startswith("C") or split_line[1].startswith("K"):
			result.append(line)
	write_file(f'{OS_PATH}/files/new_phone_file.txt', result)


# phone_review()


# ============================ TASK 3

def right_align_data():
	"""function that add whitespaces foreach line"""
	path_file = f'{OS_PATH}/files/3.txt'
	lines = open_file(path_file)
	result = []
	for line in lines:
		new_line = line.rjust(120)
		result.append(new_line)
	write_file(path_file, result)


# right_align_data()


# ============================ TASK 4


def count_most_finded_elem(value):
	counter = 1
	elem = value[0]
	for unique_elem in set(value):  # get unique list
		count_ = value.count(unique_elem)  # count same elements for each unique elem from set
		if count_ > counter:
			counter, elem = count_, unique_elem
	return elem


def filter_ip_file():
	path_file = f'{OS_PATH}/files/4.txt'
	lines = open_file(path_file)
	filtred_ip = dict()  # dict for store result
	for line in lines:
		site_ip, visit_time, week_day = (line.split(' '))
		hours_time = visit_time[0:2]
		if site_ip in filtred_ip:  # check ip in dict if find , add info to same ip
			filtred_ip[site_ip][0].append(hours_time)
			filtred_ip[site_ip][1].append(week_day)
		else:  # add first time find ip
			filtred_ip[site_ip] = [[hours_time], [week_day]]
	result = list()
	max_same_time = []
	for ip, elem in filtred_ip.items():
		res_time, res_day = count_most_finded_elem(elem[0]), count_most_finded_elem(elem[1])
		result.append([ip, len(elem[0]), res_day])
		max_same_time.append(count_most_finded_elem(res_time))
	pprint.pprint(result)
	pprint.pprint(max_same_time)


filter_ip_file()
