class Person:
    def __init__(self, name):
        self.name = name

    # def info(self):
    #     return f"Person: {self.name}"


class Child(Person):
    def __init__(self, name, father, mother):
        super().__init__(name)
        self.father = father
        self.mother = mother

    def info(self):
        return f"{self.name}, child of {self.father.name} and {self.mother.name}"


father = Person("John")
mother = Person("Anna")
child = Child("Tom", father, mother)
print(child.info())