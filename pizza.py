import object_factory

class CheesePizza:
	def __init__(self, i):
		self.thin_crust_dough = i.get('THINCRUSTDOUGH', ingredients)
		self.marinara_sauce = i.get('MARINARASAUCE', ingredients)
		self.reggiano_cheese = i.get('REGGIANOCHEESE', ingredients)
		self.garlic = i.get('GARLIC', ingredients)
		self.onion = i.get('ONION', ingredients)
		self.mushroom = i.get('MUSHROOM'. ingredients)
		self.redpepper = i.get('REDPEPPER', ingredients)
		self.sliced_pepperoni = i.get('SLICEDPEPPERONI', ingredients)
		self.fresh_clam = i.get('FRESHCLAM', ingredients)
		
	def say_hello(self):
		print(f'Hello, my name is {self.marinara_sauce}')


class CheesePizzaBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self, ingredients):
		if not self._instance:
			self._instance = CheesePizza(ingredients)
		return self._instance


class ClamPizza:
	def __init__(self, name):
		self.name = name
		
	def say_hello(self):
		print(f'Hello, and my name is {self.name}')


class ClamPizzaBuilder:
	def __init__(self):
		self._instance = None
		
	def __call__(self, name):
		if not self._instance:
			self._instance = ClamPizza(name)
		return self._instance


class NYPizzaProviders(object_factory.ObjectFactory):
	def get(self, pizza_id, **kwargs):
		pass


class ThinCrustDough():
	def to_str(self):
		print(f"Hi I'm ThinCrustDough ingredient")
	

class ThickCrustDough():
	def to_str(self):
		print(f"Hi I'm ThickCrustDough ingredient")

		
class PlumTomatoSauce():
	def to_str(self):
		print(f"Hi I'm PlumTomatoSauce ingredient")


class MarinaraSauce():
	def to_str(self):
		print(f"Hi I'm MarinaraSauce ingredient")


class ParmesanCheese():
	def to_str(self):
		print(f"Hi I'm ParmesanCheese ingredient")


class REGGIANOCheese():
	def to_str(self):
		print(f"Hi I'm REGGIANOCheese ingredient")


class MozzarellaCheese():
	def to_str(self):
		print(f"Hi I'm MozzarellaCheese ingredient")


class BlackOlives():
	def to_str(self):
		print(f"Hi I'm BlackOlives ingredient")


class Eggplant():
	def to_str(self):
		print(f"Hi I'm Eggplant ingredient")


class Onion():
	def to_str(self):
		print(f"Hi I'm Onion ingredient")


class Garlic():
	def to_str(self):
		print(f"Hi I'm Garlic ingredient")


class RedPepper():
	def to_str(self):
		print(f"Hi I'm Red Pepper ingredient")
	

class Mushroom():
	def to_str(self):
		print(f"Hi I'm Mushroom ingredient")


class Spinach():
	def to_str(self):
		print(f"Hi I'm Spinach ingredient")


class SlicedPepperoni():
	def to_str(self):
		print(f"Hi I'm Sliced Pepperoni ingredient")


class FreshClam():
	def to_str(self):
		print(f"Hi I'm Fresh Clam ingredient")


class FrozenClam():
	def to_str(self):
		print(f"Hi I'm Frozen Clam ingredient")


class PizzaIngredients:
	def __init__(self, ingredients):
		self.ingredients = ingredients


class PizzaIngredientsBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self, ingredients):
		if not self._instance:
			self._instance = PizzaIngredients(ingredients)
		return self._instance


class PizzaIngredientsProviders(object_factory.ObjectFactory):
	def get(self, ingredient_id, **kwargs):
		return self.create(ingredient_id, **kwargs)

		
NYpizzas = NYPizzaProviders()
NYpizzas.register_builder('CHEESE', CheesePizzaBuilder())
NYpizzas.register_builder('CLAM', ClamPizzaBuilder())

"""
Ingredients Factory
"""
ingredients = PizzaIngredientsProviders()
ingredients.register_builder('PLUMTOMATOSAUCE', PlumTomatoSauce())
ingredients.register_builder('MARINARASAUCE', MarinaraSauce())
ingredients.register_builder('THINCRUSTDOUGH', ThinCrustDough())
ingredients.register_builder('THICKCRUSTDOUGH', ThickCrustDough())
ingredients.register_builder('PARMESANCHEESE', ParmesanCheese())
ingredients.register_builder('REGGIANOCHEESE', REGGIANOCheese())
ingredients.register_builder('MOZZARELLACHEESE', MozzarellaCheese())
ingredients.register_builder('GARLIC', Garlic())
ingredients.register_builder('ONION', Onion())
ingredients.register_builder('MUSHROOM', Mushroom())
ingredients.register_builder('REDPEPPER', RedPepper())
ingredients.register_builder('BLACKOLIVES', BlackOlives())
ingredients.register_builder('EGGPLANT', Eggplant())
ingredients.register_builder('SPINACH', Spinach())
ingredients.register_builder('SLICEDPEPPERONI', SlicedPepperoni())
ingredients.register_builder('FRESHCLAM', FreshClam())
ingredients.register_builder('FROZENCLAM', FrozenClam())