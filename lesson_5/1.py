'''
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''
import fileinput

print("Введите данные:")
for fileinput_line in fileinput.input():
    if '' == fileinput_line.rstrip():
        break
    with open('1.txt', 'a') as file:
        file.write(fileinput_line)
print("Проверьте файл с данными")