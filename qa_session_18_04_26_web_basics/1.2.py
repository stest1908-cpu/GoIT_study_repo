# QA сесія 18.04.26 | Основи веб
# Тема: 1.2
# Розглянуто:
# -----------------------------------------------

# Як працює Lock and RLock

import threading

# lock = threading.Lock()
lock = threading.RLock()  # reentrant


def inner():
    with lock:
        print("inner")


def outer():
    with lock:
        print("outer")
        inner()  # тут буде deadlock


outer()