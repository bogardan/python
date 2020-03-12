start_list = [15,11,11,9,7,5,3,3,2]
user_input = input("Введите число рейтинга: ")
print("Начальный список:", start_list)
if user_input.isdigit():
    reverse_list = start_list[::-1]
    if reverse_list.count(int(user_input)):
        reverse_list.insert(reverse_list.index(int(user_input)),int(user_input))
    else:
        for idx in range(0, len(reverse_list)):
            if int(reverse_list[idx]) < int(user_input) and int(reverse_list[idx+1]) > int(user_input):
                reverse_list.insert(idx+1,int(user_input))
            elif max(reverse_list) < int(user_input):
                reverse_list.append(int(user_input))
    print("Преобразованный список: ", reverse_list[::-1])
else:
    print("Вы ввели не число")
