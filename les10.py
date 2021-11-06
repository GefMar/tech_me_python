import os
from os import path
import sys


# print(os.name)
# print(os.environ)
# print(os.getlogin())
# print(os.listdir())
# print(os.getcwd())
# print(os.chdir("./../"))
# print(os.getcwd())
# os.mkdir()
# a = os.system("python3 hello_world.py")
# print("A", a)

# base = path.dirname(path.abspath(__file__))
# new_file_name = "NEW_FILE"
# new_file_path = path.join(base, new_file_name)
# print(new_file_path)

# print(path.getsize("game_init"))
# current_path =
#
# for item in os.listdir():
#     print(item, path.islink(item))
#
# print(sys.platform)
# print(sys.maxsize)
# print(sys.getrecursionlimit())
# print(sys.argv)

def help():
    print("ВВОДИТЕ ИМЯ ФУНКЦИИ И ДВА ЧИСЛА")


def summary(a, b):
    return a + b


def multi(a, b):
    return a * b


def exponentiation(a, b):
    return a ** b


command = {
    multi.__name__: multi,
    summary.__name__: summary,
    exponentiation.__name__: exponentiation,
    "help": help
}


def main():
    if "help" in sys.argv:
        command['help']()
    elif len(sys.argv) < 4:
        print("ошибка ввода данных")
    else:
        func = command[sys.argv[1]]
        a, b = int(sys.argv[2]), int(sys.argv[3])
        print(func(a, b))


if __name__ == '__main__':
    main()
