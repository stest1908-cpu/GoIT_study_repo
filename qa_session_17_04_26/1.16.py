# QA сесія 17.04.26
# Тема: 1.16
# Розглянуто:
# -----------------------------------------------

#MRO (Method Resolution Order) - це порядок, в якому Python шукає методи та атрибути в класах при виклику їх на об'єкті. MRO визначає, який метод буде викликаний, якщо він є в декількох класах у спадковій ієрархії.

class A:
    def info(self):
        print("A")


class B(A):
    def info(self):
        print("B")


class C(A):
    def info(self):
        print("C")


class D(C, B):
    pass


d = D()
d.info()
print(D.__mro__)