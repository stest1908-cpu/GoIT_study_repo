age = 20
user_name = "Boris"
user_name = "Fedor"
user_age = 30
ADULT_THR = 18
user_name = input("Enter your name: ")
if user_name == "Boris":
        print("Hello, Boris!")
if user_name == "Fedor":
        print("Enter is not allowed, Fedor!")
else: print(f"The user {user_name} is not found!")

user_age = int(input("Enter your age: "))
if user_age >= ADULT_THR:
    print(f"{user_name} is an adult.")
else:
    print(f"{user_name} is a minor.")

   