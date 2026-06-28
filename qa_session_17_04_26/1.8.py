# QA сесія 17.04.26
# Тема: 1.8
# Розглянуто:
# -----------------------------------------------

#Програма, яка створює клас Person з атрибутами name та age, а також створює кілька об'єктів цього класу та виводить їх атрибути.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Alex", 25)
p2 = Person("Marta", 30)
p3 = Person("John", 20)

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)