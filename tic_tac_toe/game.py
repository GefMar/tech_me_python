from itertools import cycle
from tic_tac_toe.board import get_board, board_match
from tic_tac_toe.steps import get_step, chek_step


def game(users: list[dict], board: list[list]):
    # 1 должна циклично итерироваться по пользователям либо написать свой цикличный итератор либо найти его в itertools
    # Опрашивать пользователя на предмет хода
    # Проверяем возможность хода
    # Проверяем выйгрышный вариант
    # Либо поздравить с победой, либо обьявить Ничью
    for user in cycle(users):
        print(f"Ход Игрока: {user['name']}")
        while True:
            step = get_step()
            if chek_step(board, step):
                board[step[0]][step[1]] = user["symbol"]
                break
            else:
                print("Ячейка не существует или занята")
                continue
        if board_match(board):
            print(f"Победил {user['name']}")
            break
    print("END GAME")


game([{"name": 1, "symbol": "X"}, {"name": 2, "symbol": "O"}], get_board(3))
