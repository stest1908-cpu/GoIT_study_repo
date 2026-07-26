# Модуль 4 | Робота з файлами та модульна система
# Тема: Файл __init__.py
# Розглянуто: __init__.py — запускається при першому імпорті пакету; дозволяє задати скорочені імпорти для користувача; from package import function — працює завдяки __init__.py; __all__ — список для from package import *
# -----------------------------------------------

'''
У версіях Python до 3.3 в пакетах обов'язково потрібно було розмістити допоміжний файл __init__.py. Якщо цього не зробити, то Python не сприймав директорію як пакет та імпортувати з такої директорії нічого не міг. Зараз в цьому немає потреби, але часто такі файли створюються для зворотної сумісності зі старими версіями.

Файл __init__.py — це службовий файл, який інтерпретатор обов'язково виконає під час першого імпорту пакету. Таким чином, якщо вам потрібно виконати якісь дії під час імпорту пакету, ви можете прописати їх у __init__.py.

Зазвичай __init__.py — порожній і нічого не робить. Але, коли структура пакету не занадто проста і там багато модулів та/або пакетів, про які користувачеві знати не обов'язково, ви можете імпортувати те, що користувачеві потрібно, в __init__.py. У такому випадку користувач зможе вже у своєму коді прописати скорочені варіанти імпортів.

Наприклад, у пакеті utility є два пакети: useful та dummy. В кожному з них є модуль functions.py (у кожного свій). А в цих модулях вже є функції nice_function та not_bad відповідно.

# useful/functions.py
def nice_function():
    pass

# dummy/functions.py
def not_bad(s: str) -> str:
    if s.find("not") == -1 or s.find("bad") == -1:
        return s
    else:
        return s.replace("not bad", "good")

Структура проєкту виглядатиме так:

 📦example_init
 ┣ 📂utility
 ┃ ┣ 📂dummy
 ┃ ┃ ┗ 📜functions.py
 ┃ ┣ 📂useful
 ┃ ┃ ┗ 📜functions.py
 ┃ ┗ 📜__init__.py
 ┗ 📜main.py

Користувачеві пакета utility необов'язково знати про внутрішню структуру пакету, бо вона зроблена для зручності розробника пакету.

Якщо залишити файл __init__.py порожнім, то використання функцій nice_function та not_bad буде виглядати якось так:

import utility

utility.useful.functions.nice_function()
utility.dummy.functions.not_bad("Test string")

Це дуже не зручно і користувачеві пакету потрібно буде розібратися, де і що там лежить.

Якщо ж розробник подумав про користувача, то __init__.py має виглядати ось так:

from utility.useful.functions import nice_function
from utility.dummy.functions import not_bad

__all__ = ['nice_function', 'not_bad']

Зверніть увагу на константу __all__ — це список модулів або пакетів, які імпортуються, якщо у виразі from ... import * в кінці вказаний символ *.

Тепер можна скористатися таким імпортом функцій з пакету:

from utility import nice_function, not_bad

nice_function()
not_bad("Test string")

або таким:

from utility import *

nice_function()
not_bad("Test string")

Все повинно працювати без помилок.
'''

#--------------------------------------------------------------------------------#

'''Завдання: Файл __init__.py

Використаємо пакет geometry з попереднього завдання.

1. У папці geometry створи порожній файл __init__.py
2. У __init__.py імпортуй обидві функції з shapes:
      from geometry.shapes import square_area, circle_area
3. У цьому файлі (нижче) використай скорочений імпорт:
      from geometry import square_area, circle_area
4. Виведи площу квадрата зі стороною 4 і площу кола з радіусом 7
5. Пиши сам, показуй коли готово.
'''

# завдяки __init__.py можна імпортувати функції напряму з пакету
from geometry import square_area, circle_area

side = 4
# square_area — функція з geometry.shapes, доступна через geometry.__init__.py
square_result = square_area(side)
print(square_result)  # 16

radius = 7
circle_result = circle_area(radius)
print(circle_result)  # 153.86