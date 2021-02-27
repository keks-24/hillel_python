import os
import time
from contextlib import suppress, ContextDecorator


class do_cd(ContextDecorator):
	"""context manager for 1 and 2 task sametimes"""
	def __init__(self, path, *exc):
		self.path = path
		self.exc = exc

	def __enter__(self):
		self.current_cwd = os.getcwd()
		try:
			os.chdir(self.current_cwd + self.path)
		except self.exc:
			suppress(self.exc)
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		if self.exc:
			os.chdir(self.current_cwd)
		return self


with do_cd('/files', FileNotFoundError) as cd:
	print(os.getcwd())
print(os.getcwd())

# ------------- TASK 2


@do_cd('/file', FileNotFoundError)
def some_func():
	print('i am function path')
	print(os.getcwd())


some_func()


# ------------- TASK 3


class count_func_execution:
	"""context manager that count func execution time"""
	def __init__(self):
		self.func_time = None

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


with count_func_execution() as f:
	some_func()
print(f'function time execution is: {f.func_time}')