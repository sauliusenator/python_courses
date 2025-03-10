class Asmuo:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

class Darbuotojas(Asmuo):
    def __init__(self, vardas, amzius, pareigos):
        super().__init__(vardas, amzius)
        self.pareigos = pareigos

    def __str__(self):
        return f"Vardas: {self.vardas}, Amžius: {self.amzius}, Pareigos: {self.pareigos}"

darbuotojas = Darbuotojas("Jonas", 30, "Programuotojas")
print(darbuotojas)
print('-' * 20)
########################################################################################################################

class TransportoPriemone:
    def judeti(self):
        print("Transporto priemonė juda")

class Dviratis(TransportoPriemone):
    def judeti(self):
        super().judeti()
        print("Dviratis važiuoja pedalais")

transporto_priemone = TransportoPriemone()
dviratis = Dviratis()

transporto_priemone.judeti()
print('-' * 20)
dviratis.judeti()