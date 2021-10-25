import random


COMP_NAMES = [
    "R2D2",
    "C3PO",
    "WALLE",
    "DALEK",
]

user_template = (
    ("name", lambda *args, **kwargs: input("ВВЕДИТЕ ВАШЕ ИМЯ")),
    ("symbol", lambda symbol, *args, **kwargs: symbol),
    ("steps", lambda *args, **kwargs: list()),
)


def create_user(symbol) -> dict:
    user = {}
    for itm in user_template:
        user[itm[0]] = itm[1](symbol=symbol)
    return user


def create_comp(symbol) -> dict:
    return {
        "name": random.choice(COMP_NAMES),
        "symbol": symbol,
        "steps": [],
    }


MODES = {
    "COMP": {"creator": create_comp},
    "USER": {"creator": create_user},
}


def get_user(mode, symbol) -> dict:
    return MODES[mode]["creator"](symbol=symbol)


user = get_user("COMP", "X")
print(user)
