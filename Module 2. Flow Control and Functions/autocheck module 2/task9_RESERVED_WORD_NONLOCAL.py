# Модуль 2 | Керування потоком та функції
# Тема: Task9 reserved word nonlocal
# Розглянуто:
# -----------------------------------------------

#Зарезервоване слово "nonlocal"

'''
Необхідно створити функцію discount_price на Python, яка розраховує кінцеву ціну товару після застосування знижки.

Задачі:

Створіть функцію discount_price, яка приймає два аргументи: price - початкова ціна товару та discount - знижка як дійсне число від 0 до 1.
Усередині функції discount_price створіть вкладену функцію apply_discount, яка використовує nonlocal для доступу та модифікації змінної price.
Функція apply_discount має обчислити знижену ціну, помноживши price на (1 - discount).
Викличте apply_discount всередині discount_price, а потім поверніть оновлену ціну.
Очікуваний результат:

Функція повинна повертати ціну товару після застосування знижки.

Підказки:

Використання nonlocal дозволяє функції apply_discount модифікувати змінну price, оголошену у зовнішній функції discount_price.
Для розрахунку зниженої ціни використовуйте формулу price * (1 - discount).
'''

try:
    # Зовнішня функція приймає ціну та знижку
    def discount_price(price, discount):
        
        # Перевірка що знижка між 0 і 1
        if not (0 <= discount <= 1):
            raise ValueError("Discount must be between 0 and 1.")
        
        # Вкладена функція має доступ до змінних зовнішньої функції
        def apply_discount():
            nonlocal price  # дозволяє змінювати змінну price із зовнішньої функції
            price = price * (1 - discount)  # розраховуємо ціну після знижки
            return price  # повертаємо нову ціну
        
        return apply_discount()  # викликаємо вкладену функцію і повертаємо результат
    
    # Отримуємо дані від користувача і викликаємо функцію
    print(discount_price(int(input("Enter the price: ")), float(input("Enter the discount: "))))

except ValueError as e:
    print(f"Invalid input: {e}")  # виводимо конкретну помилку
#Головна ідея — nonlocal дозволяє вкладеній функції змінювати змінну зовнішньої функції. Без нього price всередині apply_discount була б новою локальною змінною. 