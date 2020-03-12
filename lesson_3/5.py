def num_func():
    numbers = input("Введите цифры: ")
    return numbers

def main_list(user_input):
    user_list = user_input.split()
    return user_list

def all_sum(sum_list):
        return int(sum_list[0]) + int(all_sum(sum_list[1::])) if sum_list else 0

def user_check():
    text = input("Для продолжения нажмите Enter, для выхода q: ")
    if text == "":
        check = 1
    elif text == "q":
        check = 0
    else:
        check = 2
        print("Вы ввели некорректный ответ")
    return check

result_list = []
result_list = result_list + main_list(num_func())

if result_list.count("q") == 0:
    print("Сумма введенных чисел равна: ", all_sum(result_list))
else:
    result_list.remove("q")
    print("Сумма введенных чисел равна: ", all_sum(result_list))

check = user_check()
while check == 1:
    result_list = result_list + main_list(num_func())
    if result_list.count("q") == 0:
        print(result_list)
        print("Сумма введенных чисел равна: ", all_sum(result_list))
    else:
        result_list.remove("q")
        print("Сумма введенных чисел равна: ", all_sum(result_list))
        break
    print("Сумма введенных чисел равна: ", all_sum(result_list))
    check = user_check()




