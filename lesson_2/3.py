input_month = input("Введите порядковый номер месяца от 1 до 12:")
month_dict={'зима': ["1", "2", "12"], 'весна': ["3", "4", "5"], 'лето':["6", "7", "8"], 'осень': ["9", "10", "11"]}
for i in month_dict:
    month_list = month_dict.get(i)
    if month_list.count(input_month):
        print(i)