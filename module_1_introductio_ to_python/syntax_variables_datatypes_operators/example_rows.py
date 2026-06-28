# Модуль 1 | Вступ до Python
# Тема: Example rows
# Розглянуто:
# -----------------------------------------------

message = "Hello world!"
print(message)
print(message[1])  # виведе 'e', оскільки індексація починається з 0
print(message[0:7])  # виведе 'Hell', оскільки індексація починається з 0 і не включає 7
print(message[-1])  # виведе '!', оскільки -1 означає останній символ
print(message[-6:-1])  # виведе 'world', оскільки -

s1 = "Nice"
s2 = "to meet you!"
joined_string = s1 + ' ' + s2
print(joined_string)  # виведе 'Nice to meet you!'
print (f"{s1} {s2}")  # виведе 'Nice to meet you!' за допомогою f-рядка

name = "Oleg"
hello_string = f"Hello, {name}!"
print(hello_string)  # виведе 'Hello, Oleg!'

s1 = 'Have'
s2 = 'a nice day!'
joined_string = f"{s1} {s2}"  # Have a nice day!
print(joined_string)  # виведе 'Have a nice day!'