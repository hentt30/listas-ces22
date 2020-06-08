class MyAccount():
    def __init__(self):
        self.balance = 0
        self.statement = []
        self.my_account = 1234

    def make_transaction(self, account, value):
        """Realizar a transação"""
        self.statement.append((account, value))

        if (account == self.my_account):
            self.balance += value

        return f"Transação de valor {value} feita para a conta {account} realizada com sucesso!!"

    def get_balance(self):
        return f""" 
        Sua conta eh : {self.my_account}
        Seu saldo eh : {self.balance}
        """

    def verify_statement(self):
        if (len(self.statement) is 0):
            return "Nenhuma transação feita"
        hist = ""
        for item in self.statement:
            hist += f"Transacao para a conta {item[0]} no valor de {item[1]} \n"
        return hist