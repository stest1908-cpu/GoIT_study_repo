#all() function returns True if all items in an iterable are true, otherwise it returns False.
mylist = [True, True, False]
x = all(mylist)
print(x)

mylist = [0, 1, 1]
t = all(mylist)
print(t)

mytuple = (1, True, 1)
x = all(mytuple)
print(x)

myset = {0, 1, 0}
x = all(myset)
print(x)

mydict = {"Banana" : "Apple", 1 : "Orange"}
x = all(mydict)
print(x)

#abs() function returns the absolute value of the specified number.
x = abs(-1.256)
print(x)

x = abs(3+5j)
print(x)

#any() function returns True if any item in an iterable is true, otherwise it returns False. If the iterable object is empty, the any() function will return False.

mylist = [False, True, False]
x = any(mylist)
print(x)

myset = {0, 1, 0}
x = any(myset)
print(x)

mytuple = (0, 1, False)
x = any(mytuple)
print(x)

mydict = {0 : "Apple", 1 : "Orange"}
x = any(mydict)
print(x)

#ascii() function returns a readable version of any object (Strings, Tuples, Lists, etc).
x = ascii("My name is Ståle")
print(x)

#bin() function returns the binary version of a specified integer.
x = bin(5)
print(x)
# The result will always have the prefix 0b

#bool() function returns the boolean value of the specified object. If the object is false, it returns False, otherwise it returns True.
x = bool(1)
print(x)

x = bool(0)
print(x)

#bytearray() function returns a bytearray object which is an array of bytes. The bytearray object is mutable and can be modified after it is created.
x = bytearray(5)
print(x)

#bytes() function returns a bytes object which is an immutable array of bytes. The bytes object is immutable and cannot be modified after it is created.
x = bytes(7)
print(x)

#callable() function returns True if the specified object is callable, otherwise it returns False.
def x():
  a = 5

print(callable(x))

#chr() function returns a character from the specified Unicode code.
x = chr(97)
print(x)   

#classmethod() function is a built-in function that returns a class method for a given function. A class method is a method that is bound to the class and not the instance of the class. It can modify the class state that applies across all instances of the class, rather than just the state of a single instance.
class MyClass:
  @classmethod
  def my_class_method(cls):
    return "This is a class method"
print(MyClass.my_class_method())

#compile() function returns the specified source as an object, ready to be executed.
x = compile('print("Hello World")', 'hello.py', 'exec')
exec(x)

x = compile('print(55)', 'test', 'eval')
exec(x)

#complex() function returns a complex number with the value real + imag*1j or converts a string or number to a complex number.
x = complex(2, 3)
print(x)

#delattr() function deletes the specified attribute (property or method) from the specified object.
class Person:
  name = "John"
  age = 36
  country = "Norway"

delattr(Person, 'age')
# The Person object will no longer contain an "age" property

#dict() function creates a dictionary object.
x = dict(name = "John", age = 36, country = "Norway")
print(x)

#dir() function returns a list of the specified object's properties and methods.
class Person:
  name = "John"
  age = 36
  country = "Norway"

print(dir(Person))

#divmod() function takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.
x = divmod(5, 2)
print(x)

#enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
mylist = ("apple", "banana", "cherry")
x = enumerate(mylist)
print(list(x))

#eval() function parses the expression passed to this function and runs python expression (code) within the program.
x = eval('3 + 5')
print(x)

#exec() function executes the specified code (or object).
x = 'name = "John"\nprint(name)'
exec(x)

#filter() function constructs an iterator from elements of an iterable for which a function returns true.
ages = [1, 5, 12, 17, 18, 24, 32, 45, 65, 72, 80, 81.25]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)

#float() function converts the specified value into a floating point number.
x = float(1)
print(x)

#format() function formats a specified value into a specified format.
x = format(0.5, '%')
print(x)  

x = format(6, 'b')
print(x)

#frozenset() function returns a frozenset object which is an immutable set. The frozenset object is immutable and cannot be modified after it is created.
x = frozenset([1, 2, 3, 4, 5])
print(x)

#getattr() function returns the value of the specified attribute (property or method) from the specified object.
class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'age')
print(x)  

class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'page', 'my message')
print(x)

#globals() function returns a dictionary containing the current scope's global variables.
x = globals()
print(x)

x = globals()
print(x["__file__"])

#hasattr() function returns True if the specified object has the specified attribute (property/method), otherwise it returns False.
class Person:
  name = "John"
  age = 36
  country = "Norway"

x = hasattr(Person, 'country')
print(x)

#hash() function returns the hash value of a specified object.
x = hash("Test")
print(x)

#help() function invokes the built-in help system.
help(print)

#hex() function converts a specified number into a hexadecimal number.
x = hex(255)
print(x)

#id() function returns the id of an object.
x = ('apple', 'banana', 'cherry')
y = id(x)
print(y)

# This value is the memory address of the object and will be different every time you run the program

#input() function allows user input.
name = input("Enter your name: ")
print("Hello, " + name)

#int() function converts the specified value into an integer number.
x = int(2.8)
print(x)

x = int("12")

print(x)

#isinstance() function returns True if the specified object is of the specified type, otherwise it returns False.
x = isinstance(5, int)

print(x)

x = isinstance("Hello", (float, int, str, list, dict, tuple))
print(x)

class myObj:
  name = "John"

y = myObj()

x = isinstance(y, myObj)
print(x)

#issubclass() function returns True if the specified class is a subclass of the specified object, otherwise it returns False.
class myAge:
  age = 36

class myObj(myAge):
  name = "John"
  age = myAge

x = issubclass(myObj, myAge)
print(x)

#iter() function returns an iterator object.
x = iter(["apple", "banana", "cherry", "orange"])
print(next(x))
print(next(x))
print(next(x))
print(next(x))

#len() function returns the number of items in an object.
mylist = ["apple", "orange", "cherry"]

x = len(mylist)

print(x)


mylist = "Sergey"
x = len(mylist)
print(x)

#list() function creates a list object.
x = list(("apple", "banana", "cherry", "orange"))
print(x)

#locals() function returns a dictionary containing the current scope's local variables.
x = locals()
print(x)

x = locals()
print(x["__file__"])

#map() function applies a specified function to each item of an iterable and returns a map object (an iterator).
def myFunc(x):
  return len(x)

x = map(myFunc, ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango'))

print(x)

#convert the map into a list, for readability:
print(list(x))

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(x)

#convert the map into a list, for readability:
print(list(x))

#max() function returns the largest item in an iterable or the largest of two or more arguments.
x = max(5, 10)
print(x)

x = max("Mike", "John", "Vicky")
print(x)


a = (1, 5, 3, 9)
x = max(a)

print(x)
