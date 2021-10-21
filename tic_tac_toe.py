"""
Игра Крестики нолики
"""
"""
Правила игры:
Игровое поле 3х3
участвуют 2 игрока
игроки ходят поочереди
каждый игрок имеет индивидуальный символ который ставит на свободную ячейку игрового поля
Победитель определяется по следующим правилам:
символ игрока заполняет горизонталь, вертикаль или диагональ

возможный исход игры когда нет победителя
"""
# TODO: Играть с компуктером
# TODO: Игровое поле в виде Матрицы 3на3 не изменяемо. 
# TODO: Ячейка игрового поля будет изменяться, 
"""(
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
)"""
# TODO: Игрок Словарь - ТИП пользователя

# TODO: Управляющий игрой распорядитель

# TODO: Функция матчинга игрового поля на наличие победителя
# TODO: Определение возможности хода
# TODO: Функция Взаимодействия с пользователем на предмет хода
# TODO: Функция совершения хода записывает на игровое поле в ячейку самого пользователя

interface_string = {
    "rules": "",
    "hello": "Здравствуй игрок",
    "enter_name": "Игрок #{user_number}: Введите свое имя",
    "game_type": "С кем вы желаете играть {variants}",
    "ask_step": "Ход #{step_number} игрока {name}",
    "win": "Победил игрок {name} на ходу #{step_number}",
    "new_game": "Желаете начать новую игру? {variants}",
    "draw": "Ничья победителей нет"
}

template_variants = {
    "game_type": lambda template, **kwargs: template.format(variants=("U", "C")),
    "ask_step": lambda template, **kwargs: template.format(**kwargs),
    "win": lambda template, **kwargs: template.format(**kwargs),
    "new_game": lambda template, **kwargs: template.format(variants=("Y", "N")),
    "enter_name": lambda template, **kwargs: template.format(**kwargs),
}

game_type = {
    "U": lambda x: " ",
    "C": lambda x: " "
}


def user_interface(template_name, **template_vars):
    if template_name in template_variants:
        ask_str = template_variants[template_name](interface_string[template_name], **template_vars)
        user_input = input(ask_str)
        return user_input
    else:
        print(interface_string[template_name])


def matrix_match(board):
    def chek_line(line):
        line_set = set(line)
        if (0 not in line_set and len(line_set) == 1):
            raise ValueError("CHECK_LINE")
        return False

    board_len = len(board)
    diagonal = map(lambda idx: board[idx][idx], range(0, board_len))
    diagonal_invert = map(lambda idx: board[idx][board_len - idx - 1], range(board_len - 1, -1, -1))
    try:
        _ = any(map(chek_line, (diagonal, diagonal_invert)))
        for row, column in zip(board, zip(*board)):
            _ = any(map(chek_line, (row, column)))
    except ValueError as exc:
        if 'CHECK_LINE' in exc.args:
            return True
        else:
            raise exc
    return False


def game(users: list, board):
    # 1 должна циклично итерироваться по пользователям либо написать свой цикличный итератор либо найти его в itertools
    # Опрашивать пользователя на предмет хода
    # Проверяем возможность хода
    # Проверяем выйгрышный вариант
    # Либо поздравить с победой, либо обьявить Ничью
    pass


def main():
    pass


print("hello")

main()
