"""
1 Даны кортеж пользователей users и набор шаблонов templates
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

"""
2 Дан зашифрованный текст и набор замен которые использовались для шифрования. 
Написать процедуру и вывести на экран расшифрованный текст

"""

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


"""
3 Даны 2 списка и список чисел, написать процедуру и распределить числа по спискам
числа четные должны попасть в список even, числа нечетные должны попасть в список odd
"""
numbers = [44, 22, 54, 87, 345, 912, 654, 18, 33, 76, 11]
even = []
odd = []

