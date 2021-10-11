import time

cycles = 10 ** 6


def while_test():
    strt = time.time()
    idx = 0
    itms = []
    while idx < cycles:
        itms.append(idx)
        idx += 1
    print(time.time() - strt)


def for_test():
    strt = time.time()
    itms2 = []
    for itm in range(cycles):
        itms2.append(itm)
    print(time.time() - strt)


# for_test()
# while_test()
