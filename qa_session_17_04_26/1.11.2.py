#Розписати клас Address з атрибутом city, а також клас Person з атрибутом name та конструктором, який приймає необмежену кількість об'єктів Address та зберігає їх у списку. Створити об'єкт Person та додати до нього кілька адрес, потім вивести всі адреси цього об'єкта.

class Address:
    def __init__(self, city):
        self.city = city


class Person:
    def __init__(self, name, *addresses):
        self.name = name
        self.addresses = list(addresses)


a1 = Address("Kyiv")
a2 = Address("Lviv")

p = Person("Alex", a1, a2)

print(p.name)
print(p.addresses)