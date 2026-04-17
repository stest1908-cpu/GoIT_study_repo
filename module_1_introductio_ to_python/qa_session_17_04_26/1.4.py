#Функція, яка фільтрує слова довші за 3 символи за допомогою циклу for та умовного оператора if.

def filter_words(words):
    result = []

    for word in words:
        if len(word) > 3:
            result.append(word)

    return result


words = ["hi", "hello", "cat", "python", "go"]
print(filter_words(words))