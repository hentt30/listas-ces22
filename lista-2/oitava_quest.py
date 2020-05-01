from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_noise(self):
        pass


class Dog(Animal):
    like_bone = True

    @staticmethod
    def birth_date():
        print("Yesteday")

    def make_noise(self):
        print("Au Au")

    @classmethod
    def dont_like_bone(cls):
        cls.like_bone = False


# métodos estáticos :Podemos acessar sem instanciar um objeto
print("######## FUNCIONAMENTO DOS MÉTODOS ESTÁTICOS ########")
Dog.birth_date()


# métodos abstratos: É possível que a mesmafunção tenha duas implementações diferentes em classes filhas(polimorfismo)
print("######## FUNCIONAMENTO DOS MÉTODOS ABSTRATOS########")
dog = Dog()
dog.make_noise()

# métodos da classe: Recebem uma instância para a classe e podem alterar todos os objeto
print("######## FUNCIONAMENTO DOS MÉTODOS DE CLASSE########")
dog1 = Dog()
dog2 = Dog()

dog1.dont_like_bone()

print(dog1.like_bone)
print(dog2.like_bone)
