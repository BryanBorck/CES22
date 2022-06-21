import abc
import random

class User:
    # Aqui verifica-se se é usuário e/ou admin

    def __init__(self, isAuthor, isAdmin, isApproved, isExpired):
        self.isAuthor = isAuthor
        self.isAdmin = isAdmin
        self.isApproved = isApproved
        self.isExpired = isExpired

class Document:
    # Aqui é basicamente a classe do Documento em si, performando as transições

    _state = None

    def __init__(self, state, user):
        self._state = state
        self._state.document = self
        self._state.user = user
        self.render()
        self.publish()

    def changeState(self, state):
        self._state = state
        self._state.document = self
        self._state.user = user
        if (type(state).__name__ == "DraftState"):
            print("")
            print("--- New Document ---")
            print("")
            self._state.user.isApproved = random.choice([True, False])
            self._state.user.isExpired = random.choice([True, False])
        self.render()
        self.publish()

    def render(self):
        self._state.render()

    def publish(self):
        self._state.publish()


class State(abc.ABC):
    # Aqui a definição abstrata do estado

    @property
    def document(self):
        return self._document

    @document.setter
    def document(self, document):
        self._document = document

    @abc.abstractmethod
    def render(self):
        pass

    @abc.abstractmethod
    def publish(self):
        pass

class DraftState(State):
    # Aqui render certifica a validade e publish avança para prox estado

    def render(self):
        if (self.user.isAdmin or self.user.isAuthor):
            print("DraftState renders the document.")
        else:
            print("Error: Invalid Document.")
            self.document.changeState(InvalidState())
            

    def publish(self):
        if (self.user.isAdmin):
            print("--- Published by admin ---")
            print("DraftState changes to PublishedState.")
            self.document.changeState(PublishedState())
        else:
            print("--- Published by user ---")
            print("DraftState changes to ModerationState.")
            self.document.changeState(ModerationState())


class ModerationState(State):
    # Aqui render não faz nada e publish verifica a aprovação do doc

    def render(self):
        pass

    def publish(self):
        if (self.user.isApproved):
            print("--- Approved by admin ---")
            print("ModerationState changes to PublishedState.")
            self.document.changeState(PublishedState())
        else:
            print("--- Review Failed ---")
            print("ModerationState changes to DraftState.")
            self.document.changeState(DraftState())

class PublishedState(State):
    # Aqui render não faz nada e publish verifica se a publicação foi expirada

    def render(self):
        pass

    def publish(self):
        if (self.user.isExpired):
            print("--- Publication Expired ---")
            print("PublishedState changes to DraftState.")
            self.document.changeState(DraftState())
        else:
            print("--- Sucessful Publication ---")
            pass

class InvalidState(State):
    # Chegando aqui o algoritmo para por ser inválido

    def render(self):
        pass

    def publish(self):
        pass


if __name__ == "__main__":
    # The client code.
    # Aqui eu defini variáveis iniciais dos tomadores de decisão,
    # mas perceba que quando ele volta ao DraftState automaticamente
    # isso muda aleatoriamente

    user = User(True, False, True, True)

    print("")
    print("--- New Document ---")
    print("")

    document = Document(DraftState(), user)

    print("")