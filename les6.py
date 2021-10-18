# a = 5
# b = 0
# 
# try:
#     result = a / b
# except ZeroDivisionError:
#     print("ZDE")
# except (KeyError, IndexError):
#     print('KeyE')
# finally:
#     print("FIN")


def some(a, b, c):
    h = []
    result = None
    try:
        if c:
            result = a / b
        else:
            result = h[a]
        return result
    except ZeroDivisionError:
        print("ZDE")
    except (KeyError, IndexError):
        print('KeyE')
    finally:
        return 234
    return result


a = some(1, 2, 1)
print(a)
