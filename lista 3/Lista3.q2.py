
def tag_decorate(func):
   def legend(*args, **kwargs):
       return " @ LEGEND @ {0} @ LEGEND @ ".format(func(*args, **kwargs))
   return legend


class Car():
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name

    @tag_decorate
    def exclaim(self):
        return "O carro é uma " + self.brand + ", mais especificamente uma " + self.name 


my_car = Car('Ferrari', '458 Italia')
print(my_car.exclaim())
