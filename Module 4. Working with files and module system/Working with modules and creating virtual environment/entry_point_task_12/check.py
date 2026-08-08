# демонструє, що функції з calculator.py можна використати окремо від main.py
from calculator import add, multiply

print(add(2, 3))
print(multiply(2, 3))

# справжня перевірка if __name__ == "__main__": — імпорт main.py не повинен викликати main()
# якщо це запрацює без запиту чисел (input), значить guard працює правильно
import main

