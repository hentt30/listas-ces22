from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, StringVar

class BankGUI:

    def __init__(self, master):
        self.master = master
        master.title("Bank")

        self.total = "Resutado das operações"
        self.entered_number = 0

        self.total_label_text = StringVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Sistema bancário")

       
        self.account_entry = Entry(master)
        self.value_entry = Entry(master)

        self.statement_button = Button(master, text="Extrato", command=lambda: self.update("add"),height=1,width=10)
        self.balance_button = Button(master, text="Saldo", command=lambda: self.update("subtract"),height=1,width=10)

        self.account_text=StringVar()
        self.account_text.set("conta: ")
        self.label_account=Label(master, textvariable=self.account_text, height=1)

        self.value_text=StringVar()
        self.value_text.set("  valor: ")
        self.label_value=Label(master, textvariable=self.value_text, height=1)
        
        self.transaction_button = Button(master, text="Transação", command=lambda: self.update("reset"),height=1,width=10)

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=4, column=0, columnspan=2, sticky=W)

        self.label_account.grid(row=3,column=1)
        self.label_value.grid(row=3,column=6)
        self.account_entry.grid(row=3, column=2, columnspan=3, sticky=W+E)
        self.value_entry.grid(row=3, column=7, columnspan=3, sticky=W+E)

        self.statement_button.grid(row=1, column=0)
        self.balance_button.grid(row=2, column=0)
        self.transaction_button.grid(row=3, column=0)



    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
my_gui = BankGUI(root)
root.mainloop()