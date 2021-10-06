"""
Ввод данных от пользователя
функция input()
# """
# user_template = (
#     ("name", str),
#     ("surname", str),
#     ("age", int)
# )
# 
# user = {}
# input_data = input(user_template[0][0])
# 
# """
# isinstance(data, type_func) bool === type(data) == type_func
# """
# 
# if not isinstance(input_data, user_template[0][1]):
#     print("ОШИБКА ПРИ ВВОДЕ ПОЛЯ", user_template[0][0])
# 
# user[user_template[0][0]] = user_template[0][1](input_data)
# 
# input_data = input(user_template[1][0])
# if not isinstance(input_data, user_template[1][1]):
#     print("ОШИБКА ПРИ ВВОДЕ ПОЛЯ", user_template[1][0])
# user[user_template[1][0]] = user_template[1][1](input_data)
# 
# input_data = input(user_template[2][0])
# 
# if not input_data.isdigit():
#     print("ОШИБКА ПРИ ВВОДЕ ПОЛЯ", user_template[2][0])
# user[user_template[2][0]] = user_template[2][1](input_data)
# 
# print(user)

# 
# if 2 > 5:
#     pass
# elif 2 >= 2: # else if
#     pass
# elif 2 >= 2: # else if
#     pass
# elif 2 >= 2: # else if
#     pass
# elif 2 >= 2: # else if
#     pass
# else:
#     pass
# 
# user = {}
# 
# name = input("ваше имя:\n>>")
# age = int(input("сколько вам лет:\n>>"))
# 
# if age <= 12:
#     print("Доступны только мультики")
# elif age < 18:
#     print("Доступны боевики")
# elif age >= 18:
#     print("Доступен раздел ХХХ")

"""
>
<
>=
<=
==
!=
is
not
is not
and
or
"""

# num = int(input("ЧИСЛО"))
"""
вывести на экран FUZZ если число кратно 3 или вывести BUZZ если число кратно 5 или FUZZBUZZ если кратно и 3 и 5 
Во всех остальных случаях вывести само число
"""
# result = num
# if not (num % 3) and not (num % 5):
#     result = "FUZZBUZZ"
# elif not (num % 3):
#     result = "FUZZ"
# elif not (num % 5):
#     result = "BUZZ"
# 
# result = "Fuzz" * (not (num % 3)) + "Buzz" * (not (num % 5)) or num
# print(result)
# 
# ruls = (
#     "some",
#     "some1",
#     "some2",
# )
# 
# print(
#     "hello",
#     "world"
# )

# 
# if 2 > 1:
#     if 2 > 3:
#         if 2 > 4:
#             pass

# n = 500
# 
# while n >= 0:
#     if not (n % 3):
#         n -= 1
#         continue
#     elif not (n % 11):
#         break
#     print(n)
#     n -= 1
# else:
#     print("ELSE")


# user_template = (
#     ("name", str),
#     ("surname", str),
#     ("age", int)
# )


# 
# user_template = (
#     {
#         "title": "name",
#         "type": str,
#         "error": "Ошибка ввода Имени",
#         "input_string": "Представьтесь"
#     },
#     {
#         "title": "age",
#         "type": int,
#         "error": "Ошибка ввода Возраста, вводите только число",
#         "input_string": "Сколько вам лет?"
#     },
#     {
#         "title": "weight",
#         "type": int,
#         "error": "Ошибка ввода Веса, вводите только число",
#         "input_string": "Сколько вы весите?"
#     },
# {
#         "title": "city",
#         "type": str,
#         "error": "нет такого города",
#         "input_string": "Город Рождения"
#     },
# 
# )
# user = {}
# 
# template_count = len(user_template)
# error_count = 0
# n = 0
# while n < template_count:
#     field_template = user_template[n]
#     # "{}\n>>".format(field_template["input_string"])
#     user_input = input(f'{field_template["input_string"]}\n>>>')
#     error = False
#     if field_template["type"] is not int:
#         pass
#     elif field_template["type"] is int and not user_input.isdigit():
#         error = not error
#         error_count += 1
#     if error:
#         if error_count >= 5:
#             print("Доступ заблокирован")
#             break
#         print(field_template["error"])
#         continue
# 
#     user[field_template["title"]] = field_template["type"](user_input)
#     n += 1
#     error_count = 0
# else:
#     print("АВТОРИЗИРОВАН")
#     print(user)


"""
Пользователь вводит целые числа через пробел, посчитать сумму чисел и вывести на экран
"""
# 
# user_input = input("Введите числа через пробел")
# user_input = user_input.split(" ")
# result = 0
# while user_input:
#     data = user_input.pop()
#     if not data.isdigit():
#         print("Ошибка ввода")
#         break
#     result += int(data)
# else:
#     print(result)


user_input = input("введите число")
flg = user_input.isdigit()
if not flg:
    a = user_input.split(".")
    flg = len(a) == 2
    while a and flg:
        data = a.pop()
        flg = data.isdigit()
if flg:
    user_num = float(user_input)
    print(user_num)
else:
    print("ОШИБКА ВВОДА")

