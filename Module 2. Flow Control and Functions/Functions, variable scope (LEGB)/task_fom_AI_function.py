'''
Завдання 1
Додайте до списку ще 2 фрукти та запустіть функцію.

Завдання 2
Змініть функцію так, щоб вона виводила фрукти без індексу, просто так:
apple
banana
cherry

Завдання 3
Змініть назву функції та назву списку — і запустіть її.

'''
def list_sweet_fruits():
    sweet_fruits = ["apple", "banana", "cherry", "orange", "grape"]
    for index, value in enumerate(sweet_fruits):
        print(value)

list_sweet_fruits()