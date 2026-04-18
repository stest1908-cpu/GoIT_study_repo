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