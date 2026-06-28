# QA сесія 17.04.26
# Тема: 1.3
# Розглянуто:
# -----------------------------------------------

#Функкція-генератор яка повертає n випадкових чисел від 1 до 100. Використайте її для генерації 5 випадкових чисел та виведіть їх на екран. Потім спробуйте викликати генератор ще раз, щоб побачити, що він вже вичерпаний.

import random


def random_numbers(n):
    for _ in range(n):
        yield random.randint(1, 100)


gen = random_numbers(5)

print(next(gen))
print(next(gen))
print(next(gen))

for num in gen:
    print(num)

print(next(gen))
print(next(gen))
print(next(gen))