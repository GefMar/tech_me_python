import random


def p_deco(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<p>{result}</p>"

    return wrapper


def div_deco(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<div>{result}</div>"

    return wrapper


def tag_deco(tag_name, class_string=""):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            tag_class = f' class="{class_string}"' if class_string else ''
            return f'<{tag_name}{tag_class}>{result}</{tag_name}>'

        return wrapper

    return decorator


@tag_deco("html")
@tag_deco("body")
@tag_deco("div", "div_name")
@tag_deco("span", "some_span")
@tag_deco("p")
def user_name_counter(name, count):
    result = f"User: {name}, Count: {count}"
    return result


with open("hello.html", "w", encoding="UTF-8") as file:
    file.write(user_name_counter("SERGEY", 23))


# print(user_name_counter("SERGEY", 22))
# TODO: 3 вложенности это плохо
def retry(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal count
            while count:
                try:
                    result = func(*args, **kwargs)
                    return result
                except ValueError:
                    count -= 1
            raise ValueError

        return wrapper

    return decorator


@retry(10)
def connect(url):
    a = random.randint(1, 100)
    if a % 3:
        return "ОТВЕТ"
    raise ValueError


print("HELLOOOOOOO")
