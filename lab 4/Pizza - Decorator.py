class PizzaIngredient:

    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost

class PizzaBox(PizzaIngredient):
    cost = 0.0

class Decorator(PizzaIngredient):
    def __init__(self, pizzaIngredient):
        self.component = pizzaIngredient
    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaIngredient.getTotalCost(self)
    def getDescription(self):
        return self.component.getDescription() + " " + PizzaIngredient.getDescription(self)

class Mozzarela(Decorator):
    cost = 5.00
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)

class TomatoSauce(Decorator):
    cost = 3.00
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)

class Tomatoes(Decorator):
    cost = 2.00
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)

class Onions(Decorator):
    cost = 1.50
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)

class Olives(Decorator):
    cost = 1.50
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)

class Pepper(Decorator):
    cost = 0.50
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)

class Chicken(Decorator):
    cost = 7.00
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)

class Ham(Decorator):
    cost = 4.00
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)

class Pepperoni(Decorator):
    cost = 8.00
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)

class Catupiry(Decorator):
    cost = 5.00
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)

ham_pizza = Ham(Tomatoes(Pepper(Mozzarela(TomatoSauce(PizzaBox())))))
print(ham_pizza.getDescription() + ": $" + str(ham_pizza.getTotalCost()))
pepperoni_pizza = Pepperoni(Onions(Pepper(Mozzarela(TomatoSauce(PizzaBox())))))
print(pepperoni_pizza.getDescription() + ": $" + str(pepperoni_pizza.getTotalCost()))
chicken_pizza = Chicken(Olives(Mozzarela(TomatoSauce(PizzaBox()))))
print(chicken_pizza.getDescription() + ": $" + str(chicken_pizza.getTotalCost()))
chicken_wcat_pizza = Chicken(Catupiry(Olives(Onions(Mozzarela(TomatoSauce(PizzaBox()))))))
print(chicken_wcat_pizza.getDescription() + ": $" + str(chicken_wcat_pizza.getTotalCost()))
chicken_pepperoni_wcat_pizza = Chicken(Pepperoni(Catupiry(Olives(Tomatoes(Onions(Pepper(Mozzarela(TomatoSauce(PizzaBox())))))))))
print(chicken_pepperoni_wcat_pizza.getDescription() + ": $" + str(chicken_pepperoni_wcat_pizza.getTotalCost()))