import pizza

NYcheese_pizza = pizza.Nypizzas.create('CHEESE', **{'name':'CHEESE'})
NYcheese_pizza.say_hello()

NYclam_pizza = pizza.Nypizzas.create('CLAM', **{'name':'CLAM'})
NYclam_pizza.say_hello()