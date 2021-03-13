import datetime
from pprint import pprint


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

		if product.name not in self.storage.keys():
			self.storage[product.name] = {
				'description': product.description,
				'quantity': product.quantity,
				'availability': product.availability,
				'price': product.price,
				'category': category
			}
			print(f'Product - {product.name} add on storage')
		else:
			print(f'Product - {product.name} already at storage')

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
	order_id = 0
	order_position = 0
	orders_pull = {}

	def __init__(self):
		self.order_product_list = {}

	def add_product_to_basket(self, product: Product):
		if product.name not in self.order_product_list.keys():  # если товар еще не в корзине
			if Storage.storage[product.name]['availability'] is True and Storage.storage[product.name]['quantity'] > 0:
				self.order_product_list[product.name] = {
					'description': product.description,
					'price': product.price,
					'count': 1
				}
			else:
				print(f'Product {product.name} not available or out of sale')  # если товар недостуен по каой то причине
		else:
			self.order_product_list[product.name]['count'] += 1 # если продукт уже в корзине просто увеличиваем кол-во

	def get_basket_prod_and_price(self):  # элементы корзины покупок с ценой и общей суммой
		result_list = {}
		total_sum = 0
		_ = []
		for key in self.order_product_list.keys():
			total_sum += self.order_product_list[key]['price'] * self.order_product_list[key]['count']
			_.append(key)
			result_list = {
				'products': _,
				'total summ': total_sum
			}

		return result_list

	def checkout(self):
		"""finish order save order info and manage with storage quantity"""

		Basket.order_id += 1
		Basket.order_position += 1
		quantity = 0
		total_amount = 0

		for key in self.order_product_list:  # считаем кол-во товаров и считаем конечную цену
			quantity += self.order_product_list[key]['count']
			total_amount += self.order_product_list[key]['price'] * self.order_product_list[key]['count']
			if key in Storage.storage.keys():
				Storage.storage[key]['quantity'] -= self.order_product_list[key]['count']  # 13) После оформления заказа количество товара уменьшается на количество товаров из заказа.

		receive = {
			'order_id': self.order_id,
			'date_purchased': datetime.datetime.now().strftime('%d.%m.%Y %H:%M'),
			'items': self.order_product_list,
			'quantity': quantity,
			'total amount': round(total_amount, 2)
		}
		self.orders_pull[self.order_id] = {
			"order position": self.order_position,  # 12) Позиция заказа, созданная после оформления заказа пользователем.
			"order details": receive
		}

		return receive

	def get_order_info_by_order_id(self, order_id):
		if order_id in self.orders_pull.keys():
			return self.orders_pull[order_id]
		else:
			print('order not found')


# 1) Создайте товар с такими свойствами, как имя(name), подробные сведения(description or details),
# количество на складе(quantity), доступность(availability), цена(price).
# Добавить к этой задаче дескриптор для аттрибута цена.
# При назначении цены товара будет автоматически добавлен НДС 20%
# При получении цены товара, цена возврщается уже с учетом НДС
bread = Product(name='Bread', description='tasty fresh baked', availability=True)
bread.quantity = 6
bread.price = 125

milk = Product(name='Milk', description='fresh made from farm', availability=True)
milk.quantity = 20
milk.price = 15.99

soap = Product(name='Soap', description='clean up hands after walk', availability=True)
soap.quantity = 10
soap.price = 35.90


# 2) Добавить товар на склад
storage = Storage()
storage.add_to_storage(bread, category='food')
storage.add_to_storage(milk, category='food')
storage.add_to_storage(soap, category='cleaning')


# 3) Удалить товар со склада
storage.remove_product('Soap')


# 4) Распечатать остаток товара по его имени
print(storage.get_product_quantity('Bread'))
print(storage.get_product('Bread'))
print(storage.get_product('Milk'))


# 5) Распечатать остаток всех товаров
print(storage.get_all_products_quantity())

# 7) Распечатать список товаров с заданной категорией
print(storage.get_product_by_category('food'))


# 8) Корзина для покупок, в которой может быть много товаров с общей ценой.
basket_1 = Basket()


# 9) Добавить товары в корзину (вы не можете добавлять товары, если их нет в наличии)
basket_1.add_product_to_basket(bread)
basket_1.add_product_to_basket(bread)
basket_1.add_product_to_basket(bread)
basket_1.add_product_to_basket(bread)
basket_1.add_product_to_basket(milk)


# 10) Распечатать элементы корзины покупок с ценой и общей суммой
print(basket_1.get_basket_prod_and_price())


# 11) Оформить заказ и распечатать детали заказа по его номеру
pprint(basket_1.checkout())


# 11 распечатать детали заказа по его номеру
pprint(basket_1.get_order_info_by_order_id(order_id=1))

# ---------- второй заказ в котором можно проверить реакцию если раскупят товар, availability и тд
basket_2 = Basket()

basket_2.add_product_to_basket(bread)
basket_2.add_product_to_basket(bread)
basket_2.add_product_to_basket(milk)
basket_2.add_product_to_basket(milk)

print(basket_2.get_basket_prod_and_price())

pprint(basket_2.checkout())

pprint(basket_1.get_order_info_by_order_id(order_id=2))
