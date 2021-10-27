import random


def get_step() -> tuple:
    while True:
        result = []
        input_step = input("Введите координаты хода через пробел\n")
        steps = input_step.split(" ")
        try:
            if len(steps) != 2:
                raise ValueError
            for itm in steps:
                result.append(int(itm))
        except ValueError:
            print("Ошибка ввода, повторите")
            continue
        return tuple(result)


def chek_step(board: list[list], step: tuple) -> bool:
    try:
        cell = board[step[0]][step[1]]
        if not cell:
            return True
    except IndexError:
        print("Неверные координаты")
    return False


def user_step(user: dict, board: list[list]):
    if user["user_type"] == "COMP":
        step = auto_step(user, board)
        if chek_step(board, step):
            board[step[0]][step[1]] = user["symbol"]
            return step
    while True:
        step = get_step()
        if chek_step(board, step):
            board[step[0]][step[1]] = user["symbol"]
            return step
        else:
            print("Ячейка не существует или занята")
            continue


def auto_step(user, board: list[list]):
    board_size = len(board)
    all_steps_variants = set((i, j) for i in range(board_size) for j in range(board_size))
    return random.choice(tuple(all_steps_variants.difference(user["all_steps"])))
