#Робота з датою

'''
Python містить інструменти, призначені для роботи з датою і часом, 
які дозволяють представляти їх у форматі, зрозумілому для користувачів. 
Ви звикли до стандартного відображення дати в календарях пошти, на веб-сайтах тощо.

Однак у програмуванні дати виглядають інакше,
і для здійснення перетворень між різними форматами в Python використовується спеціальний вбудований модуль datetime.
Цей модуль надає класи для маніпуляцій з датами і часом.

Основні можливості datetime:

- визначення поточної дати і часу;
- обчислення інтервалу між двома подіями;
- визначення дня тижня, високосного року для будь-якої дати у минулому не раніше року datetime.MINYEAR або в майбутньому не пізніше року datetime.MAXYEAR;
- порівняння дати і часу декількох подій за допомогою операторів порівняння;
- робота з часовими зонами, порівняння подій з урахуванням часових зон та переходу на літній/зимовий час;
- перетворення дати/часу в рядок і навпаки.
'''


#Перед роботою з датами і часом потрібно імпортувати модуль в нашому скрипті:
import datetime #імпортуємо модуль datetime

print(datetime.MINYEAR) #Виводить мінімальний рік, який може бути представлений у модулі datetime (1)
print(datetime.MAXYEAR) #Виводить максимальний рік, який може бути представлений у модулі datetime (9999)

#Для отримання поточної дати і часу використовується метод datetime.now():
import datetime
now = datetime.datetime.now()
print(now)

#Виведення у форматі рік-місяць-день години:хвилини:секунди.мікросекунди: 2023-12-14 12:39:29.992996

#Роботу з модулями ми ще розглянемо, але об'єкт datetime в свій скрипт ми також можемо отримати, просто витягнув його з модуля:

from datetime import datetime #імпортуємо клас datetime з модуля datetime
now = datetime.now() #отримуємо поточну дату і час
print(now)

#Так — і модуль і об'єкт мають однакове ім'я, ви все вірно зрозуміли. 😉
#У результаті виклику методу now() ми отримуємо об'єкт datetime, у якого є ряд корисних атрибутів:
from datetime import datetime

current_datetime = datetime.now()

print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
print(current_datetime.tzinfo)

#Ось основні з них:
'''
1. year: Повертає рік дати. Наприклад, якщо now містить дату "2023-12-14 12:39:29", now.year буде 2023.
2. month: Повертає місяць як число від 1 до 12. У нашому прикладі now.month буде 12.
3. day: Повертає день місяця. Для "2023-12-14 12:39:29" now.day буде 14.
4. hour: Повертає годину дня від 0 до 23. У нашому випадку now.hour буде 12.
5. minute: Повертає хвилини часу від 0 до 59. Для даної дати now.minute буде 39.
6. second: Повертає секунди часу від 0 до 59. В нашому прикладі now.second буде 29.
7. microsecond: Повертає мікросекунди часу. Це значення може бути від 0 до 999999. У "2023-12-14 12:39:29.992996", now.microsecond буде 992996.
8. tzinfo: Повертає інформацію про часову зону об'єкта datetime. Для now, якщо часова зона не була вказана, tzinfo буде None.
'''
#В об'єкта datetime є методи, щоб отримати дату (без часу) та час (без дати):

from datetime import datetime

current_datetime = datetime.now() 
print(current_datetime.date()) #Виводить дату у форматі рік-місяць-день: 2023-12-14
print(current_datetime.time()) #Виводить час у форматі години:хвилини:секунди.мікросекунди: 12:39:29.992996

'''
Є зворотний метод datetime.combine який використовується для створення нового об'єкта datetime шляхом комбінування об'єктів date та time.
Це дозволяє створювати точний момент часу, вказуючи дату та час окремо, а потім об'єднуючи їх.
'''
#Основний синтаксис:
#datetime.datetime.combine(date_object, time_object)

#date_object: Об'єкт date, який містить інформацію про рік, місяць та день.
#time_object: Об'єкт time, який містить інформацію про години, хвилини, секунди та мікросекунди.

#Розглянемо приклад:
import datetime

# Створення об'єктів date і time
date_part = datetime.date(2023, 12, 14)
time_part = datetime.time(12, 30, 15)

# Комбінування дати і часу в один об'єкт datetime
combined_datetime = datetime.datetime.combine(date_part, time_part)

print(combined_datetime)  # Виведе "2023-12-14 12:30:15"
#У цьому прикладі ми створюємо об'єкт date для представлення конкретної дати (14 грудня 2023 року) і об'єкт time для представлення конкретного часу (12:30:15).
#  Потім ми використовуємо datetime.combine для створення нового об'єкта datetime, який представляє цей конкретний момент часу.

#My example:
try:
    import datetime
    date_part = datetime.date(int(input('Enter year: ')), int(input('Enter month: ')), int(input('Enter day: ')))
    time_part = datetime.time(int(input('Enter hours: ')), int(input('Enter minutes: ')), int(input('Enter seconds: ')))
    combined_datetime = datetime.datetime.combine(date_part, time_part)
    print(combined_datetime)
except ValueError:
    print("Invalid input. Please enter valid numbers.") 

'''
Цей метод є корисним, коли у вас є окремі компоненти дати та часу,
які потрібно об'єднати для отримання точного моменту в часі.
'''

'''
Щоб створити об'єкт datetime з конкретною вибраною датою у Python, можна використовувати конструктор класу datetime.datetime, передаючи йому рік, місяць, і день як аргументи. 
Також можна вказати годину, хвилину, секунду та мікросекунду, але це не обов'язково — якщо їх пропустити, вони будуть встановлені на 0.
'''

#Для створення об'єкта datetime з певною датою:

import datetime

# Створення об'єкта datetime з конкретною датою
specific_date = datetime.datetime(year=2020, month=1, day=7)

print(specific_date)  # Виведе "2020-01-07 00:00:00"
#У цьому прикладі створюється об'єкт datetime для 7 січня 2020 року.
# Оскільки час не вказано, він автоматично встановлюється на початок дня (00:00:00).

#My example:
try:
    import datetime
    specific_date = datetime.datetime(int(input('Enter year: ')), int(input('Enter month: ')), int(input('Enter day: ')))
    print(specific_date)
except ValueError:
    print("Invalid input. Please enter valid numbers.") 

#Створення об'єкта datetime з датою та часом:

import datetime

# Створення об'єкта datetime з конкретною датою і часом
specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)

print(specific_datetime)  # Виведе "2020-01-07 14:30:15"
'''
Тут створюється об'єкт datetime для 7 січня 2020 року о 14:30:15.
Використання ключових параметрів допомагає уникнути плутанини 
та забезпечує чіткість при вказівці конкретних компонентів часу. 
Наприклад попередній приклад можна було записати так:
'''
import datetime

# Створення об'єкта datetime з конкретною датою і часом
specific_datetime = datetime.datetime(2020, 1, 7, 14, 30, 15)

print(specific_datetime)  # Виведе "2020-01-07 14:30:15"

#Але використання ключових параметрів робить код більш зрозумілим, особливо коли його читають інші розробники. 
#Також це дозволяє легко вказувати тільки ті компоненти дати/часу, які вам потрібні, та уникнути помилок зі змішуванням порядку параметрів.

#Метод weekday() використовується для отримання номера дня тижня для вказаної дати. 
# Він повертає номер дня тижня, де понеділок має номер 0, а неділя - 6.

from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Отримання номера дня тижня
day_of_week = now.weekday()

# Поверне число від 0 (понеділок) до 6 (неділя)
print(f"Сьогодні: {day_of_week}")  

'''
Для порівняння двох об'єктів datetime у Python, ви можете використовувати стандартні оператори порівняння,
такі як == (рівність), != (нерівність), < (менше), > (більше), <= (менше або дорівнює) та >= (більше або дорівнює).
 Ці оператори дозволяють порівнювати дати та часи, щоб визначити, чи один об'єкт datetime передує, наступає або є точно таким самим як інший.'''
from datetime import datetime

# Створення двох об'єктів datetime
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)

# Порівняння дат
print(datetime1 == datetime2)  # False, тому що дати не однакові
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2
#виведення:
#False
#True   
#True
#False

