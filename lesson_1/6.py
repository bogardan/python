start = input("Введите начальное значение ")
end = input("Введите конечное значение ")
day = 1
if str(start).isdigit() and str(end).isdigit():
    if end >= start:
        result = start
        while float(result) < float(end):
            day = day + 1
            result = float(result) + float(result)/10
        print("Номер дня", day)
    else:
        print("Ошибка!Конечное значение больше начального")
else:
    print("Введены некорректные начальные данные")

