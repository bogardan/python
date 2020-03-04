user_number = input("Введите целое положительное число ")
max = user_number[0]
pos = 0
if str(user_number).isdigit():
    while pos < len(str(user_number)):
        if int(user_number[pos]) > int(max):
            max = user_number[pos]
        pos = pos + 1
    print("Максимальная цифра в вашем числе", max)
else:
    print("Вы ввели не число")

