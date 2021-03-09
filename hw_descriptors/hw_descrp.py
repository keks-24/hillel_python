class EmailDescriptor:
	def __init__(self):
		self._email = None

	def __get__(self, instance, owner):
		return self._email

	def __set__(self, instance, value):
		if '@' in value:
			self._email = value
		else:
			raise ValueError('Email not valid')


class MyClass:
	email = EmailDescriptor()


my_class = MyClass()
print(f"t is: {my_class.email}")
my_class.email = "validemail@gmail.com"
print(f"t is: {my_class.email}")
my_class.email = "novalidemail"
print(f"t is: {my_class.email}")