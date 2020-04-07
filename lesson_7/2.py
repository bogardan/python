'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

class Wear():
    title = None

class Coat(Wear):
    def __init__(self,title: str, size: int):
        self.title = title
        Wear.title = title
        self.size = size
    @property
    def quantity(self):
        return self.size/6.5 + 0.5

class Suit(Wear):
    def __init__(self,title: str, growth: int):
        self.title = title
        Wear.title = title
        self.growth = growth
    @property
    def quantity(self):
        return 2 * self.growth/6.5 + 0.3


print(1)