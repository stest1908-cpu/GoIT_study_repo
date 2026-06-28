# QA сесія 17.04.26
# Тема: 1.9
# Розглянуто:
# -----------------------------------------------

#Простий клас Adress, створити об'єкт цього класу та викликати метод info для виведення інформації про адресу.

class Adress:
    def __init__(self, country, city, street):
        self.country = country
        self.city = city
        self.street = street

    def info(self):
        print(self.country, self.city, self.street)


addr = Adress("Norway", "Oslo", "Vikings Street, 1")
print(addr.country)
addr.info()