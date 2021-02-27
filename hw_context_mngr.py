import os
import time
from contextlib import suppress, contextmanager


class do_cd:
	"""context manager for 1 and 2 task sametimes"""
	def __init__(self, path, *exc):
		self.path = path
		self.exc = exc

	def __enter__(self):
		self.current_cwd = os.getcwd()
		try:
			os.chdir(self.current_cwd + self.path)
		except self.exc:
			pass
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		os.chdir(self.current_cwd)


with do_cd('/files', FileNotFoundError) as cd:
	print(os.getcwd())
print(os.getcwd())

# ------------- TASK 2


@contextmanager
def context_manager_cd(path, *exc):
	current_cwd = os.getcwd()
	try:
		os.chdir(current_cwd + path)
	except exc:
		suppress(exc)
	print(os.getcwd())
	yield

	os.chdir(current_cwd)
	print(os.getcwd())


with context_manager_cd('/file1s', FileNotFoundError) as f:
	print('i am print text inside context manager')


# ------------- TASK 3


class count_func_execution:
	"""context manager that count func execution time"""
	def __enter__(self):
		self.start_time = time.time()
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.func_time = time.time() - self.start_time
		return self.func_time


def some_func():
	"""This is example function with long time execution"""
	n = 0
	b = 0
	while n <= 10000000:
		b += 10
		n += 1
	return b


with count_func_execution() as ft:
	some_func()
print(f'function time execution is: {ft.func_time}')