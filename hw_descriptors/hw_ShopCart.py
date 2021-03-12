# Задача4
# Необходимо создать модели работы со складскими запасами товаров и процесса оформления заказа этих товаров.
# Cписок требований:
# 1) Создайте товар с такими свойствами, как имя(name), подробные сведения(description or details),
# количество на складе(quantity), доступность(availability), цена(price).
# Добавить к этой задаче дескриптор для аттрибута цена.
# При назначении цены товара будет автоматически добавлен НДС 20%
# При получении цены товара, цена возврщается уже с учетом НДС

# 2) Добавить товар на склад
# 3) Удалить товар со склада
# 4) Распечатать остаток товара по его имени
# 5) Распечатать остаток всех товаров
# 6) Товар может принадлежать к категории
# 7) Распечатать список товаров с заданной категорией


# 8) Корзина для покупок, в которой может быть много товаров с общей ценой.
# 9) Добавить товары в корзину (вы не можете добавлять товары, если их нет в наличии)
# 10) Распечатать элементы корзины покупок с ценой и общей суммой
# 11) Оформить заказ и распечатать детали заказа по его номеру
# 12) Позиция заказа, созданная после оформления заказа пользователем.
# Он будет иметь идентификатор заказа(order_id), дату покупки(date_purchased), товары(items), количество(quantity)
# 13) После оформления заказа количество товара уменьшается на количество товаров из заказа.


class PriceDescriptor:
	"""descriptor that add NDS to price"""
	def __set__(self, instance, value):
		if value > 0:
			instance._price = round(value * 1.2, 2)
		else:
			raise ValueError('Not valid price')

	def __get__(self, instance, owner):
		return instance._price


class Product:
	"""Class that represent product"""
	price = PriceDescriptor()

	def __init__(self, name, description='no description', quantity=None, availability=False, price=None):
		self._name = str(name).capitalize()
		self._description = description
		self._quantity = quantity
		self._availability = availability
		self._price = price

	@property
	def name(self):
		return self._name

	@property
	def description(self):
		return self._description

	@description.setter
	def description(self, new_description):
		self._description = new_description

	@property
	def quantity(self):
		return self._quantity

	@quantity.setter
	def quantity(self, new_quantity):
		if new_quantity >= 0:
			self._quantity = new_quantity
		else:
			raise ValueError('Not valid quantity')

	@property
	def availability(self):
		return self._availability

	@availability.setter
	def availability(self, new_availability):
		if self._availability is None:
			self._availability = new_availability

	def __str__(self):
		return f'Product name - {self._name}, description - {self._description}, quantity - {self._quantity}, availability - {self._availability}, price - {self._price}'


class Storage:
	"""Class that store all products"""
	storage = {}

	def add_to_storage(self, product: Product, category):
		"""add product to storage"""

		self.storage[product._name] = {
			'description': product._description,
			'quantity': product._quantity,
			'availability': product._availability,
			'price': product._price,
			'category': category
		}
		print(f'Product - {product._name} add on storage')

	def get_product(self, name):
		"""get product by name"""

		if name in self.storage.keys():
			return self.storage[name]
		else:
			print('No such product')

	def get_product_quantity(self, name):
		"""get product quantity by name"""
		return f"total quantity of {name} is {self.storage[name]['quantity']}"

	def get_all_products_quantity(self):
		result = {}
		for key in self.storage.keys():
			result[key] = self.storage[key]['quantity']
		return result

	def remove_product(self, name):
		if name in self.storage.keys():
			del self.storage[name]
		else:
			print('No such product')

	def get_product_by_category(self, category):
		result = []
		for key in self.storage.keys():
			if category == self.storage[key]['category']:
				result.append(key)
		return result

	def __str__(self):
		return f'{self.storage}'


class Basket:
	"""class that represent shop basket"""


	def __str__(self):
		return f''

bread = Product('bread', 'tasty fresh baked', True)
bread.quantity = 14
bread.price = 125


milk = Product('milk', 'fresh maked from farm', True)
milk.quantity = 200
milk.price = 15.99


storage = Storage()
storage.add_to_storage(bread, category='food')
storage.add_to_storage(milk, category='food')
print(storage)
print(storage.get_product('Bread'))
print(storage.get_product_quantity('Bread'))
print(storage.get_product('Milk'))
# storage.remove_product('Bread')
# storage.remove_product('Bread')
# storage.get_product('Bread')
print(storage.get_all_products_quantity())
print(storage.get_product_by_category('food'))



