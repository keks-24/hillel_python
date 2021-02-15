# ----------- Task 1

from functools import wraps
import random


def check_reminder(func):
	"""decorator check remainder of division"""
	@wraps(func)
	def inner(*args):
		result = 100 % func(*args)
		print('we are ok' if not result else f"Bad news guys, we got {result}")
	return inner


@check_reminder
def generate_number():
	"""This function will generate and return some number"""
	value = random.randint(0, 100)
	print(value)
	return value


generate_number()


# ----------- Task 2


def check_variable_type(func):
	"""decorator that check if arg is int"""

	@wraps(func)
	def inner(arg):
		try:
			if isinstance(arg, int):
				func(arg)
			if isinstance(arg, str):
				print("string type is not supported")
		except ValueError: # i tried did it task by using raise, but i dont like when code crush, so decided use try except
			print("some other type of data") # so i think that message should be smth like "value wasnt int"
	return inner


@check_variable_type
def very_important_function(input_value):
	"""simple func that adds values"""
	print(input_value + input_value)
	return input_value


very_important_function('test string')
very_important_function(2)


# ----------- Task 3


def check_in_cache(func):
	"""decorator that count calls of function, count calls from cache, and store result"""
	cache = {}
	def inner(*args):
		if args not in cache.keys():
			cache[args] = {
				"result":str(func(*args))
			}
			inner.func_call_count +=1
			print(f"Function executed with counter = {inner.func_call_count}, function result = {cache[args]['result']}")
		else:
			inner.func_cache_used += 1
			print(f"Used cache with counter = {inner.func_cache_used}")

	inner.func_call_count = 0
	inner.func_cache_used = 0
	return inner


@check_in_cache
def plus_func(input_value):
	"""simple function that do multiplication"""
	result = input_value*input_value
	return result


plus_func(2)
plus_func(2)
plus_func(2)
plus_func(2)
plus_func(3)
plus_func(3)
plus_func(4)
plus_func(4)
print(plus_func.func_cache_used)
print(plus_func.func_call_count)
