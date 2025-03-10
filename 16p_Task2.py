class Variklis:
    def __init__(self, galia: int):
        self.galia = galia

    def startuoti(self):
        print(f"Variklis veikia su galia: {self.galia} arklio galių")


class Automobilis:
    def __init__(self, marke: str, modelis: str, variklis: Variklis):
        self.marke = marke
        self.modelis = modelis
        self.variklis = variklis

    def vaziuoti(self):
        print(f"{self.marke} {self.modelis} pradeda važiuoti.")
        self.variklis.startuoti()


variklis1 = Variklis(150)
variklis2 = Variklis(200)
variklis3 = Variklis(300)

auto1 = Automobilis("Toyota", "Corolla", variklis1)
auto2 = Automobilis("BMW", "320i", variklis2)
auto3 = Automobilis("Audi", "A6", variklis3)

auto1.vaziuoti()
print()
auto2.vaziuoti()
print()
auto3.vaziuoti()