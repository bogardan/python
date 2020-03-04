my_int = input("Введите число: ")
if str(my_int).isdigit():
    print (f"Вы ввели число: {my_int}")
    my_string = input("Введите \"Д\" или \"Н\" для подтверждения")
    if my_string == "Д":
        print ("Ура, все правильно")
    elif my_string == "Н":
        print ("Странно, такого быть не может, надо подумать")
    else:
        print ("Промахнулись")
else:
    print ("Эх, это совсем не число! Прощайте!")