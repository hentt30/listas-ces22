from abc import ABCMeta, abstractstaticmethod


class ICommand(metaclass=ABCMeta):
    """Interface para os comandos que serão implementados"""
    @abstractstaticmethod
    def execute(self):
        """ Método que será usado pelos objetos de comando"""


class VerifyBalance(ICommand):
    """Objeto que representa o comando que verifica o saldo"""
    def __init__(self, server):
        self.server = server

    def execute(self):
        return self.server.get_balance()


class MakeTransaction(ICommand):
    """Objeto que representa o comando fazer transação"""
    def __init__(self, server):
        self.server = server

    def execute(self, account, value):
        return self.server.make_transaction(account, value)


class VerifyStatement(ICommand):
    """Objeto que verifica o comando verificar extrato"""
    def __init__(self, server):
        self.server = server

    def execute(self):
        return self.server.verify_statement()


class Bank:
    """ The invoker """
    def __init__(self):
        ## Private variables
        self._commands = {}

    def register(self, command_name, command):
        """Registrar comandos"""
        self._commands[command_name] = command

    def execute(self, command_name, account=0, value=0):
        """Executa o comando solicitado"""
        if command_name in self._commands.keys():
            if (command_name is "make_transaction"):
                return self._commands[command_name].execute(account, value)
            return self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not recognised")
