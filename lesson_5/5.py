'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
import random
import os
path = os.path.dirname(__file__)

def write_file(input_list):
    with open((os.path.join(path, '5.txt')), "a") as file_w:
        file_w.write("".join(str(input_list))+" ")

a = [random.randint(10,100) for x in range(10,random.randint(10,50))]
for i in a:
    write_file(i)

all_sum = 0
with open((os.path.join(path,'5.txt')), "r") as file_r:
        for line in file_r:
            sum_list = line.split()
        for i in sum_list:
            all_sum = all_sum + int(i)
        print(all_sum)