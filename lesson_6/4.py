'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
 Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
 Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
 Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''

import random


class Car():
    speed = None

    def __init__(self, color: str, name: str, is_police: bool):
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def direction(self):
        print(random.choice(["Left", "Right"]))

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    __max_speed = 60

    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = self.__max_speed
        super().__init__(color, name, is_police)

    def show_speed(self):
        self.speed = random.randint(0, 150)
        if self.speed > self.__max_speed:
            print(f"Скорость - {self.speed} км/ч, превышаем")
        else:
            print(self.speed)


class SportCar(Car):
    __max_speed = 360

    def __init__(self, color: str, name: str, is_police: bool):
        super().__init__(color, name, is_police)


class WorkCar(Car):
    __max_speed = 40

    def __init__(self, color: str, name: str, is_police: bool):
        super().__init__(color, name, is_police)

    def show_speed(self):
        self.speed = random.randint(0, 150)
        if self.speed > self.__max_speed:
            print(f"Скорость - {self.speed} км/ч, превышаем")
        else:
            print(self.speed)


class PoliceCar(Car):
    __max_speed = 500

    def __init__(self, color: str, name: str, is_police: bool):
        super().__init__(color, name, is_police)


print(1)
