# Модуль 3 | Дата, час та рядки
# Тема: Task6 get upcoming birthdays m3
# Розглянуто:
# -----------------------------------------------

'''
Крок шостий. Фінальна функція get_upcoming_birthdays.

У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження.
Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays,
яка допоможе вам визначати, кого з колег потрібно привітати.
Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.

Оскільки дні народження колег можуть припадати на вихідні, ваша функція також повинна
враховувати це та переносити дату привітання на наступний робочий день, якщо це необхідно.

Також потрібно врахувати, що день народження вже може відбутися наступного року.
Наприклад: запускаємо функцію 30 грудня, і є можливість що день народження відбудеться
вже наступного року в перших числах січня.
'''

from datetime import datetime, date, timedelta


# ФУНКЦІЯ 1: перетворює рядок "1955.3.25" → об'єкт datetime.date(1955, 3, 25)
# strptime читає рядок за шаблоном, .date() прибирає час
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


# ФУНКЦІЯ 2: перетворює datetime.date(1955, 3, 25) → рядок "1955.03.25"
# strftime форматує дату у рядок за шаблоном
def date_to_string(date):
    return date.strftime("%Y.%m.%d")


# ФУНКЦІЯ 3: перетворює список користувачів де birthday — рядок
# на список де birthday — об'єкт datetime.date
def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


# ФУНКЦІЯ 4: знаходить дату наступного конкретного дня тижня після start_date
# weekday: 0=пн, 1=вт, 2=ср, 3=чт, 4=пт, 5=сб, 6=нд
def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    # якщо результат 0 або від'ємний — день вже минув на цьому тижні, беремо наступний
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


# ФУНКЦІЯ 5: якщо дата припадає на вихідний (сб/нд) — переносить на понеділок
# якщо будній день — повертає оригінальну дату без змін
def adjust_for_weekend(birthday):
    # .weekday() >= 5 означає субота (5) або неділя (6)
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)  # 0 = понеділок
    return birthday


# ФУНКЦІЯ 6: головна функція — повертає список колег яких треба привітати в наступні days днів
def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []  # результат — сюди збираємо тих кого треба привітати
    today = date.today()     # поточна дата (важливо: date.today(), не datetime!)

    for user in users:
        # КРОК 1: переносимо день народження на поточний рік
        # нас цікавить "25 березня 2026", а не "25 березня 1955"
        birthday_this_year = user["birthday"].replace(year=today.year)

        # КРОК 2: якщо день народження вже минув цього року — дивимось наступний рік
        # наприклад: сьогодні 30 грудня, день народження 2 січня → беремо 2 січня наступного року
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # КРОК 3: перевіряємо чи день народження потрапляє в діапазон наступних days днів
        # diff >= 0 — не минув, diff <= days — в межах діапазону
        if 0 <= (birthday_this_year - today).days <= days:
            # КРОК 4: якщо день народження на вихідному — переносимо на понеділок
            birthday_this_year = adjust_for_weekend(birthday_this_year)

            # КРОК 5: додаємо до результату з датою привітання у форматі рядка
            congratulation_date_str = date_to_string(birthday_this_year)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})

    return upcoming_birthdays