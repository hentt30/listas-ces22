class PizzaComponent:
    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost


class Box(PizzaComponent):
    cost = 0.0


class Decorator(PizzaComponent):
    def __init__(self, PizzaComponent):
        self.component = PizzaComponent

    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(
            self)

    def getDescription(self):
        return self.component.getDescription(
        ) + " " + PizzaComponent.getDescription(self)


class Mass(Decorator):
    cost = 0.5

    def __init__(self, PizzaComponent):
        Decorator.__init__(self, PizzaComponent)


class Cheese(Decorator):
    cost = 4.0

    def __init__(self, PizzaComponent):
        Decorator.__init__(self, PizzaComponent)


class Bacon(Decorator):
    cost = 3.0

    def __init__(self, PizzaComponent):
        Decorator.__init__(self, PizzaComponent)


class Pepperoni(Decorator):
    cost = 0.3

    def __init__(self, PizzaComponent):
        Decorator.__init__(self, PizzaComponent)


class TomatoSauce(Decorator):
    cost = 1.5

    def __init__(self, PizzaComponent):
        Decorator.__init__(self, PizzaComponent)


class Tomato(Decorator):
    cost = 2.0

    def __init__(self, PizzaComponent):
        Decorator.__init__(self, PizzaComponent)


class Oregano(Decorator):
    cost = 1.0

    def __init__(self, PizzaComponent):
        Decorator.__init__(self, PizzaComponent)
