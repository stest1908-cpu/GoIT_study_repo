# Модуль 3 | Дата, час та рядки
# Тема: Working with timedelta intervals
# Розглянуто:
# -----------------------------------------------

#Робота з часовими проміжками timedelta

'''
У модулі datetime є клас timedelta, який використовується для представлення різниці між двома моментами в часі.
Об'єкти timedelta можуть представляти дні, години, хвилини, секунди та мікросекунди.
Вони корисні для розрахунків, що включають додавання або віднімання часу від конкретних дат або порівняння часових інтервалів.

Об'єкт timedelta можна створити, задаючи тижні, дні, години, хвилини, секунди, мілісекунди і мікросекунди, 
передавши один або кілька з таких параметрів: days, seconds, microseconds, milliseconds, minutes, hours, weeks. 
Якщо якийсь параметр не заданий, то він дорівнює 0 за замовчуванням.
'''

from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)
#виведе: 64 days, 8:05:56.000010

#Якщо відняти від одного datetime об'єкту інший, то отримаємо timedelta об'єкт.
# Він відповідає за відрізок часу між двома датами.

from datetime import datetime

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)  # 365 days, 0:00:00
print(difference.total_seconds())  # 31536000.0

#Тут ми ще за допомоги методу total_seconds виконали конвертацію timedelta в секунди.
#Виведе: 365 days, 0:00:00
31536000.0

'''
Максимальний діапазон для timedelta обмежений приблизно 9999 роками, що більше ніж достатньо для більшості застосувань. 
Об'єкти timedelta можна створювати, щоб отримати час / дату, віддалену від початкової.
'''

from datetime import datetime, timedelta

now = datetime.now()
future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
print(future_date)
#Виведе: 2026-05-30 17:45:12.345678 (приклад виводу, залежить від поточної дати і часу)

#Або від якоїсь конкретної дати.

from datetime import datetime, timedelta

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)

print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00

#Виведе:
# 2020-02-04 14:00:00
# 2019-12-10 14:00:00

'''
Але якщо потрібно робити обчислення або порівняння, засновані на послідовності дат, наприклад, 
для визначення кількості днів між двома датами, ми можемо використати метод toordinal(), 
який повертає порядковий номер дня, враховуючи кількість днів з 1 січня року 1 нашої ери (тобто з початку християнського календаря). 
Цей метод перетворює об'єкт datetime в ціле число, що представляє порядковий номер даного дня.
'''

from datetime import datetime

# Створення об'єкта datetime
date = datetime(year=2023, month=12, day=18)

# Отримання порядкового номера
ordinal_number = date.toordinal()
print(f"Порядковий номер дати {date} становить {ordinal_number}")

#Виведе: Порядковий номер дати 2023-12-18 00:00:00 становить 738872

#Наприклад ми хочемо визначити скільки пройшло повних днів, коли Наполеон спалив Москву,
#  а це відбулося 14 вересня 1812 року

from datetime import datetime

# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# Поточна дата
current_date = datetime.now()

# Розрахунок кількості днів
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(days_since)

#Виведе: 78045