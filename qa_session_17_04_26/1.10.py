#Змінити Person так, щоб він мав всередині обєкт Address з атрибутами city та country. Створити кілька об'єктів Person з різними адресами та вивести їх атрибути.

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


addr = Address("Kyiv", "Khreshchatyk")
p = Person("Alex", 25, addr)

print(p.name)
print(p.address.city)
print(p.address.street)