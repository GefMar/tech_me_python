
def my_cycle(iter_object):
    idx = 0
    while True:
        try:
            yield iter_object[idx]
            idx += 1
        except IndexError:
            idx = 0
