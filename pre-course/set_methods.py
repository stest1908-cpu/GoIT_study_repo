# --- Python Set Methods Examples ---

# 1. add() - Adds an element to the set
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)

# 2. clear() - Removes all elements from the set
temp_set = {1, 2, 3}
temp_set.clear()
print(temp_set) # set()

# 3. copy() - Returns a copy of the set
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

# 4. difference() ( - ) - Returns a set containing the difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print(set1 - set2) # {'banana', 'cherry'}

# 5. difference_update() ( -= ) - Removes items that exist in both sets
set1.difference_update(set2)
print(set1) # {'banana', 'cherry'}

# 6. discard() - Remove the specified item
fruits.discard("banana")

# 7. intersection() ( & ) - Returns items present in both sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2) # {2, 3}

# 8. intersection_update() ( &= ) - Keeps only items present in both sets
s1.intersection_update(s2)

# 9. isdisjoint() - Returns True if sets have NO intersection
print({1, 2}.isdisjoint({3, 4})) # True

# 10. issubset() ( <= ) - Returns True if all items of this set are in another
print({1, 2}.issubset({1, 2, 3})) # True

# 11. issuperset() ( >= ) - Returns True if this set contains another set
print({1, 2, 3}.issuperset({1, 2})) # True

# 12. pop() - Removes a random element from the set
fruits.pop()

# 13. remove() - Removes the specified element (raises error if missing)
fruits.add("orange")
fruits.remove("orange")

# 14. symmetric_difference() ( ^ ) - Returns items NOT present in both sets
print({1, 2, 3} ^ {2, 3, 4}) # {1, 4}

# 15. symmetric_difference_update() ( ^= ) - Updates set with symmetric difference
s1 = {1, 2, 3}
s1.symmetric_difference_update({2, 3, 4})

# 16. union() ( | ) - Returns a set containing the union of sets
print({1, 2} | {3, 4}) # {1, 2, 3, 4}

# 17. update() ( |= ) - Update the set with the union of itself and others
s1.update({5, 6})