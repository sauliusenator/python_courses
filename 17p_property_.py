

class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos, asmens_kodas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.asmens_kodas = asmens_kodas
        self.pareigos = pareigos
        self.__atlyginimas = None

    @property

    def lytis(self):
        return 'Vyras' if self.asmens_kodas[0] in ['3', '5'] else 'Moteris'

    @property
    def atlyginimas(self):
        return self.__atlyginimas if self.__atlyginimas else 0

    @atlyginimas.setter
    def atlyginimas(self, suma):
        self.__atlyginimas = suma if suma >= 0 else 1

darb1 = Darbuotojas('Jonas', 'Jonaitis', 'Direktorius', '45487896456')

print(
    darb1.lytis
)

# atl = darb1.atlyginimas
# print(atl)
#
# darb1.atlyginimas = 5000
#
# atl2 = darb1.atlyginimas
# print(atl2)