'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

class ZeroDivisionException(ZeroDivisionError):
    pass

try:
    try:
        100 / 0
    except ZeroDivisionError:
        raise ZeroDivisionException('Деление на ноль запрещено')
except ZeroDivisionException as error:
    print(error)
    exit(1)