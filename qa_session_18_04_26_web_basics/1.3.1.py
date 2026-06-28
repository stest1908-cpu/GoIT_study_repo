# QA сесія 18.04.26 | Основи веб
# Тема: 1.3.1
# Розглянуто:
# -----------------------------------------------

import threading


def factorial_part(start, end, result, index):
    res = 1
    for i in range(start, end + 1):
        res *= i
    result[index] = res


def threaded_factorial(n):
    result = [1, 1]

    mid = n // 2

    t1 = threading.Thread(target=factorial_part, args=(1, mid, result, 0))
    t2 = threading.Thread(target=factorial_part, args=(mid + 1, n, result, 1))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    return result[0] * result[1]


print(threaded_factorial(10))
