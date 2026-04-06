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
