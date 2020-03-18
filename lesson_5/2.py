'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
'''

import os

path = os.path.dirname(__file__)

lines = 0

try:
    with open((os.path.join(path,'2.txt')), "r") as file:
        for line in file:
            lines+=1
            a = line.split()
            print("В", lines, "строке находится", len(a),"слова")
    print("Всего в файле",lines,"строк")
except:
    print("Файл не существует")



