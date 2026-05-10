#Вираз if-elif-else

'''Створіть програму на Python, яка визначає категорію розробника (Junior, Middle, Senior) на основі його стажу роботи.

Задачі:

Отримайте від користувача стаж роботи через функцію input та збережіть це значення у змінній work_experience як ціле число.
На основі значення work_experience вам потрібно визначити рівень розробника і зберегти це як рядок у змінній developer_type. Використовуйте наступні правила:
Якщо стаж роботи від 1 року до 5 років включно, developer_type повинен бути "Middle".
Якщо стаж роботи до 1 року включно, developer_type повинен бути "Junior".
Якщо стаж роботи більше 5 років, developer_type повинен бути "Senior".
Очікуваний результат:

Програма має показати рівень розробника в залежності від стажу роботи, який ввів користувач.

Підказки:

Уважно перевірте умови у вашій структурі if-elif-else, щоб вони відповідали правилам визначення рівня розробника.
Не забудьте використати int() для перетворення введеного користувачем рядка у ціле число.
'''
try:
    work_experience = int(input("Enter your full work experience in years: "))
    if work_experience <= 1:
        developer_type = "Junior"
    elif 1 < work_experience <= 5:
        developer_type = "Middle"
    else:
        developer_type = "Senior"

    print(f"You are a {developer_type} developer.")
except ValueError:
    print("Please enter a valid number for work experience.")   