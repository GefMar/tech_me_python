from some2 import SOME


def hello():
    print("hello")


hello()
print("THIS IS SOME1 NAME:", __name__)


def lloger(func):
    def wrapper(*args, **kw):
        try:
            return func(*args, **kw)
        except Exception as exc:
            "ТУТ ПИШЕМ ОШИБКУ В ФАЙЛ"
            raise exc

    return wrapper
