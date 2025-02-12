

class Claculator:
    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def sub(num1, num2):
        return num1 - num2

class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos

    @classmethod
    def sukurt_is_vienos_eilutes(cls, eilute):
        vardas, pavarde, pareigos = eilute.split()
        return  cls(vardas, pavarde, pareigos)

    def __str__(self):
        return f'{self.vardas} {self.pavarde}, pareigos: {self.pareigos}'

    def pakeisti_pareigas(self, naujos_pareigos):
        self.pareigos = naujos_pareigos

eilute = 'Jonas Jonaitis Inzinierius'
darbuotojas = Darbuotojas.sukurt_is_vienos_eilutes(eilute)
print(darbuotojas)

darbuotojas.pakeisti_pareigas('Projektu Vadovas')
print(darbuotojas)
