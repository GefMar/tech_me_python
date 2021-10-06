"""
Даны кортеж пользователей users и набор шаблонов templates
Задача обращаясь по индексу к кортежу пользователей напечатать на экране сообщение
если пользователю менее 7 лет: "{name} {surname} закончил школу"
Внимание конструкцию IF ELSE мы не используем (мы ее еще не изучали, и даже если знаете не используйте)
"""

users = (
    {
        "name": "Jon",
        "surname": "Smith",
        "age": 6,
    },
    {
        "name": "Bill",
        "surname": "Suns",
        "age": 20,
    }
)

templates = (
    "{name} {surname} закончил школу",
    "{name} {surname} скоро пойдет в школу",
)

result = templates[users[0]["age"] < 7].format(
    name=users[0]["name"],
    surname=users[0]["surname"],
)
print(result)

result = templates[users[1]["age"] < 7].format(
    name=users[1]["name"],
    surname=users[1]["surname"],
)
print(result)

text = """@*гда я п^ижимал тебя к г^уди св*ей-
Любви и счастья п*лн и п^ими^ен с судьб*ю-
Я думал: т*льк* сме^ть нас ^азлучит с т*б*ю;
+* в*т ^азлучены мы завистью людей!

Пускай тебя навек- п^елестн*е с*зданье-
&тт*^гла зл*ба их *т се^дца м*ег*;
+*- ве^ь- им не изгнать тв*й *б^аз из нег*-
П*ка не пал тв*й д^уг п*д б^еменем ст^аданья!

И если ме^твецы п^иют п*кинут св*й
И к вечн*й жизни п^ах из тленья в*з^*дится-
&пять чел* м*е на г^удь тв*ю скл*нится:
+ет ^ая для меня- где нет тебя с* мн*й!"""

crypto_keys = (("К", "@",), ("р", "^",), (",", "-"), ("c", "$"), ("О", "&",), ("Н", "+"), ("о", "*"))

result = text.replace(
    crypto_keys[0][-1], crypto_keys[0][0]
).replace(
    crypto_keys[1][-1], crypto_keys[1][0]
).replace(
    crypto_keys[2][-1], crypto_keys[2][0]
).replace(
    crypto_keys[3][-1], crypto_keys[3][0]
).replace(
    crypto_keys[4][-1], crypto_keys[4][0]
).replace(
    crypto_keys[5][-1], crypto_keys[5][0]
).replace(
    crypto_keys[6][-1], crypto_keys[6][0]
)
print(result)

"""
3 Даны 2 списка и список чисел, написать процедуру и распределить числа по спискам
числа четные должны попасть в список even, числа нечетные должны попасть в список odd
"""
numbers = [44, 22, 54, 87, 345, 912, 654, 18, 33, 76, 11]
even = []
odd = []

temporary = (even, odd)

temporary[numbers[0] & 1].append(numbers[0])
temporary[numbers[1] & 1].append(numbers[1])
temporary[numbers[2] & 1].append(numbers[2])
temporary[numbers[3] & 1].append(numbers[3])
temporary[numbers[4] & 1].append(numbers[4])
temporary[numbers[5] & 1].append(numbers[5])
temporary[numbers[6] & 1].append(numbers[6])
temporary[numbers[7] & 1].append(numbers[7])
temporary[numbers[8] & 1].append(numbers[8])
temporary[numbers[9] & 1].append(numbers[9])
temporary[numbers[10] & 1].append(numbers[10])

print(even)
print(odd)
