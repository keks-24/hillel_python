import os
from contextlib import suppress


class do_cd:
	current_cwd = os.getcwd()

	def __init__(self, path, *suppressed):
		self.path = path
		self.suppressed = suppressed

	def __enter__(self):
		self.new_dir = os.getcwd()
		os.chdir(os.getcwd() + self.path)

	def __exit__(self, exc_type, exc_val, exc_tb):
		print(exc_type)
		print(exc_val)
		print(exc_tb)
		os.chdir(self.current_cwd)
		return exc_type is not None and issubclass(exc_type, self.suppressed)


with do_cd('/some_unknown_dir', FileNotFoundError) as cd:
	print(os.getcwd())

