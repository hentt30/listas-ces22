from abc import ABC, abstractmethod


class Motor(ABC):
    """
    Classe abstrata que define os diferentes tipos de motores
    """
    def __init__(self, type) -> None:
        self.type = type

    @abstractmethod
    def description(self):
        """
        Fornece uma descrição de alto nível do motor
        """
        pass


class EletricMotor(Motor):
    """
    Define a classe motor eletrico que herda do motor.
    """
    def __init__(self):
        super().__init__("Eletrico")

    def description(self):
        """
        Fornece descrição do motor elétrico
        """
        print(f"Sou um motor do tipo {self.type}")


class HybridMotor(Motor):
    def __init__(self):
        """
        Define a classe direcao híbrida que herda do motor.
        """
        super().__init__("Hibrido")

    def description(self):
        """
        Fornece descrição do motor híbrido
        """
        print(f"Sou um motor do tipo {self.type}")


class CombustionMotor(Motor):
    def __init__(self):
        """
        Define a classe motor de combustão que herda da classe motor
        """
        super().__init__("Combustao")

    def description(self):
        """
        Fornece descrição do motor a combustão
        """
        print(f"Sou um motor movido a  {self.type}")
