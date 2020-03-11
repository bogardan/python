def div_func(a,b):
    return (int(a)/int(b))

a = input("Введите первое число: ")
b = input("Введите второе число: ")

if str(a).isdigit() and str(b).isdigit() and int(b):
    result = div_func(a,b)
    print(result)
else:
    print("Вы ввели не числа или пытаетесь делить на 0")


