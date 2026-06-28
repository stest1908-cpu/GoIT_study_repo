# Модуль 2 | Керування потоком та функції
# Тема: Task12 variabl  number of parameters
# Розглянуто:
# -----------------------------------------------

#Змінна кількість параметрів

'''
Наступне завдання буде суто теоретичним, і ми потренуємося створювати функції в Python, які можуть приймати довільну кількість позиційних або ключових аргументів.

Задачі:

1. Створіть функцію first, яка приймає один обов'язковий аргумент size та довільну кількість позиційних аргументів. Функція має повертати суму: size + кількість позиційних аргументів.
2. Створіть функцію second, яка також приймає один обов'язковий аргумент size та довільну кількість ключових аргументів. Функція має повертати суму: size + кількість ключових аргументів.
3. В обох функціях використовуйте спеціальні синтаксиси * для позиційних аргументів та ** для ключових аргументів.
4. Очікуваний результат:

Функції повинні коректно розраховувати суму size та кількості переданих аргументів.

Підказки:

*args у функції first означає, що функція може приймати будь-яку кількість позиційних аргументів.
**kwargs у функції second означає, що функція може приймати будь-яку кількість ключових аргументів.
Використовуйте функцію len для визначення кількості позиційних або ключових аргументів.

Приклад коду виконання функцій:
print(first(5, "first", "second", "third"))  # Виведе: 8
print(second(3, comment_one="first", comment_two="second", comment_third="third"))  # Виведе: 6
print(first(1, "Alex", "Boris"))  # Виведе: 3
print(second(10, comment_one="Alex", comment_two="Boris"))  # Виведе: 12
'''

# *args — приймає будь-яку кількість позиційних аргументів
# вони зберігаються як кортеж (tuple)
def first(size, *args):
    # len(args) — рахуємо кількість переданих аргументів
    result = size + len(args)
    return result

# size=5, args=("first", "second", "third") → 5 + 3 = 8
print(first(5, "first", "second", "third"))
# size=1, args=("Alex", "Boris") → 1 + 2 = 3
print(first(1, "Alex", "Boris"))


# **kwargs — приймає будь-яку кількість ключових аргументів
# вони зберігаються як словник (dict) {ключ: значення}
def second(size, **kwargs):
    # len(kwargs) — рахуємо кількість переданих ключових аргументів
    result = size + len(kwargs)
    return result

# size=3, kwargs={"comment_one": "first", ...} → 3 + 3 = 6
print(second(3, comment_one="first", comment_two="second", comment_third="third"))
# size=10, kwargs={"comment_one": "Alex", "comment_two": "Boris"} → 10 + 2 = 12
print(second(10, comment_one="Alex", comment_two="Boris"))

# Тести
assert first(5, "first", "second", "third") == 8
assert first(1, "Alex", "Boris") == 3
assert second(3, comment_one="first", comment_two="second", comment_third="third") == 6
assert second(10, comment_one="Alex", comment_two="Boris") == 12
print("Всі тести пройшли!")

