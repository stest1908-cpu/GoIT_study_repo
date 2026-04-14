is_active = True
is_delete = False

# Перевіряємо: чи активний ТА чи НЕ видалений
if is_active and not is_delete:
    print("Користувач повноцінно працює (Active: True, Delete: False)")

is_active = True
is_delete = False

if is_active:
    print("User is active")
    
    # Ця перевірка відбудеться тільки якщо is_active == True
    if not is_delete:
        print("...and safe from deletion!")
    else:
        print("...but marked for deletion!")

is_active = True
is_delete = False

if is_active == True and is_delete == False:
    print("Все ідеально: активний і не видалений.")

age = 18
is_adult = age >= 18  # True
if is_adult:
    print("Ви дорослий!")

age = 15
is_adult = age >= 18  # False
if not is_adult:
    print("Ви ще не дорослий!")

user_age = 30
ADULT_THR = 18
user_age = int(input("Enter your age: "))
if user_age >= ADULT_THR:
    print(f"{user_age} You are an adult.")
else:
    print(f"{user_age} You are a minor.")  

x = int(input("Enter x: "))
y = int(input("Enter y: "))
if x == y:
    print("x and y are equal. True")
else:
    print("x and y are not equal. False")