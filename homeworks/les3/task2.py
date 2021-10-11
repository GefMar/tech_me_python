"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
"""

seasons_list = ('зима',
                'весна',
                'лето',
                'осень',
                )
seasons = ('spring', 'summer', 'autumn', 'winter')
repeat = True
error_messages = (
    "Ошибка ввода, введено не число",
    "Ошибка ввода введено недопустимое значение, значение должно быть больше 1 и меньше 13"
)
while repeat:
    user_input = input("введите номер месяца \n>>>")
    if not user_input.isdigit():
        print(error_messages[0])
        continue
    user_month_num = int(user_input)
    if (user_month_num <= 0) or (user_month_num > 12):
        print(error_messages[1])
        continue
    season_idx = user_month_num // 3 % 4
    # season_idx = int(user_month_num / 3)-1
    season = seasons_list[season_idx]
    print(season)
    repeat = not repeat
