from veiculos import Car, Truck
from motor import EletricMotor, HybridMotor, CombustionMotor
"""
Algo muito importante a se notar nesse exemplo é que conforme cresce o
número de motores e o número de veiculos, o número de classes instanciadas
não cresce exponencialmente. Esse é um problema muito comum que é resolvido pelo design pattern bridge
"""

## Definindo os motores
eletric_motor = EletricMotor()
hybrid_motor = HybridMotor()
combustion_motor = CombustionMotor()

## 6 combinações possíveis
c1 = Car("ford fiesta", "vermelho", "12", eletric_motor)
c2 = Car("palio", "azul", "3", combustion_motor)
c3 = Car("uno", "amarelo", "23", hybrid_motor)

c4 = Truck("volvo", "branco", "23", eletric_motor)
c5 = Truck("mercedes", "ciano", "34", combustion_motor)
c6 = Truck("volksvagem", "verde", "45", hybrid_motor)

## Descrição das seis combinações

c1.description()
c2.description()
c3.description()
c4.description()
c5.description()
c6.description()
