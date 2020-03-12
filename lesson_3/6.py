def up_change(in_str):
    up_word = in_str[0].upper()+in_str[1:]
    return up_word

user_string = input("Введите строку: ")
space_count = user_string.count(' ')
str_list = user_string.split()
for i in range(0, space_count+1):
    x = str_list[i]
    y = up_change(x)
    print(''.join(y), end = ' ')