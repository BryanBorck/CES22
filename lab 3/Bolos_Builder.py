class Director:
    # Responsável por alocar determinado bolo para o confeiteiro responsável

    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    # Algoritmo para setar o Bolo com o estilo pretendido
    def getCake(self):
        cake = Cake()

        cream, fillings = self.__builder.create_cream_n_fillings()
        cake.setCream_n_Fillings(cream, fillings)

        icing = self.__builder.create_icing()
        cake.setIcing(icing)

        decoration = self.__builder.create_decoration()
        cake.setDecoration(decoration)

        return cake

# O produto final, no caso, um bolo
class Cake:

    def __init__(self):
        self.__cream = None
        self.__fillings = None
        self.__icing = None
        self.__decoration = None

    def setCream_n_Fillings(self, cream, fillings):
        self.__cream = cream
        self.__fillings = fillings

    def setIcing(self, icing):
        self.__icing = icing

    def setDecoration(self, decoration):
        self.__decoration = decoration

    # Aqui defini o print para ficar bem parecido com o caso comparativo
    def specification(self):
        print("Creme: %s" % self.__cream)
        print("Recheio: %s" % self.__fillings)
        print("Cobertura: %s" % self.__icing)
        print("Decoração: %s" % self.__decoration)

class Builder:

    def __init__(self, is_lactfree): 
        self.is_lactfree = is_lactfree

    def create_cream_n_fillings(self): 
        pass

    def create_icing(self): 
        pass

    def create_decoration(self): 
        pass


class BirthdayCakeBuilder(Builder):

    def __init__(self, is_lactfree):
        super().__init__(is_lactfree)

    def create_cream_n_fillings(self):
        if self.is_lactfree:
            cream = "Chocolate (Sem Lactose)"
            fillings = "Pedaços de Amêndoas (Sem Lactose)"
            return cream, fillings
        cream = "Chocolate"
        fillings = "Pedaços de Amêndoas"
        return cream, fillings

    def create_icing(self):
        icing = "Brigadeiro"
        return icing

    def create_decoration(self):
        decoration = "Confetes e Velas"
        return decoration

class WeddingCakeBuilder(Builder):

    def __init__(self, is_lactfree):
        super().__init__(is_lactfree)

    def create_cream_n_fillings(self):
        if self.is_lactfree:
            cream = "Mandioca (Sem Lactose)"
            fillings = "Pedaços de Nozes (Sem Lactose)"
            return cream, fillings
        cream = "Mandioca"
        fillings = "Pedaços de Nozes"
        return cream, fillings

    def create_icing(self):
        icing = "Pasta Americana Branca"
        return icing

    def create_decoration(self):
        decoration = "Bonecos de Noivos e Rosas"
        return decoration

class PartyCakeBuilder(Builder):

    def __init__(self, is_lactfree):
        super().__init__(is_lactfree)

    def create_cream_n_fillings(self):
        if self.is_lactfree:
            cream = "Cenoura (Sem Lactose)"
            fillings = "Pedaços de Chocolate (Sem Lactose)"
            return cream, fillings
        cream = "Cenoura"
        fillings = "Pedaços de Chocolate"
        return cream, fillings

    def create_icing(self):
        icing = "Chocolate"
        return icing

    def create_decoration(self):
        decoration = "MMs"
        return decoration

def main():
    birthdayBuilder = BirthdayCakeBuilder(True)
    weddingBuilder = WeddingCakeBuilder(False)
    partyBuilder = PartyCakeBuilder(True)

    director = Director()

    print("")

    # Bolo de Aniversário

    print("# Pedido de Bolo de Aniversário #")
    director.setBuilder(birthdayBuilder)
    birthdayCake = director.getCake()
    birthdayCake.specification()

    print("")

    # Bolo de Casamento

    print("# Pedido de Bolo de Casamento #")
    director.setBuilder(weddingBuilder)
    weddingCake = director.getCake()
    weddingCake.specification()

    print("")

    # Bolo de Festa

    print("# Pedido de Bolo de Festa #")
    director.setBuilder(partyBuilder)
    partyCake = director.getCake()
    partyCake.specification()

    print("")

if __name__ == "__main__":
    main()