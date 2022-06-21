import abc
import tkinter as tk
from tkinter import *

class Command(abc.ABC):
    # Comando abstrato associado aos botões

    def __init__(self, receiver):
        self.receiver = receiver
      
    def process(self):
        pass
  
class VerificationCommand(Command):
    # Comando de verificar saldo

    def __init__(self, receiver):
        self.receiver = receiver
        self.balance = receiver.balance
  
    def process(self):
        self.receiver.perform_verification(self.balance)
        return self.balance

class AdditionCommand(Command):
    # Comando de adicionar (+) dinheiro ao banco (saldo)

    def __init__(self, receiver, sum_factor):
        self.receiver = receiver
        self.balance = receiver.balance
        self.sum_factor = sum_factor
  
    def process(self):
        self.balance += self.sum_factor
        self.receiver.perform_addition(self.balance, self.sum_factor)

class WithdrawCommand(Command):
    # Comando de sacar (-) dinheiro ao banco (saldo)

    def __init__(self, receiver, sub_factor):
        self.receiver = receiver
        self.balance = receiver.balance
        self.sub_factor = sub_factor
  
    def process(self):
        self.balance -= self.sub_factor
        self.receiver.perform_withdraw(self.balance, self.sub_factor)

class TransferCommand(Command):
    # Comando de transferir (-) dinheiro para alguém (saldo)

    def __init__(self, receiver, factor, destiny, Ttype):
        self.receiver = receiver
        self.balance = receiver.balance
        self.factor = factor
        self.destiny = destiny
        self.type = Ttype
  
    def process(self):
        if (self.type == "+"):
            self.balance += self.factor
        else:
            self.balance -= self.factor
        self.receiver.perform_transfer(self.balance, self.factor, self.destiny, self.type)

class ExtractCommand(Command):
    # Comando de verificar saldo

    def __init__(self, receiver):
        self.receiver = receiver
  
    def process(self):
        self.receiver.perform_extract()
  
class Receiver:
    # Basicamente o Receiver aqui vai fazer o papel de histórico de operações, além de printar cada uma
    # Optei por implementar no caso o Cliente dentro do Receiver

    def __init__(self, balance, lst):
        self.lst = lst
        self.balance = balance

    def perform_verification(self, new_balance):
        self.balance = new_balance
        # self.lst.append(f"Verific.:              Balance: R$ {self.balance:05.2f}")
        print(f"\nReceiver: Verification realized = R$ {self.balance:05.2f}", end="")
    
    def perform_addition(self, new_balance, sum_factor):
        self.balance = new_balance
        self.lst.append(f"Addition: + R$ {sum_factor:05.2f}   Balance: R$ {self.balance:05.2f}")
        print(f"\nReceiver: Addition realized (+ R$ {sum_factor:05.2f}) = R$ {self.balance:05.2f}", end="")
    
    def perform_withdraw(self, new_balance, sub_factor):
        self.balance = new_balance
        self.lst.append(f"Withdraw: - R$ {sub_factor:05.2f}   Balance: R$ {self.balance:05.2f}")
        print(f"\nReceiver: Withdraw realized (- R$ {sub_factor:05.2f}) = R$ {self.balance:05.2f}", end="")
    
    def perform_transfer(self, new_balance, factor, destiny, Ttype):
        self.balance = new_balance
        if (Ttype == "+"):
            print(f"\nReceiver: Transfer from {destiny} (+ R$ {factor:05.2f}) = R$ {self.balance:05.2f}", end="")
            self.lst.append(f"Transfer: + R$ {factor:05.2f}   Balance: R$ {self.balance:05.2f}")
        else:
            print(f"\nReceiver: Transfer to {destiny} (- R$ {factor:05.2f}) = R$ {self.balance:05.2f}", end="")
            self.lst.append(f"Transfer: - R$ {factor:05.2f}   Balance: R$ {self.balance:05.2f}")

    def perform_extract(self):
        print(f"\nReceiver: Extract realized", end="")
        print("\n")
        for element in self.lst:
            print(element)
        print(f"***************\ Final Balance: R$ {self.balance:05.2f}")
        print("")

class Invoker:
    # O invoker será utilizado no momento do event-handler do botão      

    def command(self, cmd):
        self.cmd = cmd
  
    def execute(self):
        self.cmd.process()


#########################################################################
# Aqui começa o código em Tkinter para o App


global_balance = 0
global_lst = []

receiver = Receiver(global_balance, global_lst)
invoker = Invoker()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.menu_label = tk.Label(self)
        self.menu_label["text"] = "Bem-vindo ao Banco Seno"
        self.menu_label["fg"] = "blue"
        self.menu_label["bg"] = "white"
        self.menu_label["font"] = ("Arial", 10)
        self.menu_label["height"] = 2
        self.menu_label["width"] = 50
        self.menu_label.pack()

        self.verification = tk.Button(self)
        self.verification["text"] = "Verificar Saldo"
        self.verification["command"] = self.verification_cmd
        self.verification["height"] = 2
        self.verification.pack(fill=tk.X)

        self.addition = tk.Button(self)
        self.addition["text"] = "Adicionar ao Saldo"
        self.addition["command"] = self.addition_cmd
        self.addition["height"] = 2
        self.addition.pack(fill=tk.X)

        self.withdraw = tk.Button(self)
        self.withdraw["text"] = "Realizar Saque"
        self.withdraw["command"] = self.withdraw_cmd
        self.withdraw["height"] = 2
        self.withdraw.pack(fill=tk.X)

        self.transfer = tk.Button(self)
        self.transfer["text"] = "Realizar Transferência para ____"
        self.transfer["command"] = self.transfer_cmd
        self.transfer["height"] = 2
        self.transfer.pack(fill=tk.X)

        self.transferA = tk.Button(self)
        self.transferA["text"] = "Realizar Transferência de ____"
        self.transferA["command"] = self.transferA_cmd
        self.transferA["height"] = 2
        self.transferA.pack(fill=tk.X)

        self.extract = tk.Button(self)
        self.extract["text"] = "Ver Extrato da Conta"
        self.extract["command"] = self.extract_cmd
        self.extract["height"] = 2
        self.extract.pack(fill=tk.X)

        self.entry_label = tk.Label(self)
        self.entry_label["text"] = "Digite o valor da operação abaixo (int):"
        self.entry_label["fg"] = "white"
        self.entry_label["bg"] = "#808080"
        self.entry_label["height"] = 2
        self.entry_label["font"] = ("Arial", 8)
        self.entry_label.pack(fill=tk.X)

        self.entry = tk.Entry(self)
        self.entry["fg"] = "black"
        self.entry["bg"] = "white"
        self.entry["justify"] = CENTER
        self.entry.pack(fill=tk.X)

        self.entryW_label = tk.Label(self)
        self.entryW_label["text"] = "Escreva o nome relativo à transferência:"
        self.entryW_label["fg"] = "white"
        self.entryW_label["bg"] = "#808080"
        self.entryW_label["height"] = 2
        self.entryW_label["font"] = ("Arial", 8)
        self.entryW_label.pack(fill=tk.X)

        self.entryW = tk.Entry(self)
        self.entryW["fg"] = "black"
        self.entryW["bg"] = "white"
        self.entryW["justify"] = CENTER
        self.entryW.pack(fill=tk.X)

        self.quit = tk.Button(self)
        self.quit["command"] = self.master.destroy
        self.quit["text"] = "SAIR DO BANCO"
        self.quit["fg"] = "blue"
        self.quit.pack(fill=tk.X)

    def verification_cmd(self):
            cmd = VerificationCommand(receiver)
            invoker.command(cmd)
            invoker.execute()

    def addition_cmd(self):
            inputA_val = self.entry.get()
            cmd = AdditionCommand(receiver, int(inputA_val))
            invoker.command(cmd)
            invoker.execute()
    
    def withdraw_cmd(self):
            inputW_val = self.entry.get()
            cmd = WithdrawCommand(receiver, int(inputW_val))
            invoker.command(cmd)
            invoker.execute()

    def transfer_cmd(self):
            inputT_val = self.entry.get()
            inputWT_val = self.entryW.get()
            cmd = TransferCommand(receiver, int(inputT_val), str(inputWT_val), "-")
            invoker.command(cmd)
            invoker.execute()
    
    def transferA_cmd(self):
            inputAT_val = self.entry.get()
            inputAWT_val = self.entryW.get()
            cmd = TransferCommand(receiver, int(inputAT_val), str(inputAWT_val), "+")
            invoker.command(cmd)
            invoker.execute()

    def extract_cmd(self):
            cmd = ExtractCommand(receiver)
            invoker.command(cmd)
            invoker.execute()

root = tk.Tk()
root.geometry("400x450")
app = Application(master=root)
app.master.title("Banco Seno CES 22")
app.mainloop()