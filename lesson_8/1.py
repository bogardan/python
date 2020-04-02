'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''

import time
import datetime

class Date:
    def __init__(self, date: str):
        self.__date = date

    @property
    def date(self):
        try:
            Date.validate_date(self.__date)
        except ValueError as error:
            print(error)
            exit(1)
        else:
            return self.__date

    @classmethod
    def date_to_timestamp(cls, date: str):
        date = Date(date).date
        return int(time.mktime(datetime.datetime.strptime(date, '%Y-%m-%d').timetuple()))

    @staticmethod
    def validate_date(date):
        splitted_date = date.split('-')
        if len(splitted_date[0]) != 4 \
                or len(splitted_date[1]) != 2 or int(splitted_date[1]) < 1 or int(splitted_date[1]) > 12 \
                or len(splitted_date[2]) != 2 or int(splitted_date[2]) < 1 or int(splitted_date[2]) > 31:
            raise ValueError('Given date is incorrect')

print(Date.date_to_timestamp('2000-01-01'))