import object_factory

class CheesePizza:
	def __init__(self, **i_list):
		self._ingredients_list = i_list
		for key in self._ingredients_list:
			print(key, '->', self._ingredients_list[key].to_str())
		# self.thin_crust_dough = ingredients.create('THINCRUSTDOUGH')
		# self.reggiano_cheese = ingredients.create('REGGIANOCHEESE')
		# self.garlic = ingredients.create('GARLIC')
		# self.onion = ingredients.create('ONION')
		# self.marinara_sauce = ingredients.create('MARINARASAUCE')
		# self.mushroom = ingredients.create('MUSHROOM')
		# self.redpepper = ingredients.create('REDPEPPER')
		# self.sliced_pepperoni = ingredients.create('SLICEDPEPPERONI')
		# self.fresh_clam = ingredients.create('FRESHCLAM')

		
	def say_hello(self):
		print(f'Hello, my name is {self.marinara_sauce}')


class CheesePizzaBuilder:
	def __init__(self, **ingredients_list):
		self._instance = None
		self._list = ingredients_list

	def __call__(self):
		if not self._instance:
			self._instance = CheesePizza(**self._list)
		return self._instance


class ClamPizza:
	def __init__(self):
		self.thick_crust_dough = ingredients.create('THICKCRUSTDOUGH')
		self.plum_tomato_sauce = ingredients.create('PLUMTOMATOSAUCE')
		self.mozzarella_cheese = ingredients.create('MOZZARELLACHEESE')
		self.blach_olives = ingredients.create('BLACKOLIVES')
		self.spinach = ingredients.create('SPINACH')
		self.eggplant = ingredients.create('EGGPLANT')
		self.sliced_pepperoni = ingredients.create('SLICEDPEPPERONI')
		self.frozen_clam = ingredients.create('FROZENCLAM')

		
	def say_hello(self):
		print(f'Hello, and my name is {self.name}')


class ClamPizzaBuilder:
	def __init__(self):
		self._instance = None
		
	def __call__(self):
		if not self._instance:
			self._instance = ClamPizza()
		return self._instance


class NYPizzaProviders(object_factory.ObjectFactory):
	def get(self, pizza_id, **kwargs):
		pass


class ThinCrustDough:
	def __init__(self):
		print(f'THIN CRUST DOUGH ingredient successfuly created')
		
	def __str(self):
		return f"Hi I'm Thin Crust Dough ingredient"


class ThinCrustDoughBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self):
		if not self._instance:
			self._instance = ThinCrustDough()
		return self._instance


class ThickCrustDough:
	def __init__(self):
		print(f'THICK CRUST DOUGH ingredient successfuly created')
		
	def __str__ (self):
		return f"Hi I'm Thick Crust Dough ingredient"


class ThickCrustDoughBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self):
		if not self._instance:
			self._instance = ThickCrustDough()
		return self._instance

		
class PlumTomatoSauce:
	def __init__(self):
		print(f'PLUM TOMATO SAUCE ingredient successfuly created')

	def to_str(self):
		print(f"Hi I'm Plum Tomato Sauce ingredient")


class PlumTomatoSauceBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self):
		if not self._instance:
			self._instance = PlumTomatoSauce()
		return self._instance


class MarinaraSauce:
	def __init__(self):
		print(f'MARINARA SAUCE ingredient successfuly created')

	def to_str(self):
		print(f"Hi I'm Marinara Sauce ingredient")


class MarinaraSauceBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self):
		if not self._instance:
			self._instance = MarinaraSauce()
		return self._instance


class ParmesanCheese:
	def __init__(self):
		print(f'PARMESAN CHEESE ingredient successfuly created')

	def to_str(self):
		print(f"Hi I'm Parmesan Cheese ingredient")


class ParmesanCheeseBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self):
		if not self._instance:
			self._instance = ParmesanCheese()
		return self._instance


class ReggianoCheese:
	def __init__(self):
		print(f'REGGIANO CHEESE ingredient successfuly created')

	def to_str(self):
		print(f"Hi I'm Reggiano Cheese ingredient")


class ReggianoCheeseBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self):
		if not self._instance:
			self._instance = ReggianoCheese()
		return self._instance
		

class MozzarellaCheese:
	def __init__(self):
		print(f'MOZZARELLA CHEESE ingredient successfuly created')

	def to_str(self):
		print(f"Hi I'm MozzarellaCheese ingredient")


class MozzarellaCheeseBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self):
		if not self._instance:
			self._instance = MozzarellaCheese()
		return self._instance


class BlackOlives:
	def __init__(self):
		print(f'BLACK OLIVES ingredient successfuly created')

	def to_str(self):
		print(f"Hi I'm BlackOlives ingredient")


class BlackOlivesBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self):
		if not self._instance:
			self._instance = BlackOlives()
		return self._instance


class Eggplant:
	def __init__(self):
		print(f'EGGPLANT ingredient successfuly created')

	def to_str(self):
		print(f"Hi I'm Eggplant ingredient")


class EggplantBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self):
		if not self._instance:
			self._instance = Eggplant()
		return self._instance


class Onion:
	def __init__(self):
		print(f'ONION ingredient successfuly created')

	def to_str(self):
		print(f"Hi I'm Onion ingredient")


class OnionBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self):
		if not self._instance:
			self._instance = Onion()
		return self._instance


class Garlic:
	def __init__(self):
		print(f'GARLIC ingredient successfuly created')

	def to_str(self):
		print(f"Hi I'm Garlic ingredient")


class GarlicBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self):
		if not self._instance:
			self._instance = Garlic()
		return self._instance


class RedPepper:
	def __init__(self):
		print(f'RED PEPPER ingredient successfuly created')
		
	def to_str(self):
		print(f"Hi I'm Red Pepper ingredient")
	

class RedPepperBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self):
		if not self._instance:
			self._instance = RedPepper()
		return self._instance


class Mushroom:
	def __init__(self):
		print(f'MUSHROOM ingredient successfuly created')

	def to_str(self):
		print(f"Hi I'm Mushroom ingredient")


class MushroomBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self):
		if not self._instance:
			self._instance = Mushroom()
		return self._instance


class Spinach:
	def __init__(self):
		print(f'SPINACH ingredient successfuly created')

	def to_str(self):
		print(f"Hi I'm Spinach ingredient")


class SpinachBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self):
		if not self._instance:
			self._instance = Spinach()
		return self._instance


class SlicedPepperoni:
	def __init__(self):
		print(f'SLICED PEPPERONI ingredient successfuly created')
		
	def to_str(self):
		print(f"Hi I'm Sliced Pepperoni ingredient")


class SlicedPepperoniBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self):
		if not self._instance:
			self._instance = SlicedPepperoni()
		return self._instance


class FreshClam:
	def __init__(self):
		print(f'FRESH CLAM ingredient successfuly created')
		
	def to_str(self):
		print(f"Hi I'm Fresh Clam ingredient")


class FreshClamBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self):
		if not self._instance:
			self._instance = FreshClam()
		return self._instance


class FrozenClam:
	def __init__(self):
		print(f'FROZEN CLAM ingredient successfuly created')

	def to_str(self):
		print(f"Hi I'm Frozen Clam ingredient")


class FrozenClamBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self):
		if not self._instance:
			self._instance = FrozenClam()
		return self._instance


class PizzaIngredientsProviders(object_factory.ObjectFactory):
	def get(self, ingredient_id, **kwargs):
		return self.create(ingredient_id, **kwargs)

		
# NYpizzas = NYPizzaProviders()
# NYpizzas.register_builder('CHEESE', CheesePizzaBuilder(**NY_cheese_pizza_ingredients))
# NYpizzas.register_builder('CLAM', ClamPizzaBuilder())

"""
Ingredients Factory
"""
ingredients = PizzaIngredientsProviders()
ingredients.register_builder('PLUMTOMATOSAUCE', PlumTomatoSauceBuilder())
ingredients.register_builder('MARINARASAUCE', MarinaraSauceBuilder())
ingredients.register_builder('THINCRUSTDOUGH', ThinCrustDoughBuilder())
ingredients.register_builder('THICKCRUSTDOUGH', ThickCrustDoughBuilder())
ingredients.register_builder('PARMESANCHEESE', ParmesanCheeseBuilder())
ingredients.register_builder('REGGIANOCHEESE', ReggianoCheeseBuilder())
ingredients.register_builder('MOZZARELLACHEESE', MozzarellaCheeseBuilder())
ingredients.register_builder('GARLIC', GarlicBuilder())
ingredients.register_builder('ONION', OnionBuilder())
ingredients.register_builder('MUSHROOM', MushroomBuilder())
ingredients.register_builder('REDPEPPER', RedPepperBuilder())
ingredients.register_builder('BLACKOLIVES', BlackOlivesBuilder())
ingredients.register_builder('EGGPLANT', EggplantBuilder())
ingredients.register_builder('SPINACH', SpinachBuilder())
ingredients.register_builder('SLICEDPEPPERONI', SlicedPepperoniBuilder())
ingredients.register_builder('FRESHCLAM', FreshClamBuilder())
ingredients.register_builder('FROZENCLAM', FrozenClamBuilder())

NY_cheese_pizza_ingredients = {
	'thin_crust_dough': ingredients.get('THINCRUSTDOUGH'),
	'reggiano_cheese': ingredients.get('REGGIANOCHEESE'),
	'garlic': ingredients.get('GARLIC'),
	'onion': ingredients.get('ONION'),
	'marinara_sauce': ingredients.get('MARINARASAUCE'),
	'mushroom': ingredients.get('MUSHROOM'),
	'red_pepper': ingredients.get('REDPEPPER'),
	'sliced_pepperoni': ingredients.get('SLICEDPEPPERONI'),
	'fresh_clam': ingredients.get('FRESHCLAM')
}

NYpizzas = NYPizzaProviders()
NYpizzas.register_builder('CHEESE', CheesePizzaBuilder(**NY_cheese_pizza_ingredients))
NYpizzas.register_builder('CLAM', ClamPizzaBuilder())
