# Модуль 1 | Вступ до Python
# Тема: Dictionary method update
# Розглянуто:
# -----------------------------------------------

#Метод update() використовується для оновлення словника іншим словником або парами ключ-значення. 
#Якщо в вас є словник my_dict = {"name": "Alice", "age": 25} і ви виконаєте my_dict.update({"email": "alice@example.com", "age": 26}), то словник my_dict буде оновлено новими парами ключ-значення, 
#де ключ "email" буде додано в словник, а значення ключа "age" буде оновлено.

my_dict = {"name": "Alice", "age": 25}
print(my_dict)
my_dict.update({"email": "alice@example.com", "age": 26})
print(my_dict)
my_dict.update({"name": "Bob", 'city': "New York"})
print(my_dict)
