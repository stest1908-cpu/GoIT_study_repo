a = 0.2 + 0.1
print(a)  # Виведе 0.30000000000000004 

b = 0.3 + 0.4
print(b)  # Виведе 0.7

#Якщо при обчисленнях точність стає важливою, програмісти на Python використовують спеціальний модуль Decimal
from decimal import Decimal, getcontext
getcontext().prec = 3  # Встановлюємо точність до 3 знаків після коми
c = Decimal('0.2') + Decimal('0.1')
print(c)  # Виведе 0.3

from decimal import Decimal, getcontext
getcontext().prec = 4  # Встановлюємо точність до 4 знаків після коми
d = Decimal('0.57') / Decimal('0.1123')
print(d)  # Виведе 5.18

#Комплексні числа позначаються як complex. Використовується для представлення комплексних чисел, що складаються з реальної (дійсної) та уявної частини. Комплексні числа в Python записуються у формі a + bj, де a є реальною частиною, а b — уявною частиною, і j є символом уявної одиниці.
#Наприклад 1 + 2j, 3.14 - 5.5j.

int_number = 3
float_number = 3.3
complex_number = 3.3 + 2j
print(int_number)  # Виведе 3
print(float_number)  # Виведе 3.3
print(complex_number)  # Виведе (3.3+2j)

z = 3 + 5j
print(type(z)) # <class 'complex'>
print(z.real)  # 3.0 (дійсна частина)
print(z.imag)  # 5.0 (уявна частина)