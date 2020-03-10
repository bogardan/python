user_input=input("Введите элементы списка через пробел: ")
user_list = user_input.split()
print("Ваш исходный список:", user_list)
print ("Ваш новый сокращенный и пронумерованный список")
for idx, itm in enumerate(user_list,1):
    print(idx,":",itm[0:10])
