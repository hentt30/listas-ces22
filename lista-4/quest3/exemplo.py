from vehicle_factory import VehicleFactory
from motor_factory import MotorFactory
"""
Algo muito importante a se notar nesse exemplo é que conforme cresce o
número de motores e o número de veiculos, o número de classes instanciadas
não cresce exponencialmente. Esse é um problema muito comum que é resolvido pelo design pattern bridge
"""

## Definindo os motores
eletric_motor = MotorFactory.factory_method("ELETRIC")
hybrid_motor = MotorFactory.factory_method("HYBRID")
combustion_motor = MotorFactory.factory_method("COMBUSTION")

## 6 combinações possíveis
c1 = VehicleFactory.factory_method("ford fiesta", "vermelho", "12",
                                   eletric_motor, "CAR")
c2 = VehicleFactory.factory_method("palio", "azul", "3", combustion_motor,
                                   "CAR")
c3 = VehicleFactory.factory_method("uno", "amarelo", "23", hybrid_motor, "CAR")

c4 = VehicleFactory.factory_method("volvo", "branco", "23", eletric_motor,
                                   "TRUCK")
c5 = VehicleFactory.factory_method("mercedes", "ciano", "34", combustion_motor,
                                   "TRUCK")
c6 = VehicleFactory.factory_method("volksvagem", "verde", "45", hybrid_motor,
                                   "TRUCK")

## Descrição das seis combinações

c1.description()
c2.description()
c3.description()
c4.description()
c5.description()
c6.description()
