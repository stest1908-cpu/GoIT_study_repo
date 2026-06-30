# Модуль 4 | Робота з файлами та модульна система
# Тема: Маніпуляція з компонентами шляху (Path components manipulation)
# Розглянуто: with_name() — змінює ім'я файлу, with_suffix() — змінює розширення; обидва повертають новий Path, не змінюють оригінал
# -----------------------------------------------

'''
Клас Path надає зручні методи для маніпулювання компонентами шляху, такі як with_name і with_suffix. Ці методи дозволяють легко змінювати ім'я файлу або його розширення в об'єкті Path.

Метод with_name замінює ім'я файлу в шляху на нове. Він корисний, коли вам потрібно змінити тільки ім'я файлу, зберігаючи решту шляху незмінною.
'''

from pathlib import Path # імпортуємо модуль pathlib

# Початковий шлях до файлу
original_path = Path("documents/example.txt") # documents/example.txt

# Зміна ім'я файлу
new_path = original_path.with_name("report.txt") # documents/new_name.txt

print(new_path)

'''
У цьому прикладі, with_name("report.txt") замінює ім'я файлу example.txt на report.txt, при цьому зберігаючи решту шляху documents без змін.

Виведення:

documents/new_name.txt
'''

'''
Метод with_suffix замінює або додає розширення файлу в шляху. Це корисно, коли потрібно змінити тип файлу або додати розширення до файлу, який його не має.
'''

from pathlib import Path

# Початковий шлях до файлу
original_path = Path("documents/example.txt")

# Зміна імені файлу
new_path = original_path.with_suffix(".md")
print(new_path)

'''
У цьому прикладі, метод with_suffix(".md") додає розширення .md до шляху.

Виведення:

documents/example.md
'''

'''
Але треба розуміти, що методи with_name і with_suffix в класі Path модуля pathlib в Python не змінюють фізичне ім'я файлу на диску. Замість цього, вони використовуються для створення нового об'єкта Path, який відображає змінений шлях.
'''

from pathlib import Path

original_path = Path("documents/example.txt")

# Створює новий об'єкт Path з іншим ім'ям файлу
new_path = original_path.with_name("report.txt")

print(original_path)
print(new_path)

'''
У цьому прикладі, original_path залишається незмінним, а new_path є новим об'єктом Path, який відображає шлях з новим іменем файлу.

Виведення:

documents/example.txt
documents/report.txt
'''

'''
Щоб фізично змінити ім'я файлу на диску, потрібно використовувати методи для роботи з файловою системою, наприклад, rename. Цей виклик змінить ім'я файлу example.txt на report.txt у директорії documents на диску.
'''

from pathlib import Path

original_path = Path("documents/example.txt")

# Створює новий об'єкт Path з іншим ім'ям файлу
new_path = original_path.with_name("report.txt")
# ❌ Приклад автора курсу — падає, бо файл не існує фізично на диску
# original_path.rename(new_path)

print(original_path)

#--------------------------------------------------------------------------------#

'''Завдання: Маніпуляція з компонентами шляху

1. Створи шлях до файлу "data/report.txt" через Path()
2. Використай with_name() щоб отримати новий шлях з іменем "summary.txt" і виведи його
3. Використай with_suffix() на оригінальному шляху щоб отримати шлях з розширенням ".csv" і виведи
4. Виведи оригінальний шлях і переконайся що він не змінився
5. Пиши сам, показуй коли готово.
'''

from pathlib import Path

# Відносний шлях до файлу — без прив'язки до конкретного диска
my_path = Path("data/report.txt")

# with_name() — замінює ім'я файлу (разом з розширенням), решта шляху залишається
new_my_path1 = my_path.with_name("summary.txt")
print(new_my_path1)  # data/summary.txt

# with_suffix() — замінює тільки розширення, ім'я файлу залишається
new_my_path2 = my_path.with_suffix(".csv")
print(new_my_path2)  # data/report.csv

# Оригінальний шлях не змінився — обидва методи повертають новий об'єкт Path
print(my_path)  # data/report.txt