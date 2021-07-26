import object_factory
import ingredients

class CheesePizza:
	def __init__(self, **ingredients_list):
		self._ingredients_list = ingredients_list

	def __str__(self):
		line = "Cheese Pizza"
		return line


class CheesePizzaBuilder:
	def __init__(self, **ingredients_list):
		self._instance = None
		self._list = ingredients_list

	def __call__(self):
		if not self._instance:
			self._instance = CheesePizza(**self._list)
		return self._instance
		

class ClamPizza:
	def __init__(self, **ingredients_list):
		self._ingredients_list = ingredients_list
		
	def __str__(self):
		line = "Clam Pizza"
		return line


class ClamPizzaBuilder:
	def __init__(self, **ingredients_list):
		self._instance = None
		self._list = ingredients_list
		
	def __call__(self):
		if not self._instance:
			self._instance = ClamPizza(**self._list)
		return self._instance


class PepperoniPizza:
	def __init__(self, **ingredients_list):
		self._ingredients_list = ingredients_list
		
	def __str__(self):
		line = "Pepperoni Pizza"
		return line
		
		
class PepperoniPizzaBuilder:
	def __init__(self, **ingredients_list):
		self._instance = None
		self._list = ingredients_list
		
	def __call__(self):
		if not self._instance:
			self._instance = PepperoniPizza(**self._list)
		return self._instance


class NYPizzaProviders(object_factory.ObjectFactory):
	def get(self, pizza_id, **kwargs):
		pass


NY_cheese_pizza_ingredients = {
	'thin_crust_dough': ingredients.ingredients.get('THINCRUSTDOUGH'),
	'reggiano_cheese': ingredients.ingredients.get('REGGIANOCHEESE'),
	'marinara_sauce': ingredients.ingredients.get('MARINARASAUCE')
}

NY_clam_pizza_ingredients = {
	'thin_crust_dough': ingredients.ingredients.get('THINCRUSTDOUGH'),
	'reggiano_cheese': ingredients.ingredients.get('REGGIANOCHEESE'),
	'marinara_sauce': ingredients.ingredients.get('MARINARASAUCE'),
	'fresh_clam': ingredients.ingredients.get('FRESHCLAM')
}

NY_pepperoni_pizza_ingredients = {
	'thin_crust_dough': ingredients.ingredients.get('THINCRUSTDOUGH'),
	'reggiano_cheese': ingredients.ingredients.get('REGGIANOCHEESE'),
	'marinara_sauce': ingredients.ingredients.get('MARINARASAUCE'),
	'fresh_clam': ingredients.ingredients.get('FRESHCLAM'),
	'sliced_pepperoni': ingredients.ingredients.get('SLICEDPEPPERONI')
}

NYpizzas = NYPizzaProviders()
NYpizzas.register_builder('CHEESE', CheesePizzaBuilder(**NY_cheese_pizza_ingredients))
NYpizzas.register_builder('CLAM', ClamPizzaBuilder(**NY_clam_pizza_ingredients))
NYpizzas.register_builder('PEPPERONI', PepperoniPizzaBuilder(**NY_pepperoni_pizza_ingredients))