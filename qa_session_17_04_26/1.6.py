#Функція, яка фільтрує слова довші за 3 символи за допомогою lambda функції та функції filter.

def filter_words(words):
    return list(filter(lambda word: len(word) > 3, words))

words = ["hi", "hello", "cat", "python", "go"]
print(filter_words(words))