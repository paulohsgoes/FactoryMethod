import object_factory

class CheesePizza:
	def __init__(self, name):
		self.name = name
		
	def say_hello(self):
		print(f'Hello, my name is {self.name}')


class CheesePizzaBuilder:
	def __init__(self):
		self._instance = None

	def __call__(self, name):
		if not self._instance:
			self._instance = CheesePizza(name)
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


Nypizzas = NYPizzaProviders()
Nypizzas.register_builder('CHEESE', CheesePizzaBuilder())
Nypizzas.register_builder('CLAM', ClamPizzaBuilder())