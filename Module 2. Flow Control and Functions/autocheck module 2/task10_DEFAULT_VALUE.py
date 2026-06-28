# Модуль 2 | Керування потоком та функції
# Тема: Task10 default value
# Розглянуто:
# -----------------------------------------------

# Функція залишається такою ж — вона ідеальна

'''
Напишіть функцію get_fullname на Python, яка приймає ім'я, прізвище та, опціонально, друге ім'я (або по батькові) та повертає рядок з повним іменем користувача.

Задачі:

1. Створіть функцію get_fullname, яка приймає три аргументи: first_name, last_name та middle_name. Зробіть middle_name необов'язковим аргументом зі значенням за замовчуванням "".
2. Якщо middle_name передано, функція повинна повертати повне ім'я у форматі 'first_name middle_name last_name'.
3. Якщо middle_name не передано, функція повинна повертати повне ім'я у форматі 'first_name last_name'.
4. Для формування повного імені використовуйте f-рядок.
Очікуваний результат:

Функція повертає рядок з повним іменем користувача, залежно від того, чи передано друге ім'я.

Підказки:

Використовуйте умовну конструкцію if для перевірки, чи middle_name не порожній.
Для створення рядка з повним іменем використовуйте f-рядок для вставки значень змінних.
'''



#for HW
def get_fullname(first_name, last_name, middle_name=""):
    first_name = first_name.strip()
    last_name = last_name.strip()
    middle_name = middle_name.strip()
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    return f"{first_name} {last_name}"





#My resolution
def get_fullname(first_name, last_name, middle_name=""):
    first_name = first_name.strip()
    last_name = last_name.strip()
    middle_name = middle_name.strip()
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    return f"{first_name} {last_name}"

while True:
    f_name = input("Enter your first name: ").strip()
    l_name = input("Enter your last name: ").strip()
    m_name = input("Enter your middle name (optional): ").strip() 

    if not f_name or not l_name:
        print("First name and last name cannot be empty. Please try again.")
    else:
        # Дані вже в змінних f_name, l_name, m_name
        # Просто передаємо їх у функцію і виходимо
        full_name = get_fullname(f_name, l_name, m_name)
        print(f"\nSuccess! Full name: {full_name}")
        break