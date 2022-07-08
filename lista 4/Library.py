class Library():
    def __init__(self):
        self._listbooks = []
        self._listclients = []
        self._listpurchaseOrders = []

    def add_book(self, book):
        self._listbooks.append(book)
    
    def remove_book(self, book):
        self._listbooks.remove(book)

    def consult_book(self, book):
        print("")
        print("Titulo: " + book._titulo)
        print("Autor: " + book._autor)
        print("Genero: " + book._genero)
        print("Edicao: " + book._edicao)
        print("Editora: " + book._editora)
        print("")
    
    def consult_bookByAuthor(self, author):
        print("")
        print(author._nome)
        print("Pertencem à Loja os seguintes Livros:")
        for bookAuthor in author._titulos:
            if bookAuthor in self._listbooks:
                print("")
                print("Titulo: " + bookAuthor._titulo)
                print("Genero: " + bookAuthor._genero)
                print("Edicao: " + bookAuthor._edicao)
                print("Editora: " + bookAuthor._editora)
                print("")
    
    def add_client(self, client):
        self._listclients.append(client)
    
    def remove_client(self, client):
        self._listclients.remove(client)

    def consult_client(self, client):
        print("")
        print("Nome: " + client._nome)
        print("Email: " + client._email)
        print("")

    def add_purchaseOrder(self, purchaseOrder):
        self._listpurchaseOrders.append(purchaseOrder)
    
    def remove_purchaseOrder(self, purchaseOrder):
        self._listpurchaseOrders.remove(purchaseOrder)

    def consult_purchaseOrder(self, purchaseOrder):
        print("")
        print("Nome: " + (purchaseOrder._product)._titulo)
        print("Quantidade: " + str(purchaseOrder._quantity))
        print("")
        
class Book:
    def __init__(self, titulo, autor, genero, edicao, editora, p_venda, p_compra):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        self._edicao = edicao
        self._editora = editora
        self._p_venda = p_venda
        self._p_compra = p_compra
        self._dif = (self._p_venda - self._p_compra)
        self._tax = 0
        self.set_tax()

    def set_tax(self):
        if self._genero == "Ficcao":
            self._tax = 0.25 * (self._p_venda - self._p_compra)
        if self._genero == "Romance":
            self._tax = 0.20 * (self._p_venda - self._p_compra)
        if self._genero == "Autoajuda":
            self._tax = 0.15 * (self._p_venda - self._p_compra)
        if self._genero == "Academico":
            self._tax = 0.10 * (self._p_venda - self._p_compra)
        if self._genero == "Infantil":
            self._tax = 0.05 * (self._p_venda - self._p_compra)
        else:
            self._tax = 0.30 * (self._p_venda - self._p_compra)
    
    def modify_tax(self, correcao):
        self._tax *= correcao

class Author:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email
        self._titulos = []

    def add_book(self, book):
        self._titulos.append(book)
    
class Client:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email
        self._historico = {}

    def add_purchase(self, _purchase):
        if _purchase._product in self._historico:
            self._historico[_purchase._product] += _purchase._quantity
        else:
            self._historico[_purchase._product] = _purchase._quantity

class PurchaseOrder:
    def __init__(self, product, quantity):
        self._product = product
        self._quantity = quantity

def main():

    print("")

    author_ex = Author("Oliver Blanchard", "blanchard@gmail.com")
    book_ex = Book("Macroeconomics", "Oliver Blanchard", "Academico", "8", "Moderna", 300, 250)
    client_ex = Client("Bryan", "bryan@gmail.com")
    purchaseOrder_ex = PurchaseOrder(book_ex, 2)

    MyLibrary = Library()

    author_ex.add_book(book_ex)
    client_ex.add_purchase(purchaseOrder_ex)

    MyLibrary.add_book(book_ex)
    MyLibrary.add_client(client_ex)
    MyLibrary.add_purchaseOrder(purchaseOrder_ex)

    MyLibrary.consult_book(book_ex)
    MyLibrary.consult_client(client_ex)
    MyLibrary.consult_purchaseOrder(purchaseOrder_ex)

    print("")
    print("---- COMPRA REALIZADA ----")
    for key in client_ex._historico:
        print("Titulo: " + key._titulo)
        print("Quantidade: " + str(client_ex._historico[key]))
    print("")

if __name__ == "__main__":
    main()