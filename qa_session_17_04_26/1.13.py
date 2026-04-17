from datetime import date


class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def get_age(self):
        today = date.today()

        age = today.year - self.birth_date.year

        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1

        return age


p = Person("Alex", date(2000, 12, 10))
print(p.get_age())