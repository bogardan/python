'''
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery():
    title = None
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def __init__(self,title : str):
        self.title = title
    def draw(self):
        print(f"Ручка")

class Pencil(Stationery):
    def __init__(self,title : str):
        self.title = title
    def draw(self):
        print(f"Карандаш")

class Handle(Stationery):
    def __init__(self,title : str):
        self.title = title
    def draw(self):
        print(f"Маркер")

print(1)