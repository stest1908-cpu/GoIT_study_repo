# Модуль 4 | Робота з файлами та модульна система
# Тема: Переміщення та копіювання файлів (Moving and copying files)
# Розглянуто: shutil.copy() / shutil.move() — копіювання і переміщення, stat().st_size — розмір файлу, unlink() — видалення
# -----------------------------------------------
'''
Модуль pathlib чудово інтегрується з модулем shutil для виконання операцій копіювання та переміщення файлів. Для копіювання файлів використовується функція shutil.copy() або shutil.copy2().

Приклад копіювання файлу:

import shutil
from pathlib import Path

# Вихідний і цільовий файли
source = Path('/path/to/source/file.txt')
destination = Path('/path/to/destination/file.txt')

# Копіювання файла
shutil.copy(source, destination)

Функція shutil.copy() копіює вміст файлу, але не копіює метадані, тоді як shutil.copy2() копіює і вміст, і метадані.
'''
'''
Для переміщення файлів використовується функція shutil.move().

Приклад переміщення файлу:

import shutil
from pathlib import Path

# Вихідний і цільовий шляхи
source = Path('/path/to/source/file.txt')
destination = Path('/path/to/destination/file.txt')

# Переміщення файла
shutil.move(source, destination)

'''
'''
Метод stat() повертає інформацію про файл, включаючи його розмір.

Отримання розміру файлу

from pathlib import Path

file_path = Path("./picture/bot-icon.png")

# Отримання розміру файла
size = file_path.stat().st_size
print(f"Розмір файла: {size} байтів")

Виведення:
Розмір файла: 2876 байтів
'''
'''
Метод stat() також надає час створення, атрибут st_ctime , і час останньої модифікації файлу, атрибут st_mtime.

from pathlib import Path
import time

file_path = Path("./picture/bot-icon.png")

# Час створення та модифікації
creation_time = file_path.stat().st_ctime
modification_time = file_path.stat().st_mtime

print(f"Час створення: {time.ctime(creation_time)}")
print(f"Час модифікації: {time.ctime(modification_time)}")


Виведення:
Час створення: Fri Dec 29 04:43:16 2023
Час модифікації: Thu May 17 19:59:44 2018
'''
'''
І остання необхідна інформація для роботи з файлами це видалення. Для видалення файлу використовується метод unlink(). Він видаляє файл, на який вказує об'єкт Path.

Синтаксис:

Path.unlink(missing_ok=False)

Параметр missing_ok якщо має значення True, то виняток не буде викинуто, якщо файл не існує. За замовчуванням False, це означає, що буде викинуто виняток FileNotFoundError, якщо файл не існує.


from pathlib import Path

# Створення об'єкту Path для файлу
file_path = Path('/path/to/file.txt')

# Перевірка, чи файл існує, перш ніж видаляти
if file_path.exists():
    file_path.unlink()
    print(f'Файл {file_path} було видалено')
else:
    print(f'Файл {file_path} не існує')

    
У цьому прикладі, перш ніж видалити файл, ми перевіряємо, чи він існує, щоб уникнути винятку FileNotFoundError.
'''
'''
Можна також видалити файл без попередньої перевірки його існування, використовуючи параметр missing_ok.

from pathlib import Path
file_path = Path('/path/to/file.txt')
file_path.unlink(missing_ok=True)

У цьому випадку, якщо файл не існує, виняток не буде викинуто.
'''

#--------------------------------------------------------------------------------#

'''Завдання: Переміщення та копіювання файлів

1. Створи файл "original.txt" через Path() і запиши в нього будь-який текст через write_text()
2. Скопіюй його в "copy.txt" через shutil.copy()
3. Перемісти "copy.txt" в "moved.txt" через shutil.move()
4. Виведи розмір "moved.txt" через .stat().st_size
5. Видали "original.txt" через .unlink()
6. Перевір що "original.txt" більше не існує через exists() і виведи результат
7. Пиши сам, показуй коли готово.
'''
import shutil
from pathlib import Path

# Папка для файлів завдання — абсолютний шлях через r"..."
folder = Path(r"D:\My_GoIT_Repo\task_files")
folder.mkdir(exist_ok=True)

# Оригінальний файл — шлях через оператор /
file_path = folder / "original.txt"
file_path.write_text("Test text", encoding="utf-8")

# shutil.copy() — копіює вміст файлу в новий файл
shutil.copy(file_path, folder / "copy.txt")

# shutil.move() — переміщує файл (copy.txt → moved.txt)
shutil.move(folder / "copy.txt", folder / "moved.txt")

# stat().st_size — розмір файлу в байтах
size_moved = (folder / "moved.txt").stat().st_size
print(f"Розмір файла: {size_moved} байтів")

# unlink() — видаляє файл з диска
if file_path.exists():
    file_path.unlink()
    print(f'Файл {file_path} було видалено')
else:
    print(f'Файл {file_path} не існує')

# exists() після видалення — має повернути False
print(file_path.exists())
