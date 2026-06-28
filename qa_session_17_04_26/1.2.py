# QA сесія 17.04.26
# Тема: 1.2
# Розглянуто:
# -----------------------------------------------

#Фунція для підрахунку суми двох чисел з плаваючою комою, яка демонструє проблему точності при використанні типу float та її вирішення за допомогою типу Decimal.

from decimal import Decimal

def sum_float(): #1usage
    return 0.1 + 0.2

def sum_decimal(): #1usage
    return Decimal(0.1) + Decimal(0.2)

print("float:", sum_float())
print("decimal:", sum_decimal())