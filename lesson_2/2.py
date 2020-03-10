user_input=input("Введите элементы списка через пробел: ")
user_list = user_input.split()
print("Ваш исходный список:", user_list)
i = 0
if not len(user_list) % 2:
    while i < (len(user_list)):
        user_list[i], user_list[i+1] = user_list [i+1], user_list[i]
        i = i + 2
#    print(user_list)
else:
    temp = user_list.pop(-1)
    while i < (len(user_list)):
        user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
        i = i + 2
    user_list.append(temp)
print("Ваш список после преобразований:", user_list)





