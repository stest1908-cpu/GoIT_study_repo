#Рахування факторіалу через процесів
from multiprocessing import Process


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Factorial({n}) = {result}")

if __name__ == "__main__":
    from multiprocessing import Process

processes = []

for i in [5, 6, 7]:
    p = Process(target=factorial, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

