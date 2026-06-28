# Модуль 3 | Дата, час та рядки
# Тема: Task1 date conversion m3
# Розглянуто:
# -----------------------------------------------

#!!!Конвертація дат

#На першому кроці ми виконаємо роботу з датами. Мета кроку це ознайомлення з базовими операціями над датами які нам знадобляться для цієї задачі.

#Напишіть функцію string_to_date, яка приймає рядкове представлення дати в форматі "YYYY.MM.DD" і перетворює його на об'єкт datetime.date.

#Напишіть зворотну функцію date_to_string, яка приймає об'єкт datetime.date і повертає рядкове представлення дати в форматі "YYYY.MM.DD".

#Ці функції повинні працювати наступним чином:
'''date_string = "2024.01.01"
converted_date = string_to_date(date_string)
print(converted_date)
date_string = date_to_string(converted_date)
print(date_string)
'''

#Виконання такого коду призведе до наступного виведення:
#2024-01-01
#2024.01.01

#Solution:

#мій код з помилкою та поясненням де проблеми
'''
from datetime import datetime

date_string = "2024.01.01"

# ❌ ПОМИЛКА 1: цей код зайвий — він дублює те що робить функція string_to_date
# Ви написали логіку двічі: спочатку напряму, потім у функції
converted_date = datetime.strptime(date_string, "%Y.%m.%d").date()
print(converted_date)

# ❌ ПОМИЛКА 2: цей код зайвий — він дублює те що робить функція date_to_string
date_string = converted_date.strftime("%Y.%m.%d")
print(date_string)

# ✅ функція правильна
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

# ❌ ПОМИЛКА 3: print(converted_date) не демонструє роботу функції
# Ви виводите стару змінну, а не результат виклику функції
# Треба: print(string_to_date(date_string))
print(converted_date)

# ✅ функція правильна
def date_to_string(date):
    return date.strftime("%Y.%m.%d")

# ❌ ПОМИЛКА 4: та сама проблема — виводите стару змінну
# Треба: print(date_to_string(converted_date))
print(converted_date)
'''

#Чому ви зробили ці помилки?
#1. Тестували код до функцій — це нормально для початківця! Спочатку написали логіку напряму, потім перенесли у функцію, але забули прибрати старий код.
#2. Не викликали функції після оголошення — функція без виклику нічого не робить. Треба явно написати string_to_date(...) щоб вона запрацювала.

#Після виправлення помилок код буде виглядати так:
from datetime import datetime

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date):
    return date.strftime("%Y.%m.%d")

# Виклик функцій
date_string = "2024.01.01"
converted_date = string_to_date(date_string)
print(converted_date)                    # 2024-01-01

date_string = date_to_string(converted_date)
print(date_string)                       # 2024.01.01