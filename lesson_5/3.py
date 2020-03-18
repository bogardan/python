'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''
name_dict = {}
with open("3.txt", "r") as file:
    for line in file:
        (key, val) = line.split()
        name_dict[key] = val
print(name_dict)

sum_salary = 0
for key in name_dict:
    sum_salary = sum_salary + int(name_dict[key])
    if int(name_dict[key]) >= 21000:
        print(key)
print(sum_salary)








