
class GreenThings:
  def __init__(self, thing_name):
    print(thing_name, 'is a green thing.')

# Plant inherits GreenThings
class Plant(GreenThings):
  def __init__(self, plant_name):
    print(plant_name, 'is a plant.')
    super().__init__(plant_name)
    
# IsFood inherits Plant
class IsFood(Plant):
  def __init__(self, food_name):
    print(food_name, "can be eaten.")
    super().__init__(food_name)

# IsGood inherits Plant
class IsGood(Plant):
  def __init__(self, good_thing_name):
    print(good_thing_name, "is very good.")
    super().__init__(good_thing_name)

# Lettuce inherits IsFood and IsGood
class Lettuce(IsFood, IsGood):
  def __init__(self):
    print('I am a lettuce.')
    super().__init__('Lettuce')

# Main
lettuce = Lettuce()
print('')
dangerous_plant = IsGood('Dangerous Plant')
print('')
spinach = IsFood('Spinach')
print('')
pacifier = Plant('Pacifier')
print('')
my_car = GreenThings('My car')
