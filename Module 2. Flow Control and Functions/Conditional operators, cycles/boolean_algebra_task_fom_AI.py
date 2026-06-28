# Модуль 2 | Керування потоком та функції
# Тема: Boolean algebra task fom ai
# Розглянуто:
# -----------------------------------------------

#AI task
'''
Завдання 1: "Доступ до VIP-складу"
Тобі потрібно перевірити, чи може співробітник зайти в секцію з цінним товаром.
Умова:
Доступ дозволено, якщо:

У співробітника є ключ (has_key = True).

АБО він є адміністратором (is_admin = True).
'''
# Напиши умову if, яка виведе "Access granted", якщо хоча б одна умова виконується

has_key = input("У вас є ключ? (y/n): ").lower() == "y"
is_admin = input("Ви адміністратор? (y/n): ").lower() == "y"

if has_key or is_admin:
    print("Access granted")
else:
    print("Access denied")

'''Завдання 2: "Акція на доставку"
Твоя CRM має розрахувати, чи буде доставка безкоштовною.
Умова:
Доставка безкоштовна, якщо:

Сума замовлення (total_price) більша за 1000 грн.

ТА товар не є великогабаритним (is_heavy = False).'''
# Напиши умову, яка виведе "Free delivery", або "Pay for delivery"
# Підказка: використай оператор 'not' для перевірки is_heavy

total_price = int(input("Сума замовлення: "))
is_heavy = input("Товар великогабаритний? (y/n): ").lower() == "y"

if total_price > 1000 and not is_heavy:
    print("Free delivery")
else:
    print("Pay for delivery")

'''
Завдання 3: "Складна оренда авто" (Рівень PRO)
Давай ускладнимо твій попередній приклад. Компанія ввела нові правила.
Умова:
Оренда дозволена, якщо:

Ім'я вказане (name) І вік 18+ І є права.

АЛЕ, якщо користувачу менше 21 року, у нього обов'язково має бути стаж водіння (experience) не менше 2 років.
'''
# Спробуй поєднати це в одну складну умову if.
# Підказка: використовуй дужки ( ), щоб групувати частини умови, як у математиці.

name = input("Enter your name: ").strip()
age = int(input("Enter your age: "))
has_driver_licence = input("Do you have a driver's license?(y/n): ").lower() == "y"
experience = int(input("Enter your experience: "))

if (age >= 18 and has_driver_licence and name and experience >= 2) or (age >= 21 and has_driver_licence and name): 
    print(f"User {name} can rent a car")
else:
    print(f"User {name} can't rent a car")

'''Більш коротка реалізація'''

name = input("Enter your name: ").strip()
age = int(input("Enter your age: "))
experience = int(input("Enter your experience: "))
has_driver_licence = input("Do you have a driver's license?(y/n): ").lower() == "y"
if name and has_driver_licence and age >= 18:
    if age >= 21 or experience >= 2:
        print(f"User {name} can rent a car")
    else:
        print("Not enough experience")
else:
    print("Basic requirements not met")
