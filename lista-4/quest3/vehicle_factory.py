from __future__ import annotations
from abc import ABC, abstractstaticmethod, abstractmethod


class IVehicleFactory(ABC):
    """
        Instanciar a fábrica
    """
    @abstractstaticmethod
    def factory_method(name, color, age, motor, format):
        """
        Método para  contruir o objeto
        """
        pass


class VehicleFactory(IVehicleFactory):
    def factory_method(name, color, age, motor, format):
        try:
            if (format == "TRUCK"):
                return Truck(name, color, age, motor)
            elif (format == "CAR"):
                return Car(name, color, age, motor)
            raise AssertionError("Formato nao disponivel")
        except error:
            print(error)


class Vehicle(ABC):
    """
    Classe abstrata que define os diferentes tipos de veículo.
    """
    def __init__(self, name, color, age, motor) -> None:
        self.name = name
        self.color = color
        self.age = age
        self.motor = motor

    @abstractmethod
    def description(self):
        """
        Fornece uma descrição de alto nível do veiculo
        """
        pass


class Car(Vehicle):
    """
    Define a classe carro que herda da classe vehicle
    """
    def __init__(self, name, color, age, motor):
        super().__init__(name, color, age, motor)

    def description(self):
        """
        Fornece nome, cor idade e tipo da direcao para um carro
        """
        print("#######################")
        print("Ola, eu sou um carro com as seguintes propriedades:")
        print(f"Nome: {self.name}")
        print(f"Cor: {self.color}")
        print(f"Idade: {self.age}")
        print("Direcao:", end="")
        self.motor.description()
        print("#######################")


class Truck(Vehicle):
    def __init__(self, name, color, age, motor):
        """
        Define a classe caminhao que herda da classe vehicle
        """
        super().__init__(name, color, age, motor)

    def description(self):
        """
        Fornece nome, cor idade e tipo da direcao para um caminhao
        """
        print("#######################")
        print("Ola, eu sou um caminhao com as seguintes propriedades:")
        print(f"Nome: {self.name}")
        print(f"Cor: {self.color}")
        print(f"Idade: {self.age}")
        print("Direcao:", end="")
        self.motor.description()
        print("#######################")