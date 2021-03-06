# 1) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key).keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ожидаемый результат: {1: 1, 2: 4, 3: 9 …}

# 2) Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа.
# =======================================================
# 3)Заменить в произвольной строке согласные буквы на гласные.

# =======================================================
# 4)Дан массив чисел.[10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
# 4.1) убрать из него повторяющиеся элементы
# 4.2) вывести 3 наибольших числа из исходного массива
# 4.3) вывести индекс минимального элемента массива
# 4.4) вывести исходный массив в обратном порядке

# =======================================================
# 5) Найти общие ключи в двух словарях:
# dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# dict_two = {'a': 6, 'b': 7, 'z': 20, 'x': 40}

# =======================================================
# 6)Дан массив из словарей
# data = [
#     {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
#     {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
#     {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
#     {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
#     {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
#     {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

# =======================================================
# 6.1) отсортировать массив из словарей по значению ключа 'age'
# 6.2) сгруппировать данные по значению ключа 'city'
# вывод должен быть такого вида :
# result = {
#    'Kiev': [
#       {'name': 'Viktor', 'age': 30 },
#       {'name': 'Andrey', 'age': 34}],
#
#    'Dnepr': [ {'name': 'Maksim', 'age': 20 },
#               {'name': 'Artem', 'age': 50}],
#    'Lviv': [ {'name': 'Vladimir', 'age': 32 },
#              {'name': 'Dmitriy', 'age': 21}]
# }
# =======================================================
# 7) У вас есть последовательность строк.Необходимо определить наиболее часто встречающуюся строку в последовательности.
# Например:

# def most_frequent(list_var):
#     # your code is here
#     return
#
# most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
# =======================================================
# 8) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.

# =======================================================
# 9) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.

# =======================================================
# 10) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три словаподряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.

import random
import operator
import copy
import pprint

string_separator = '-----------------------'
print(string_separator + ' 1')

# 1 =======================================================
def first_exercise():
	key = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	number_dict = dict({k: (k*k) for k in key})
	print(number_dict)


first_exercise()
print(string_separator + ' 2')


# 2 =======================================================
def second_exercise():
	number_list = list(i for i in range(101) if i % 2 == 0)
	print(number_list)


second_exercise()
print(string_separator + ' 3')


# 3 =======================================================
def third_exercise():
	vowels_letters = ['a', 'e', 'i', 'o', 'u', 'y']
	consonants_letters = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
	some_string = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'''
	for contant_letter in consonants_letters:
		for letter_in_string in some_string:
			if letter_in_string.lower() == contant_letter:
				some_string = some_string.replace(letter_in_string, random.choice(vowels_letters))
	print(some_string)


third_exercise()
print(string_separator + ' 4')


# 4 =======================================================
def fourth_exercise():
	numbers = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
	print(list(set(numbers))) # 4.1
	print(sorted(set(numbers))[-3:])
	print(numbers.index(min(numbers)))
	print(list(reversed(numbers)))


fourth_exercise()
print(string_separator + ' 5')


# 5 =======================================================
def five_exercise():
	dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
	dict_two = {'a': 6, 'b': 7, 'z': 20, 'x': 40}

	print(dict_one.keys() & dict_two.keys()) # much better thx for advice


five_exercise()
print(string_separator + ' 6')

# 6 =======================================================
def six_exercise():
	data = [{'name': 'Viktor', 'city': 'Kiev', 'age': 30},
			{'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
			{'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
			{'name': 'Andrey', 'city': 'Kiev', 'age': 34},
			{'name': 'Artem', 'city': 'Dnepr', 'age': 50},
			{'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]
	print(sorted(data, key=operator.itemgetter('age')))

	print(string_separator + "6.2 =)")
	city_sorted = sorted(data, key=operator.itemgetter('city'))
	copy_city_sorted = copy.deepcopy(city_sorted)
	result = {}
	for element in city_sorted:
		current_city = element['city']
		persons_list = []
		if current_city not in result.keys():
			for person in copy_city_sorted:
				if 'city' in person.keys():
					if current_city == person['city']:
						person.pop("city")
						persons_list.append(person)
			result[current_city] = persons_list
		else:
			pass

	pprint.pprint(result)


six_exercise()
print(string_separator + ' 7')


# 7 =======================================================
def seven_exercise(list_var):
	finded_word = ''
	main_count = 0
	for element in list_var:
		count = 0
		for n in list_var:
			if element == n:
				count += 1
		if count > main_count:
			finded_word = element
			main_count = count

	print(finded_word)
	print(max(set(list_var), key=list_var.count))
	return finded_word


seven_exercise(['a', 'w', 'w', 'w', 'w', 'a', 'bi', 'bi', 'bi', 'w', 's'])
print(string_separator + ' 8')


# 8 =======================================================
def eight_exercise(given_value):
	result = 1
	if len(str(given_value)) > 1:
		for n in str(given_value):
			if int(n) > 0:
				result = result * int(n)
	else:
		result = int(given_value)

	print(result)


eight_exercise(1203405)
print(string_separator + ' 9')

# 9 =======================================================
def nine_exercise(array, n):
	try:
		num = array[n]
		result = num ** n
	except IndexError as e:
		# print(e)
		result = '-1'

	print(result)


nine_exercise([1, 2, 3, 4, 5], 8)
print(string_separator + ' 10')


# 10 =======================================================
def ten_exercise(given_string):
	split_string = given_string.split(' ')
	count = 0
	for element in split_string:
		if not element.isdigit():
			count += 1
		else:
			count = 0
		if count == 3:
			print("find three words in row ")
			break
	if count < 3:
		print("not found three words in row ")


ten_exercise('fsd 21 gjghj 5 ghjgh hgjgh 5 ghjghj 2')
print(string_separator + ' the end')