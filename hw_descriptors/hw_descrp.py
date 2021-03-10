import re


class EmailDescriptor:
	def __init__(self):
		self._email = None

	def __get__(self, instance, owner):
		return self._email

	def __set__(self, instance, value):
		if re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', value):
			self._email = value
		else:
			raise ValueError('Email not valid')


class EmailClass:
	email = EmailDescriptor()

#
# email_class = EmailClass()
# email_class.email = "validemail@gmail.com"
# print(f"email is: {email_class.email}")
# email_class.email = "novalidemail@ ukr.net"
# print(f"email is: {email_class.email}")


# --------------- task 2
i = 0


class Singleton(type):
	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = cls
			global i
		return cls


class MyClass(metaclass=Singleton):
	pass


# c = MyClass()
# b = MyClass()
# assert id(c) == id(b)


# --------------- task 3

class IngegerField:
	class_state = {}

	def __init__(self):
		self.number = None

	def __get__(self, instance, owner):
		return self.class_state[instance]

	def __set__(self, instance, value):
		self.number = value
		self.class_state[instance] = self.number


class Data:
	number = IngegerField()


data_row = Data()
new_data_row = Data()

data_row.number = 5
new_data_row.number = 10

assert data_row.number != new_data_row.number
