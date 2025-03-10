
class Gyvunas:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def judeti(self):
        print(f"{self.vardas} juda.")


class Kate(Gyvunas):
    def miaukseti(self):
        print(f"{self.vardas} sako MIAU!")


class Suo(Gyvunas):
    def lot(self):
        print(f"{self.vardas} sako AU AU!")

kate = Kate("Miau", 3)
suo = Suo("Rex", 5)

kate.judeti()
kate.miaukseti()

suo.judeti()
suo.lot()



########################################################
