import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()


def task1():
    with lock1:
        print("Task1: взяв lock1")
        time.sleep(1)
        with lock2:
            print("Task1: взяв lock2")


def task2():
    with lock1:  # змінили порядок
        print("Task2: взяв lock1")
        time.sleep(1)
        with lock2:
            print("Task2: взяв lock2")


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()