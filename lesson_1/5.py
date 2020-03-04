profit = input("Введите значение выручки вашей компании\n")
loss = input("Введите значение издержек вашей компании\n")
if str(profit).isdigit() and str(loss).isdigit():
    if int(profit) >= int(loss):
        print(f"Ваша компания работает в плюс. Рентабельность компании составляет {(int(profit)-int(loss))/int(profit)}")
        workers = input("Введите численность работников\n")
        if str(workers).isdigit():
            print(f"Прибыл на одного сотрудника компании состявляет\n {(int(profit)-int(loss))/int(workers)}")
        else:
            print("Вы ввели некорректное число работников")
    else:
        print("Ваша компания работает в убыток!")
else:
    print("Вы ввели неверные значения для выручки и издержек!")