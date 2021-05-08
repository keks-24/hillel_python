import pytest
from hw_descriptors.hw_ShopCart import Storage, Product, Basket


@pytest.fixture(scope="session")
def product_bread():
	name = 'Bread'
	description = 'tasty fresh baked'
	availability = True
	prod = Product(name=name, description=description, availability=availability)
	return prod


@pytest.fixture(scope="session")
def product_milk():
	name = 'Milk'
	description = 'tasty fresh baked'
	availability = True
	prod = Product(name=name, description=description, availability=availability)
	return prod


@pytest.fixture(scope="session")
def storage():
	return Storage()


@pytest.fixture(scope="session")
def basket():
	return Basket()


def test_product_name(product_bread):
	assert product_bread.name == "Bread"


def test_product_description(product_bread):
	assert product_bread.description == 'tasty fresh baked'


def test_product_availability(product_bread):
	assert product_bread.availability == True


def test_change_quantity_of_product(product_bread):
	new_value = 10
	product_bread.quantity = new_value
	assert product_bread.quantity == new_value


def test_product_instance(product_bread):
	isinstance(product_bread, Product)


def test_adding_to_storage(storage, product_bread):
	product = product_bread
	assert storage.add_to_storage(product_bread, category='food') == f'Product - {product.name} add on storage'


def test_double_adding_to_storage(storage, product_bread):
	assert storage.add_to_storage(product_bread, category='food') == f'Product - {product_bread.name} already at storage'


def test_check_quantity_product(storage, product_bread):
	assert storage.get_product_quantity(product_bread.name) == f"total quantity of {product_bread.name} is {Storage.storage[product_bread.name]['quantity']}"


def test_delete_not_exist_product(storage):
	assert storage.remove_product('cheese') == 'No such product'


def test_add_unavailable_product_to_basket(storage, basket, product_bread):
	Storage.storage[product_bread.name]['availability'] = False
	assert basket.add_product_to_basket(product_bread) == f'Product {product_bread.name} not available or out of sale'