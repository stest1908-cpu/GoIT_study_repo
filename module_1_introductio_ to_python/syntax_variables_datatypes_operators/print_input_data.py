#Вивід даних
print("Hello, World!")
print(42)
x= 10
print("Значення x:", x)
print(f"Значення x: {x}")  # Використання f-рядка для форматування виводу   
print("Привіт", end=" ")
print("світ!")  # Виведе "Привіт світ!" на одній строке

#Введення даних
a = input("Enter a value for a: ")  # Введення даних користувачем, зберігається як рядок
print("You entered:", a)

c = int(input("Enter a value for c: "))  # Введення даних та перетворення на ціле число
print(f"You entered: {c}")

d = float(input("Enter a value for d: "))  # Введення даних та перетворення на число з плаваючою точкой
print(f"You entered: {d}")

e = bool(input("Enter a value for e (True/False): "))  # Введення даних та перетворення на булеве значение
print(f"You entered: {e}")