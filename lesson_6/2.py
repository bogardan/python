'''
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
'''
class Road():
    _length = 0
    _width = 0
    def __init__(self,leng: int, wid: int):
        self._length = leng
        self._width = wid
    def weigth(self):
        one_sm_weight = 25
        all_sm = 5
        all_weight = self._length * self._width * one_sm_weight * all_sm
        print(all_weight)

print(1)
