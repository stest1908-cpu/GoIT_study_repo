# Модуль 3 | Дата, час та рядки
# Тема: Line creation options
# Розглянуто:
# -----------------------------------------------

##Варіанти створення рядків

#Для створення рядків можна скористатися одинарними або подвійними лапками:

this_is_string = "Hi there!"

the_same_string = 'Hi there!'

this_is_string == the_same_string# True

print(this_is_string)
print(the_same_string)

#Але що робити, якщо нам потрібен текст із перенесенням рядків (коли в тексті більше одного рядка)? 
# Для цього можна скористатися потрійним повторенням лапок:

text = """This is first line
And second line
Last third line"""
print(text)

song = '''Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh'''
print(song)

#В цьому прикладі змінна text містить три рядки, а song — чотири рядки.

'''
Коли інтерпретатор виявляє лапки, повторені тричі, 
він сприймає усі символи до наступних трьох лапок, 
які закривають рядок, як символи рядка.
'''

#Зворотна ситуація, у вас є довгий рядок, який не повинен містити перенесень,
#  але в коді його незручно відобразити одним рядком.

one_line_text = "Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways: single quotes, double quotes, triple quoted."

#Щоб структурувати код і не додавати зайвих перенесень, ви можете розбити одну рядкову змінну на декілька частин:

one_line_text = "Textual data in Python is handled with str objects," \
                " or strings. Strings are immutable sequences of Unicode" \
                " code points. String literals are written in a variety " \
                " of ways: single quotes, double quotes, triple quoted."

print(one_line_text)
#Зверніть увагу на символ \ в кінці першого та другого рядка коду, 
# він вказує інтерпретатору ігнорувати закінчення рядка і продовжити відразу з наступного.

#Змінна one_line_text в обох прикладах буде містити один і той самий текст без перенесень.

'''У Python, коли ви поміщаєте два рядкових літерали поруч, 
вони автоматично конкатенуються (об'єднуються в один рядок). 
Це відомо як неявна конкатенація рядків:'''

("spam " "eggs") == "spam eggs"  # True

'''
Вираз ліворуч та вираз праворуч — це два рівнозначні записи одного і того самого тексту 'spam eggs' і, 
з погляду Python, — вони нерозрізнені. У нашому випадку, "spam " та "eggs" - це два окремих рядкових літерала, 
але коли вони розміщені один за одним без оператора додавання (+), Python автоматично об'єднує їх у один рядок.
'''

'''
Це часто використовується для зручності, 
особливо при написанні довгих рядків і тому змінну one_line_text можна записати наступним чином.
'''
one_line_text = ("Textual data in Python is handled with str objects,"
                " or strings. Strings are immutable sequences of Unicode"
                " code points. String literals are written in a variety "
                " of ways: single quotes, double quotes, triple quoted.")

print(one_line_text)

'''
Неявна конкатенація рядків - це корисна властивість мови Python, 
яка дозволяє писати більш чистий і читабельний код, 
особливо коли працюєте з довгими рядками або рядками, 
що формуються на основі декількох частин.
'''

#Наприклад, в майбутньому, це дуже допомагає при створенні SQL запитів до бази даних:

query = ("SELECT * "
         "FROM some_table "
         "WHERE condition1 = True "
         "AND condition2 = False")

print(query)