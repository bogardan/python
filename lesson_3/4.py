'''
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
'''

x=3.22
y=-10

def create_list(x:int,y):
    '''
    Эта функция создает из числа, которое необходимо возвести в степень список длиной, равной модулю второго отрицательного числа
    :param x: действительное положительное число
    :param y: целое отрицательное число
    :return: возвращается список
    '''
    my_list=[x,]
    for i in range(1,abs(y)):
        my_list.append(x)
    return my_list

number_list = create_list(x,y)

def power(number_list):
    '''
    Стандартная функция умножения всех чисел в списке
    :param number_list: передается сформированный в функции create_list список
    :return: возвращается результат умножениявсех чисел в списке
    '''
    power_res = 1
    for number in number_list:
        power_res = power_res * number
    return power_res

result = 1/power(number_list)
print(result)

