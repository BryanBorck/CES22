from datetime import date


class Car:
    def __init__(self, brand, name, year):
        self.brand = brand
        self.name = name
        self.year = year

    def __repr__(self):
        return (f'Car({self.brand}, {self.name}, {self.year})') 

    # instance methods
    def change_car_of_this_brand(self, new_name, new_year): 
        self.name = new_name
        self.year = new_year
    
    # abstract methods
    def sound(self):
        raise NotImplementedError

    # static methods
    @staticmethod
    def my_car():
        return 'Car(Mercedez Benz G-63 AMG 2022)'
    
    @staticmethod
    def is_new(yr):
        return (date.today().year - yr) < 4

    # class methods
    @classmethod
    def my_other_car(cls):
        return cls('Ford', 'GT40', 1968)

    @classmethod
    def age_to_year_of_creation(cls, brand, name, age):
        return cls(brand, name, date.today().year - age)


class LegendCar(Car):
    def __init__(self, brand, name, year):
        super().__init__(brand, name, year)
        print('Im a legend.')
    
    def sound(self):
        print('VRUMM VRUUUUMMMMMM')


class TrashCar(Car):
    def __init__(self, brand, name, year):
        super().__init__(brand, name, year)
        print('Im a trash.')
    
    def sound(self):
        print('BOOOOMMMMM')


# class method vs static method
print(Car.my_car())
print(Car.my_other_car())
print('')

# instance method vs class method
car_1 = Car('Ferrari', '458 Italia', 2009)
car_2 = Car.age_to_year_of_creation('Ferrari', '458 Italia', 13)
print(car_1)
print(car_2)
print('')

# good example of instace method
car_1.change_car_of_this_brand('California', 2008)
print(car_1)
print('')

# good example of static method
print(Car.is_new(2020))
print(Car.is_new(2010))
print('')

# good example of class method
print(Car.age_to_year_of_creation('Volkswagen', 'Typ 1', 84))
print('')

# good example of abstract method
legend_car = LegendCar('Ferrari', '458 Italia', 2009)
print(legend_car.sound())
trash_car = TrashCar('Volkswagen', 'Typ 1', 1938)
print(trash_car.sound())
print('')
