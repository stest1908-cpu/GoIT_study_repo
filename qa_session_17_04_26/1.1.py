#Рекурсія на прикладі суми

def recursive_sum(n):
    print(f"-> заходжу в {n}")

    if n == 1:
        print(f"<- база {n}")
        return 1

    result = n + recursive_sum(n - 1)
    print(f"<- виходжу з {n}, result={result}")
    return result


print(recursive_sum(5))