#Імпорт модуля datetime та використання його функцій для роботи з датою та часом
from datetime import datetime #імпортуємо клас datetime з модуля datetime

print(datetime.now()) #виводимо поточну дату та час
print(datetime.now().date()) #виводимо поточну дату без часу
print(datetime.now().time()) #виводимо поточний час без дати
print(datetime.now().year) #виводимо поточний рік
print(datetime.now().month) #виводимо поточний місяць
print(datetime.now().day) #виводимо поточний день
print(datetime.now().hour) #виводимо поточну годину
print(datetime.now().minute) #виводимо поточну хвилину
print(datetime.now().second) #виводимо поточну секунду
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) #виводимо поточну дату та час у форматі "рік-місяць-день година:хвилина:секунда"
print(datetime.now().strftime("%d/%m/%Y")) #виводимо поточну дату у форматі "день/місяць/рік"
print(datetime.now().strftime("%B %d, %Y")) #виводимо поточну дату у форматі "місяць день, рік"
print(datetime.now().strftime("%A, %d %B %Y")) #виводимо поточну дату у форматі "день тижня, день місяць рік"
print(datetime.now().strftime("%I:%M %p")) #виводимо поточний час у форматі "година:хвилина AM/PM"
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) #виводимо поточну дату та час з мікросекундами у форматі "рік-місяць-день година:хвилина:секунда.мікросекунда"
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]) #виводимо поточну дату та час з мілісекундами у форматі "рік-місяць-день година:хвилина:секунда.мілісекунда"
