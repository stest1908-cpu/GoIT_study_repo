#Заморожені множини в Python, відомі як frozenset, є подібними до звичайних множин set, але з ключовою відмінністю: вони є незмінними. 
# Це означає, що після створення замороженої множини ви не можете додати або видалити елементи з неї.

# Заморожену множину можна створити за допомогою функції frozenset():

my_frozenset = frozenset([1, 2, 3, 4, 5])
print(my_frozenset)

# my_frozenset.add(6) - 
# AttributeError: 'frozenset' object has no attribute 'add'

# Створюємо НОВИЙ frozenset, об'єднуючи старий з числом 6
my_frozenset = my_frozenset | {7}
print(my_frozenset)

#my_frozenset.remove(7)
# AttributeError: 'frozenset' object has no attribute 'remove'

#my_frozenset.discard(7)
# AttributeError: 'frozenset' object has no attribute 'discard'

#Хоча ви не можете змінювати заморожені множини, 
# над ними все ще можна виконувати різні операції, які не змінюють саму множину, такі як об'єднання, перетин і різниця:

a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

union = a | b  # Об'єднання множин
intersection = a & b  # Перетин множин
difference = a - b  # Різниця множин
symmetric_difference = a ^ b  # Симетрична різниця

print(union)  # frozenset({1, 2, 3, 4, 5})
print(intersection)  # frozenset({3})
print(difference)  # frozenset({1, 2})
print(symmetric_difference)  # frozenset({1, 2, 4, 5})
