name = 'Alice'
age = 30
city = 'New York'

message = 'My name is ' + name + '. I am ' + str(age) + ' years old'
print(message)

message = f'My name is {name}. I am {age/2} years old'
print(message)

print(f'My name is {name}. I am {age/2} years old')

print(f'My name is {name}. I am {age/2 = } years old')

message = 'Test 2. My name is {}. I am {} years old. I am from {}'.format(name, age, city) #format це метод який використовується для форматування рядків 
print(message)

message = 'Test 3. My name is %s. I am %d years old. I am from %s' % (name, age, city) # % - це спеціальний символ, який використовується для форматування рядків
print(message)

message = 'Test 4. My name is ' + name + '. I am ' + str(age) + ' years old' + '. I am from ' + city
print(message)