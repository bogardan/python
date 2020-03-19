'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
'''

import os
import json
path = os.path.dirname(__file__)
all_dict = {}
with open((os.path.join(path,'7.txt')), "r") as file_r:
    for line in file_r:
        input_list = line.split()
        all_dict.update({input_list[0]: (float(input_list[2]) - float(input_list[3]))})
print(all_dict)
profit = []
minus = []
av_profit = 0
av_minus = 0
plus_dict = {key:value for key, value in all_dict.items() if value > 0}
minus_dict = {key:value for key, value in all_dict.items() if value <= 0}
for key,value in plus_dict.items():
    av_profit = av_profit + value/len(plus_dict)
for key,value in minus_dict.items():
    av_minus = av_minus + value/len(minus_dict)
profit.append(plus_dict)
profit.append({"average_profit":av_profit})
minus.append(minus_dict)
minus.append({"average_minus":av_minus})

with open((os.path.join(path, '7_json_plus.txt')), "w") as file_w:
    json.dump(profit, file_w)
with open((os.path.join(path, '7_json_minus.txt')), "w") as file_w:
    json.dump(minus, file_w)



