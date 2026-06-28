# QA сесія 17.04.26
# Тема: 1.5
# Розглянуто:
# -----------------------------------------------

#Функція, яка фільтрує слова довші за 3 символи за допомогою list comprehension.

def filter_words(words):
    return [word for word in words if len(word) > 3]


words = ["hi", "hello", "cat", "python", "go"]
print(filter_words(words))