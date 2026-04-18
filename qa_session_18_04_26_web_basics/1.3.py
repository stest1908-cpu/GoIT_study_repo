#Рахування факторіалу через потоки

import threading


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Factorial({n}) = {result}")


threads = []

for i in range(1, 10):
    t = threading.Thread(target=factorial, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()