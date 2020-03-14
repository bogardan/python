'''
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
'''

from itertools import cycle, count
from time import sleep

for i in count(10):
    print(i)
    sleep(1)
    if i > 15:
        break

a = [1, 2, 3, 4, 5]
for i in cycle(a):
    print(a)
    sleep(1)


