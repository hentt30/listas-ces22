from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_noise(self):
        pass
# Polimorfismo
class Dog(Animal):
    def make_noise(self):
        print("Au Au")
class Cow(Animal):
    def make_noise(self):
        print("Moo Moo")

#duck typing
for obj in Cow(),Dog():
    obj.make_noise()


