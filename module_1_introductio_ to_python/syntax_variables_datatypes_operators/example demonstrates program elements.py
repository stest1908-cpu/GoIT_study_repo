# Модуль 1 | Вступ до Python
# Тема: Example demonstrates program elements
# Розглянуто:
# -----------------------------------------------

# Введення (отримання даних)
name = input("Enter your name: ")

# Перетворення (обробка даних)
greeting = f"Hello, {name}!"

# Виведення (виведення даних)
print(greeting)

age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.") 
