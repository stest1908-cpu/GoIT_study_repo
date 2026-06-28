# QA сесія 18.04.26 | Основи веб
# Тема: 1.5.3
# Розглянуто:
# -----------------------------------------------

from multiprocessing import Pool


def task(n):
    s = 0
    for i in range(10 ** 7):
        s += i
    return s


if __name__ == "__main__":
    with Pool(4) as p:
        print(p.map(task, [1, 2, 3, 4]))