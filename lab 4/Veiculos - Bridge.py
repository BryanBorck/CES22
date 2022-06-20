import abc

class Vehicle(abc.ABC):
    #

    def __init__(self, engine, length, color):
        self.engine = engine._engine
        self.fuelRequired = engine._fuelRequired
        self.greenPhrase = engine._green
        self.length = length
        self.color = color
        self.size = None

    @abc.abstractmethod
    def setSize(self):
        pass

    @abc.abstractmethod
    def setWheels(self):
        pass

    @abc.abstractmethod
    def setPassengers(self):
        pass

    @abc.abstractmethod
    def setFuelRequired(self):
        pass

    @abc.abstractmethod
    def specifications(self):
        pass

class Car(Vehicle):
    # Aqui define-se atributos de um carro

    def __init__(self, engine, length, color):
        super().__init__(engine, length, color)
        self.setSize()
    
    def setSize(self):
        if self.length > 5:
            self.size = 'Big'
        self.size = 'Normal'

    def setWheels(self):
        return 4

    def setPassengers(self):
        if self.length > 5:
            return 7
        return 5
    
    def setFuelRequired(self):
        if self.fuelRequired:
            return "Sim"
        return "Não"

    def specifications(self):
        print("Motor: %s" % self.engine)
        print("Cor: %s" % self.color)
        print("Tamanho: %s" % self.size)
        print("N de Rodas: %s" % self.setWheels())
        print("N de Passageiros: %s" % self.setPassengers())
        print("Precisa de Combustível? %s" % self.setFuelRequired())
        print("%s" % self.greenPhrase)

class Truck(Vehicle):
    # Aqui define-se atributos de um caminhão

    def __init__(self, engine, length, color):
        super().__init__(engine, length, color)
        self.setSize()
    
    def setSize(self):
        if self.length > 20:
            self.size = 'Big'
        self.size = 'Normal'

    def setWheels(self):
        if self.length > 20:
            return 10 
        return 8

    def setPassengers(self):
        return 2
    
    def setFuelRequired(self):
        if self.fuelRequired:
            return "Sim"
        return "Não"

    def specifications(self):
        print("Motor: %s" % self.engine)
        print("Cor: %s" % self.color)
        print("Tamanho: %s" % self.size)
        print("N de Rodas: %s" % self.setWheels())
        print("N de Passageiros: %s" % self.setPassengers())
        print("Precisa de Combustível? %s" % self.setFuelRequired())
        print("%s" % self.greenPhrase)

class Bus(Vehicle):
    # Aqui define-se atributos de um ônibus

    def __init__(self, engine, length, color):
        super().__init__(engine, length, color)
        self.setSize()
    
    def setSize(self):
        if self.length > 10:
            self.size = 'Big'
        self.size = 'Normal'

    def setWheels(self):
        if self.length > 10:
            return 6 
        return 4

    def setPassengers(self):
        if self.length > 10:
            return 60 
        return 40
    
    def setFuelRequired(self):
        if self.fuelRequired:
            return "Sim"
        return "Não"

    def specifications(self):
        print("Motor: %s" % self.engine)
        print("Cor: %s" % self.color)
        print("Tamanho: %s" % self.size)
        print("N de Rodas: %s" % self.setWheels())
        print("N de Passageiros: %s" % self.setPassengers())
        print("Precisa de Combustível? %s" % self.setFuelRequired())
        print("%s" % self.greenPhrase)

class Engine(abc.ABC):
    # A classe representa o motor instanciando duas funções: qtd de combustível utilizada e caráter verde da escolha     

    @abc.abstractmethod
    def fuel_required(self):
        pass

    @abc.abstractmethod
    def green_engine(self):
        pass

class Eletric(Engine):
    # Aqui define-se a escolha de um motor elétrico

    def __init__(self):
        self._engine = "Elétrico"
        self.fuel_required()
        self.green_engine()
    
    def fuel_required(self):
        self._fuelRequired = False

    def green_engine(self):
        self._green = "Escolha positiva ao meio-ambiente"

class Combustion(Engine):
    # Aqui define-se a escolha de um motor de combustão

    def __init__(self):
        self._engine = "Combustão"
        self.fuel_required()
        self.green_engine()
    
    def fuel_required(self):
        self._fuelRequired = True

    def green_engine(self):
        self._green = "Escolha negativa ao meio-ambiente"

class Hybrid(Engine):
    # Aqui define-se a escolha de um motor híbrido

    def __init__(self):
        self._engine = "Híbrido"
        self.fuel_required()
        self.green_engine()
    
    def fuel_required(self):
        self._fuelRequired = True

    def green_engine(self):
        self._green = "Escolha neutra ao meio-ambiente"


# Aqui vamos aos resultados


def main():

    print("")

    # Carros

    print("# Primeiro Veículo #")
    print("CARRO")
    car1 = Car(Eletric(), 4, 'Azul')
    car1.specifications()
    print("")

    print("# Segundo Veículo #")
    print("CARRO")
    car2 = Car(Hybrid(), 6, 'Cinza')
    car2.specifications()
    print("")

    # Caminhões

    print("# Terceiro Veículo #")
    print("CAMINHÃO")
    truck1 = Truck(Combustion(), 21, 'Vermelho')
    truck1.specifications()
    print("")

    print("# Quarto Veículo #")
    print("CAMINHÃO")
    truck2 = Truck(Hybrid(), 15, 'Branco')
    truck2.specifications()
    print("")

    # Ônibus

    print("# Quinto Veículo #")
    print("ÔNIBUS")
    bus1 = Bus(Eletric(), 18, 'Rosa')
    bus1.specifications()
    print("")

    print("# Sexto Veículo #")
    print("ÔNIBUS")
    bus2 = Bus(Combustion(), 8, 'Amarelo')
    bus2.specifications()
    print("")

if __name__ == "__main__":
    main()