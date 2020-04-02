'''
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
'''

class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                user_input = int(input('Введите число, и нажмите Enter - '))
                self.my_list.append(user_input)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print("Вы ввели не число")
                choice = input(f'Продолжить? Y/N ')

                if choice == 'Y' or choice == 'y':
                    print(try_except.my_input())
                elif choice == 'N' or choice == 'n':
                    return print("Exit")
                else:
                    return print("Exit")

try_except = Error(1)
print(try_except.my_input())