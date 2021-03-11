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
	def __set__(self, instance, value):
		if value > 0:
			instance._price = round(value * 1.2, 2)
		else:
			raise ValueError('Not valid price')

	def __get__(self, instance, owner):
		return instance._price


class Product:
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
	storage = {}

	def __init__(self, product, category):
		self.product_name = product._name
		Storage.storage[product._name] = {
			'description': product._description,
			'quantity': product._quantity,
			'availability': product._availability,
			'price': product._price,
			'category': category
		}

	def __str__(self):
		return f'Product - {self.product_name} add on storage'


bread = Product('bread', 'tasty fresh baked', True)
bread.quantity = 14
bread.price = 125
print(bread)

storage = Storage(bread, category='food')
print(storage)


