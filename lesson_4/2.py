"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
"""
import random

r_list = [x for x in range(random.randint(10,40))]
random.shuffle(r_list)
print("Исходный список\n",r_list)
new_list = []
idx = 0
while idx < (len(r_list)-1):
    if r_list[idx] < r_list[idx+1]:
        new_list.append(r_list[idx+1])
        idx += 1
    else:
        idx += 1
print("Новый список\n",new_list)




