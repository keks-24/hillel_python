import pytest
from hw_descriptors.hw_ShopCart import Storage, Product, Basket


def test_product_fields():
	name = 'Bread'
	description = 'tasty fresh baked'
	availability = True
	prod1 = Product(name=name, description=description, availability=availability)
	assert prod1.name == name
	assert prod1.description == description
	assert prod1.availability == availability
	isinstance(prod1, Product)


