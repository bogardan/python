user_seconds = input("Введите количество секунд для перевода их в часы ")
if str(user_seconds).isdigit():
    print (f"время - {int(user_seconds)//3600:>02}:{(int(user_seconds)%3600)//60:>02}:{(int(user_seconds)%3600)%60:>02}")
else:
    print ("Вы ввели не число!")
