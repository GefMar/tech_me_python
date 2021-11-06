def func_log(file_name, data):
    with open(file_name, "a", encoding="UTF-8") as file:
        file.write(data)


def some(func):
    counter = 0

    def wrapper1(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(func.__name__, counter)
        result = func(*args, **kwargs)
        print("Function close")
        return result

    return wrapper1


def log_some(file_name):
    def decorator(func):
        counter = 0

        def wrapper2(*args, **kwargs):
            nonlocal counter
            counter += 1
            func_log(file_name, f"{func.__name__}, {counter}\n")
            result = func(*args, **kwargs)
            return result

        return wrapper2

    return decorator


@log_some("log.txt")
@some
def my_func(a, b):
    return a + b


def some2(func, **kw):
    def wrapper(*args, **kwargs):
        return func(*args, **kw, **kwargs)

    return wrapper


# 
# A = 2
# B = [2, 3, 4, 5, 6, 7, 8, 9]
# func = some2(my_func, b=A)
# results = []
# for itm in B:
#     results.append(func(itm))
# print(results)


# my_func = some(my_func)

print(my_func(a=2, b=5))
print(my_func(2, 7))
print(my_func(8, 5))
print(my_func.__name__)
