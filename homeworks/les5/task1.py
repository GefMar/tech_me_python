""" 1
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Результатом работы функции должна быть строка 
Пример строки результата: 

Иванов Иван Иванович 1986 года Рождения, проживающий в городе Норильск.
Контактные данные: 
- телефон: 89181111111
- email: test@test.ru
"""


def format_user_data(name, surname, b_date, live_city, email, phone):
    result = f"""{name} {surname} {b_date} года Рождения в городе {live_city}.
Контактные данные:
- телефон: {phone}
- email: {email}"""
    return result


users = {
    "name": "Иван",
    "surname": "Иванов",
    "b_date": 1986,
    "live_city": "Krasnodar",
    "email": "test@test.ru",
    "phone": "+7111777999988",
}

user_str = format_user_data(**users)
user_str2 = format_user_data(
    name=users["name"],
    surname=users["surname"],
    b_date=users["b_date"],
    phone=users["phone"],
    live_city=users["live_city"],
    email=users["email"]
)

print(user_str)
print(user_str2)
