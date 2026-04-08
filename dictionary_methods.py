# --- Python Dictionary Methods Examples ---

# 1. clear() - Removes all elements from the dictionary
item = {"name": "Hammer", "price": 250}
item.clear()
print(item)  # {}

# 2. copy() - Returns a copy of the dictionary
stock_data = {"SKU001": 50, "SKU002": 100}
backup = stock_data.copy()
print(backup)

# 3. fromkeys() - Returns a dictionary with the specified keys and value
keys = ("section_A", "section_B", "section_C")
default_value = "empty"
warehouse_map = dict.fromkeys(keys, default_value)
print(warehouse_map) # {'section_A': 'empty', ...}

# 4. get() - Returns the value of the specified key
# (Safe way: doesn't crash if key is missing)
inventory = {"nails": 500, "screws": 1000}
print(inventory.get("nails")) # 500
print(inventory.get("bolts", 0)) # 0 (default value if not found)

# 5. items() - Returns a list containing a tuple for each key-value pair
print(inventory.items()) # dict_items([('nails', 500), ('screws', 1000)])

# 6. keys() - Returns a list containing the dictionary's keys
print(inventory.keys()) # dict_keys(['nails', 'screws'])

# 7. pop() - Removes the element with the specified key
inventory.pop("nails")
print(inventory) # {'screws': 1000}

# 8. popitem() - Removes the last inserted key-value pair
inventory["drills"] = 10
inventory.popitem()
print(inventory) # 'drills' is removed

# 9. setdefault() - Returns value of key. If key doesn't exist, inserts it.
category = inventory.setdefault("category", "hardware")
print(inventory) # {'screws': 1000, 'category': 'hardware'}

# 10. update() - Updates the dictionary with specified key-value pairs
inventory.update({"screws": 1200, "status": "in stock"})
print(inventory) # screws updated, status added

# 11. values() - Returns a list of all values in the dictionary
print(inventory.values()) # dict_values([1200, 'hardware', 'in stock'])