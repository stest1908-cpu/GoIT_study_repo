#Декоратор - це функція, яка приймає іншу функцію як аргумент і повертає нову функцію, яка зазвичай розширює або змінює поведінку оригінальної функції без зміни її коду.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        starte = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: Execution time: {end - starte} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

print(slow_function())


