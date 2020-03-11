f_name = "Иванов"
s_name = "Иван"
b_year = "1900"
city = "Moscow"
email = "blabla@bla.com"
m_number = "99999999999"

def user_info(**kwargs):
    return kwargs

print(user_info (Имя = f_name, Фамилия = s_name,Год_рождения = b_year, Город=city, email=email, телефон=m_number))


