from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel

"""
доработайте базовый класс `base.Vehicle`:
    - добавьте атрибуты `weight`, `started`, `fuel`, `fuel_consumption` со значениями по умолчанию
    - добавьте инициализатор для установки `weight`, `fuel`, `fuel_consumption`
    - добавьте метод `start`. При вызове этого метода необходимо проверить состояние `started`. И если не `started`, то нужно проверить, что топлива больше нуля, 
      и обновить состояние `started`, иначе нужно выкинуть исключение `exceptions.LowFuelError`
    - добавьте метод `move`, который проверяет, 
      что топлива достаточно для преодоления переданной дистанции (вплоть до полного расхода), 
      и изменяет количество оставшегося топлива, иначе выкидывает исключение `exceptions.NotEnoughFuel`
"""


class Vehicle(ABC):
    weight: int = 2500
    started: bool = False
    fuel: float = 45
    fuel_consumption: float = 9.5


    def __init__(self, w: int, f: float, fc: float):
        self.weight = w
        self.fuel = f
        self.fuel_consumption = fc

    def start(self) -> True:
        if not self.started:
            if self.fuel <= 0:
                raise LowFuelError
        self.started = True
        return True

    def move(self, distance: float):
        if self.fuel < self.fuel_consumption * distance:
            raise NotEnoughFuel

        self.fuel -= distance * self.fuel_consumption
        return True
