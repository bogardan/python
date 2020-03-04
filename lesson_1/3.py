var_n = input ("Введите произвольное число ")
if str(var_n).isdigit():
    result = int(var_n)+int(var_n*2)+int(var_n*3)
    print(result)
else:
    print ("Вы ввели не число")