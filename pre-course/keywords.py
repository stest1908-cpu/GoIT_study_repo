# --- Python Keywords Examples ---

# False, True, None - Basic constants
is_active = True
is_finished = False
result = None

# and, or, not - Logical operators
if is_active and not is_finished:
    print("System is running")

# as - Create an alias
import math as m
print(m.pi)

# assert - For debugging (checks if condition is true)
x = 10
assert x > 0, "x must be positive"

# break, continue, for, in, else - Loops and sequences
for i in range(5):
    if i == 2:
        continue # Skip 2
    if i == 4:
        break # Stop at 4
    print(i)
else:
    print("Loop finished successfully")

# class - Define a class (for your Warehouse objects)
class Product:
    def __init__(self, name):
        self.name = name

# def, return - Define a function
def get_status():
    return "OK"

# del - Delete an object
temp_list = [1, 2]
del temp_list[0]

# if, elif, else - Conditional statements
age = 20
if age < 18:
    print("Minor")
elif age == 18:
    print("Fresh adult")
else:
    print("Adult")

# try, except, finally, raise - Exception handling
try:
    # x = 1 / 0
    pass
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution complete")

# from, import - Importing modules
from datetime import datetime
print(datetime.now())

# global - Declare a global variable inside a function
count = 0
def increment():
    global count
    count += 1

# is - Test if two variables point to the same object
a = [1, 2]
b = a
print(a is b) # True

# lambda - Anonymous function (short one-liners)
square = lambda n: n * n
print(square(5))

# nonlocal - Declare a variable in an outer (but not global) scope
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
    inner()
    return x

# pass - A null statement (placeholder)
def future_function():
    pass # I will write code here later

# with - Simplify exception handling (context manager)
with open("test.txt", "w") as f:
    f.write("test")

# yield - Returns a generator (useful for large warehouse databases)
def count_to_three():
    yield 1
    yield 2
    yield 3

generator = count_to_three()
print(next(generator))