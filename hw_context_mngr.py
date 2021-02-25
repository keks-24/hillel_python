import os
from contextlib import suppress


class do_cd:
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


with do_cd('/files1', FileNotFoundError) as cd:
	print(os.getcwd())
print(os.getcwd())



