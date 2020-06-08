from server.my_account import MyAccount
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, StringVar
from command import *


class BankGUI:
    def __init__(self, master):
        ## Inicializando  a aplicação e definindo um título para ela
        self.master = master
        self.master.geometry("700x500")
        ## Definindo o servidor
        self.server = MyAccount()
        ## Construindo a interface para os comandos
        self.Bank = Bank()
        self.command_interface()

        ## Variável que mostrará o resultado das operações
        master.title("Bank")

        ## Título das aplicações
        self.label = Label(master, text="Sistema bancário")

        ## Setando o resultado das operações
        self.total = "Resutado das operações"
        self.total_label_text = StringVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        ## Definindo as configurações das entradas
        self.account_entry = Entry(master)
        self.value_entry = Entry(master)

        self.account_text = StringVar()
        self.account_text.set("conta: ")
        self.label_account = Label(master,
                                   textvariable=self.account_text,
                                   height=1)

        self.value_text = StringVar()
        self.value_text.set("  valor: ")
        self.label_value = Label(master,
                                 textvariable=self.value_text,
                                 height=1)

        ## Definindo as configurações dos botões
        self.statement_button = Button(
            master,
            text="Extrato",
            command=lambda: self.update("verify_statement"),
            height=1,
            width=10)
        self.balance_button = Button(
            master,
            text="Saldo",
            command=lambda: self.update("get_balance"),
            height=1,
            width=10)
        self.transaction_button = Button(
            master,
            text="Transação",
            command=lambda: self.update("make_transaction"),
            height=1,
            width=10)

        ## Making Layout
        self.set_layout()

    def set_layout(self):
        """Set the application layout"""
        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=4, column=0, columnspan=2, sticky=W)

        self.label_account.grid(row=3, column=1)
        self.label_value.grid(row=3, column=6)
        self.account_entry.grid(row=3, column=2, columnspan=3, sticky=W + E)
        self.value_entry.grid(row=3, column=7, columnspan=3, sticky=W + E)

        self.statement_button.grid(row=1, column=0)
        self.balance_button.grid(row=2, column=0)
        self.transaction_button.grid(row=3, column=0)

    def command_interface(self):
        self.Bank.register("make_transaction", MakeTransaction(self.server))
        self.Bank.register("verify_statement", VerifyStatement(self.server))
        self.Bank.register("get_balance", VerifyBalance(self.server))

    def update(self, command_name):
        if (command_name is "make_transaction"):
            if (self.account_entry.get() is ""
                    or self.value_entry.get() is ""):
                self.total = "Um dos campos não foi informado"
            else:
                try:
                    account = int(self.account_entry.get())
                    value = float(self.value_entry.get())
                    self.total = self.Bank.execute(command_name, account,
                                                   value)
                except:
                    self.total = "Entradas inválidas"
        else:
            self.total = self.Bank.execute(command_name)

        self.total_label_text.set(self.total)
        self.account_entry.delete(0, END)
        self.value_entry.delete(0, END)


root = Tk()
my_gui = BankGUI(root)
root.mainloop()