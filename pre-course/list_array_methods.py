# Передкурс | Основи Python
# Тема: List array methods
# Розглянуто:
# -----------------------------------------------

# --- Python List Methods Examples ---

# 1. append() - Adds an element at the end of the list
stock = ["Screws", "Nails"]
stock.append("Bolts")
print(stock)  # ['Screws', 'Nails', 'Bolts']

b = ["apple", "banana", "cherry"]
a = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)


# 2. clear() - Removes all elements from the list
temp_list = [1, 2, 3]
temp_list.clear()
print(temp_list)  # []

# 3. copy() - Returns a copy of the list
original = ["A", "B"]
new_copy = original.copy()
print(new_copy)  # ['A', 'B']

# 4. count() - Returns the number of elements with the specified value
prices = [10, 20, 10, 50, 10]
print(prices.count(20))  # 3

fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

# 5. extend() - Add elements of a list to the end of the current list
delivery = ["Hammers", "Drills"]
stock = ["Screws", "Nails", "Bolts"]
stock.extend(delivery)
print(stock)  # ['Screws', 'Nails', 'Bolts', 'Hammers', 'Drills']

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

# 6. index() - Returns the index of the first element with the specified value
print(stock.index("Bolts"))  # 2

# 7. insert() - Adds an element at the specified position
stock.insert(1, "Wrenches")
print(stock)  # ['Screws', 'Wrenches', 'Nails', ...]

# 8. pop() - Removes the element at the specified position (default is last)
removed_item = stock.pop(2)
print(f"Removed: {removed_item}")
print(stock)

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)  # ['apple', 'cherry']

# 9. remove() - Removes the first item with the specified value
items = ["box", "bag", "box"]
items.remove("box")
print(items)  # ['bag', 'box']

# 10. reverse() - Reverses the order of the list
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)  # [4, 3, 2, 1]

# 11. sort() - Sorts the list (alphabetically or numerically)
stock.sort()
print(stock)  # Sorted list