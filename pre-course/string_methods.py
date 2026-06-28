# Передкурс | Основи Python
# Тема: String methods
# Розглянуто:
# -----------------------------------------------

# --- Python String Methods Examples ---

text = "hello world"

# capitalize() - Capitalizes the first character
print(text.capitalize()) # "Hello world"

# casefold() - Converts string into lower case (stronger than lower())
print("HELLO".casefold()) # "hello"

# center() - Returns a centered string
print("Warehouse".center(20, "-")) # "-----Warehouse-----"

txt = "banana"

x = txt.center(20, "O")

print(x)

# count() - Returns the number of times a value occurs
print("apple apple cherry".count("apple")) # 2

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)

# encode() - Returns an encoded version of the string
print("Hello".encode()) # b'Hello'

# endswith() - Returns true if the string ends with the specified value
print("report.pdf".endswith(".pdf")) # True

txt = "Hello, welcome to my world."

x = txt.endswith("my world.")

print(x)

# expandtabs() - Sets the tab size of the string
print("Item\tPrice".expandtabs(10))

txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x)

txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

# find() - Searches for a value and returns its position
print("Find the key".find("key")) # 9

#Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."

x = txt.find("e", 5, 10)

print(x)

# format() - Formats specified values in a string
print("Price: {:.2f} UAH".format(150.5)) # "Price: 150.50 UAH"

# format_map() - Formats specified values using a dictionary
data = {'item': 'Screws', 'qty': 50}
print("{item}: {qty} pcs".format_map(data))

# index() - Searches for a value and returns its position (raises error if not found)
print("Search here".index("here")) # 7

# isalnum() - Returns True if all characters are alphanumeric
print("Product123".isalnum()) # True

# isalpha() - Returns True if all characters are in the alphabet
print("OnlyLetters".isalpha()) # True

# isascii() - Returns True if all characters are ASCII
print("Hello123".isascii()) # True

# isdecimal() - Returns True if all characters are decimals
print("12345".isdecimal()) # True

# isdigit() - Returns True if all characters are digits
print("123".isdigit()) # True

# isidentifier() - Returns True if string is a valid identifier (variable name)
print("my_var".isidentifier()) # True

# islower() - Returns True if all characters are lower case
print("hello".islower()) # True

# isnumeric() - Returns True if all characters are numeric
print("½".isnumeric()) # True

# isprintable() - Returns True if all characters are printable
print("Hello\n".isprintable()) # False (due to \n)

# isspace() - Returns True if all characters are whitespaces
print("   ".isspace()) # True

# istitle() - Returns True if string follows title case rules
print("Hello World".istitle()) # True

# isupper() - Returns True if all characters are upper case
print("HELLO".isupper()) # True

# join() - Joins elements of an iterable to the end of the string
print(", ".join(["Screws", "Nails", "Tools"])) # "Screws, Nails, Tools"

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

# ljust() - Returns a left justified version of the string
print("Left".ljust(10, ".")) # "Left......"

# lower() - Converts a string into lower case
print("PYTHON".lower()) # "python"

# lstrip() - Returns a left trim version of the string
print("   space".lstrip()) # "space"

# maketrans() & translate() - Used to replace characters
mytable = str.maketrans("S", "P")
print("Screws".translate(mytable)) # "Pcrews"

# partition() - Returns a tuple where the string is parted into three parts
print("item-123-warehouse".partition("-")) # ('item', '-', '123-warehouse')

# replace() - Returns a string where a value is replaced with another
print("Old version".replace("Old", "New")) # "New version"

# rfind() - Searches for the last occurrence of a value
print("one two one".rfind("one")) # 8

# rindex() - Searches for the last occurrence of a value (raises error if not found)
print("one two one".rindex("one")) # 8

# rjust() - Returns a right justified version of the string
print("Right".rjust(10, ".")) # ".....Right"

# rpartition() - Returns a tuple (last occurrence of separator)
print("item-123-warehouse".rpartition("-")) # ('item-123', '-', 'warehouse')

# rsplit() - Splits the string at the specified separator from the right
print("a, b, c".rsplit(", ", 1)) # ['a, b', 'c']

# rstrip() - Returns a right trim version of the string
print("space   ".rstrip()) # "space"

# split() - Splits the string at the specified separator
print("Screws,Nails,Bolts".split(",")) # ['Screws', 'Nails', 'Bolts']

# splitlines() - Splits the string at line breaks
print("Line 1\nLine 2".splitlines()) # ['Line 1', 'Line 2']

# startswith() - Returns True if string starts with a specified value
print("INV-001".startswith("INV")) # True

# strip() - Returns a trimmed version of the string (both sides)
print("  clean me  ".strip()) # "clean me"

# swapcase() - Swaps cases, lower becomes upper and vice versa
print("PyThOn".swapcase()) # "pYtHoN"

# title() - Converts the first character of each word to upper case
print("hello world software".title()) # "Hello World Software"

# translate() - Returns a string where some specified characters are replaced with the character described in a dictionary
#use a dictionary with ascii codes to replace 83 (S) with 90 (Z):
mydict = {83:  90}

txt = "Hello Sam!"

print(txt.translate(mydict))

# upper() - Converts a string into upper case
print("update".upper()) # "UPDATE"

# zfill() - Fills the string with zeros at the beginning
print("42".zfill(10)) # "0000000042" (useful for SKU/ID numbers)

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))