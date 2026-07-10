# Модуль 4 | Робота з файлами та модульна система
# Тема: Робота з директоріями (Working with directories)
# Розглянуто: mkdir() — створення директорії, iterdir() — перелік вмісту, exists() / is_dir() / is_file() — перевірки
# -----------------------------------------------
'''
Модуль pathlib в Python включає функціонал для ефективної роботи з файловою системою, зокрема з директоріями.

Метод iterdir() використовується для отримання переліку всіх файлів та піддиректорій у вказаній директорії. Цей метод повертає ітератор, який виробляє об'єкти Path для кожного файлу та піддиректорії у директорії, що визначена поточним об'єктом Path.
'''
#Розглянемо приклад використання. В нас є скрипт ex01.py з наступним кодом:
'''
from pathlib import Path

# Створення об'єкту Path для директорії
directory = Path("./picture")

## Виведення переліку всіх файлів та піддиректорій

for item in directory.iterdir():
    print(item)
'''
'''
Ми виведемо список елементів з директорії "./picture" яка знаходить в середині директорії проєкту core_course, де ми запускаємо скрипт ex01.py.

Маємо таку структуру каталогів:

📦core_course
 ┣ 📂picture
 ┃ ┣ 📂Logo
 ┃ ┣ 📜bot-icon.png
 ┃ ┗ 📜mongodb.jpg
 ┗ 📜ex01.py

 
В нашому випадку тоді виведення буде:

picture\\bot-icon.png
picture\\Logo
picture\\mongodb.jpg
'''

'''Для створення нової директорії використовується метод mkdir().

Path.mkdir(mode=0o777, parents=False, exist_ok=False)

Параметри:
- mode - права доступу до директорії, використовуються для Linux і не актуальні для Windows.
- parents - якщо має значення True, створить всі батьківські директорії, які відсутні.
- exist_ok - якщо має значення True, помилка не буде викинута, якщо директорія вже існує.
'''
#Приклад:

from pathlib import Path
directory = Path('/my_directory/new_folder')
directory.mkdir(parents=True, exist_ok=True)

#Для видалення директорії використовується метод rmdir(). Він видаляє директорію, але директорія повинна бути порожньою.

#Приклад:

from pathlib import Path
directory = Path('/my_directory/new_folder')
# ❌ Приклад автора курсу — директорія не існує, впаде FileNotFoundError
# directory.rmdir()

'''
Модуль pathlib також надає декілька методів для перевірки існування та типу файлових об'єктів:
- метод exists() перевіряє, чи існує файл або директорія.
- метод is_dir() перевіряє, чи є об'єкт директорією.
- метод is_file() перевіряє, чи є об'єкт файлом.
'''
#Приклад використання:


from pathlib import Path

path = Path("./picture")

# Перевірка існування
if path.exists():
    print(f"{path} існує")

# Перевірка, чи це директорія
if path.is_dir():
    print(f"{path} є директорією")

# Перевірка, чи це файл
if path.is_file():
    print(f"{path} є файлом")

#Виведення:
#picture існує
#picture є директорією

#--------------------------------------------------------------------------------#

'''Завдання: Робота з директоріями

1. Створи шлях до директорії "test_folder/sub_folder" через Path()
2. Створи цю директорію через mkdir() з parents=True, exist_ok=True
3. Перевір через exists() що вона існує і виведи результат
4. Перевір через is_dir() що це директорія і виведи результат
5. Виведи список всіх елементів у "test_folder" через iterdir()
6. Пиши сам, показуй коли готово.
'''

from pathlib import Path

# Створюємо шлях і одразу всі батьківські папки через parents=True
test_directory = Path("test_folder/sub_folder")
test_directory.mkdir(parents=True, exist_ok=True)

# exists() — повертає True якщо шлях існує на диску
if test_directory.exists():
    print(f"{test_directory} exists")

# is_dir() — повертає True якщо це директорія
if test_directory.is_dir():
    print(f"{test_directory} directory exists")

# iterdir() — повертає ітератор, тому потрібен цикл
for item in Path("test_folder").iterdir():
    print(item)