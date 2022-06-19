import abc 
  
class AbstractFactory(abc.ABC): 
    # Aqui a construção do bolo com recheio (creme e outros), cobertura e decoração
    
    def __init__(self, is_lactfree): 
        self.is_lactfree = is_lactfree

    @abc.abstractmethod 
    def create_cream_n_fillings(self): 
        pass
  
    @abc.abstractmethod 
    def create_icing(self): 
        pass
  
    @abc.abstractmethod 
    def create_decoration(self): 
        pass
  
class BirthdayCakeFactory(AbstractFactory): 
    # Aqui a Fábrica de Bolo de Aniversário

    def __init__(self, is_lactfree):
        print('# Pedido de Bolo de Aniversário #')
        super().__init__(is_lactfree)
      
    def create_cream_n_fillings(self): 
        if self.is_lactfree: 
            return BirthdayCream_n_FillingsLactFree() 
        return BirthdayCream_n_Fillings() 
  
    def create_icing(self): 
        return BirthdayIcing() 
  
    def create_decoration(self): 
        return BirthdayDecoration() 
  
class WeddingCakeFactory(AbstractFactory): 
    # Aqui a Fábrica de Bolo de Casamento
    
    def __init__(self, is_lactfree):
        print('# Pedido de Bolo de Casamento #')
        super().__init__(is_lactfree)

    def create_cream_n_fillings(self): 
        if self.is_lactfree: 
            return WeddingCream_n_FillingsLactFree() 
        return WeddingCream_n_Fillings() 
  
    def create_icing(self): 
        return WeddingIcing() 
  
    def create_decoration(self): 
        return WeddingDecoration() 

class PartyCakeFactory(AbstractFactory): 
    # Aqui a Fábrica de Bolo de Festa Informal
    
    def __init__(self, is_lactfree):
        print('# Pedido de Bolo de Festa #')
        super().__init__(is_lactfree)

    def create_cream_n_fillings(self): 
        if self.is_lactfree: 
            return PartyCream_n_FillingsLactFree() 
        return PartyCream_n_Fillings() 
  
    def create_icing(self): 
        return PartyIcing() 
  
    def create_decoration(self): 
        return PartyDecoration() 
  
class Cream_n_FillingsAbstractProduct(abc.ABC): 
    # Aqui o produto A abstrato
      
    @abc.abstractmethod 
    def cream(self): 
        pass

    @abc.abstractmethod 
    def fillings(self): 
        pass
      
class BirthdayCream_n_Fillings(Cream_n_FillingsAbstractProduct): 
    # Produto A do Bolo de Aniversário
      
    def cream(self): 
        print('Creme: Chocolate')

    def fillings(self): 
        print('Recheio: Pedaços de Amêndoas')
  
class BirthdayCream_n_FillingsLactFree(Cream_n_FillingsAbstractProduct): 
    # Produto A do Bolo de Aniversário SEM LACTOSE
      
    def cream(self): 
        print('Creme: Chocolate (Sem Lactose)')

    def fillings(self): 
        print('Recheio: Pedaços de Amêndoas (Sem Lactose)')
  
class WeddingCream_n_Fillings(Cream_n_FillingsAbstractProduct): 
    # Produto A do Bolo de Casamento
      
    def cream(self): 
        print('Creme: Mandioca')

    def fillings(self): 
        print('Recheio: Pedaços de Nozes')
  
class WeddingCream_n_FillingsLactFree(Cream_n_FillingsAbstractProduct): 
    # Produto A do Bolo de Casamento SEM LACTOSE
      
    def cream(self): 
        print('Creme: Mandioca (Sem Lactose)')

    def fillings(self): 
        print('Recheio: Pedaços de Nozes (Sem Lactose)')

class PartyCream_n_Fillings(Cream_n_FillingsAbstractProduct): 
    # Produto A do Bolo de Festa Informal
      
    def cream(self): 
        print('Creme: Cenoura')

    def fillings(self): 
        print('Recheio: Pedaços de Chocolate')
  
class PartyCream_n_FillingsLactFree(Cream_n_FillingsAbstractProduct): 
    # Produto A do Bolo de Festa Informal SEM LACTOSE
      
    def cream(self): 
        print('Creme: Cenoura (Sem Lactose)')

    def fillings(self): 
        print('Recheio: Pedaços de Chocolate (Sem Lactose)')
  
class IcingAbstractProduct(abc.ABC): 
    # Aqui o produto B abstrato
      
    @abc.abstractmethod 
    def icing(self): 
        pass
      
class BirthdayIcing(IcingAbstractProduct): 
    # Produto B do Bolo de Aniversário
      
    def icing(self): 
        print('Cobertura: Brigadeiro')

class WeddingIcing(IcingAbstractProduct): 
    # Produto B do Bolo de Casamento
      
    def icing(self): 
        print('Cobertura: Pasta Americana Branca')

class PartyIcing(IcingAbstractProduct): 
    # Produto B do Bolo de Festa Informal
      
    def icing(self): 
        print('Cobertura: Chocolate')

class DecorationAbstractProduct(abc.ABC): 
    # Aqui o produto C abstrato
      
    @abc.abstractmethod 
    def decoration(self): 
        pass
      
class BirthdayDecoration(DecorationAbstractProduct): 
    # Produto C do Bolo de Aniversário
      
    def decoration(self): 
        print('Decoração: Confetes e Velas')

class WeddingDecoration(DecorationAbstractProduct): 
    # Produto C do Bolo de Casamento
      
    def decoration(self): 
        print('Decoração: Bonecos de Noivos e Rosas')

class PartyDecoration(DecorationAbstractProduct): 
    # Produto C do Bolo de Festa Informal
      
    def decoration(self): 
        print('Decoração: MMs')

def main():

    print("")

    # Bolo de Aniversário 

    factory = BirthdayCakeFactory(True)
    product_a = factory.create_cream_n_fillings()
    product_b = factory.create_icing()
    product_c = factory.create_decoration()
    product_a.cream()
    product_a.fillings()
    product_b.icing()
    product_c.decoration()

    print("")

    # Bolo de Casamento

    factory = WeddingCakeFactory(False)
    product_a = factory.create_cream_n_fillings()
    product_b = factory.create_icing()
    product_c = factory.create_decoration()
    product_a.cream()
    product_a.fillings()
    product_b.icing()
    product_c.decoration()

    print("")

    # Bolo de Festa

    factory = PartyCakeFactory(True)
    product_a = factory.create_cream_n_fillings()
    product_b = factory.create_icing()
    product_c = factory.create_decoration()
    product_a.cream()
    product_a.fillings()
    product_b.icing()
    product_c.decoration()

    print("")

if __name__ == "__main__":
    main()