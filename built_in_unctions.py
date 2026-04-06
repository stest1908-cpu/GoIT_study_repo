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

x = abs(-1.256)
print(x)

x = abs(3+5j)
print(x)

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