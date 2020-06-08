from pizza import *

## Encapsulamento
pepperoni_pizza = Oregano(Pepperoni(Cheese(TomatoSauce(Mass(Box())))))

## Se aproveita do encapsulamento para calcular o custo total
print(
    f"{pepperoni_pizza.getDescription()}  : R$ {pepperoni_pizza.getTotalCost()}"
)

bacon_tomato_pizza = Oregano(Tomato(Bacon(Cheese(TomatoSauce(Mass(Box()))))))

print(
    f"{bacon_tomato_pizza.getDescription()} : R$ {bacon_tomato_pizza.getTotalCost()}"
)
