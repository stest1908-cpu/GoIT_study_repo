#!!!"Підготовка даних" 


#На другому кроці ми виконаємо операції над списками користувачів. Мета кроку це навчитися працювати зі списками та словниками в Python в межах нашого завдання.

#Напишіть функцію prepare_user_list, яка приймає список імен користувачів та їх дат народження у рядковому форматі, і повертає список словників у форматі {"name": <name>, "birthday": <birthday>}, де <birthday> - це об'єкт datetime.date.

#Виконання наступного коду для вашої функції:
'''
users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

prepared_users = prepare_user_list(users)
print(prepared_users)
Повинно призводити до виведення:

[
    {"name": "Bill Gates", "birthday": datetime.date(1955, 3, 25)},
    {"name": "Steve Jobs", "birthday": datetime.date(1955, 3, 21)},
    {"name": "Jinny Lee", "birthday": datetime.date(1956, 3, 22)},
    {"name": "John Doe", "birthday": datetime.date(1985, 1, 23)},
    {"name": "Jane Smith", "birthday": datetime.date(1990, 1, 27)},
]

Як бачимо, після виконання функції, в словнику значення ключа "birthday" має бути об'єктом datetime.date. Для перетворення рядка в об'єкт datetime.date використовуйте написану на першому кроці функцію string_to_date, яка приймає рядкове представлення дати в форматі "YYYY.MM.DD" і перетворює його на об'єкт datetime.date.
'''

# Імпортуємо інструменти для роботи з датами
from datetime import date, datetime

# ФУНКЦІЯ 1: перетворює рядок "1955.3.25" → об'єкт datetime.date(1955, 3, 25)
# strptime — читає рядок за шаблоном "%Y.%m.%d"
# .date() — прибирає час (00:00:00) і залишає лише дату
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

# Список словників з іменами та датами народження у рядковому форматі
# birthday поки що рядок "1955.3.25", а не об'єкт date
user_data = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

# ФУНКЦІЯ 2: отримує список користувачів з рядковими датами
# і повертає новий список де birthday вже об'єкт datetime.date
def prepare_user_list(user_data):
    result = []  # порожній список для результату

    for user in user_data:  # перебираємо кожного користувача
        
        # витягуємо ім'я зі словника
        # user = {"name": "Bill Gates", "birthday": "1955.3.25"}
        # user["name"] = "Bill Gates"
        name = user["name"]
        
        # витягуємо дату і перетворюємо рядок → datetime.date
        # user["birthday"] = "1955.3.25"
        # string_to_date("1955.3.25") = datetime.date(1955, 3, 25)
        birthday = string_to_date(user["birthday"])
        
        # створюємо новий словник з перетвореною датою
        new_user = {"name": name, "birthday": birthday}
        
        # додаємо новий словник до результату
        result.append(new_user)

    return result  # повертаємо готовий список

# Викликаємо функцію і передаємо user_data як аргумент
# результат одразу виводимо на екран
print(prepare_user_list(user_data))

#Головна ідея:
#Ви взяли список де birthday — рядок, і перетворили його на список де birthday — об'єкт datetime.date. Це потрібно щоб пізніше можна було порівнювати дати між собою. 😊