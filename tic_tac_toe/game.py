from itertools import cycle
from tic_tac_toe.board import get_board, board_match
from tic_tac_toe.steps import user_step


def game_init():
    pass


def game_end():
    pass


def game_cycle(users: list[dict, ...], board: list[list]):
    # 1 должна циклично итерироваться по пользователям либо написать свой цикличный итератор либо найти его в itertools
    # Опрашивать пользователя на предмет хода
    # Проверяем возможность хода
    # Проверяем выйгрышный вариант
    # Либо поздравить с победой, либо обьявить Ничью
    for step_num, user in enumerate(cycle(users), 1):
        print(f"Ход Игрока: {user['name']}")
        user_step(user, board)
        if board_match(board):
            print(f"Победил {user['name']}")
            break
        if step_num >= 8:
            print("Ничья")
            break
    print("END GAME")


game_cycle([{"name": 1, "symbol": "X"}, {"name": 2, "symbol": "O"}], get_board(3))
