#Розписати клас Address з атрибутами city та street, а також клас Person з атрибутом name та методом add_address, який додає об'єкт Address до списку адрес. Створити об'єкт Person та додати до нього кілька адрес, потім вивести всі адреси цього об'єкта.

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street


class Person:
    def __init__(self, name):
        self.name = name
        self.addresses = []

    def add_address(self, address):
        self.addresses.append(address)


p = Person("Alex")

p.add_address(Address("Kyiv", "Khreshchatyk"))
p.add_address(Address("Lviv", "Bandery"))

for addr in p.addresses:
    print(addr.city, addr.street)
    print(addr)