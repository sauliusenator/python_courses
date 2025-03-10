class Darbuotojas:
    def __init__(self, vardas, pavarde, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.__atlyginimas = None
        self.atlyginimas = atlyginimas

    @property
    def atlyginimas(self):
        return self.__atlyginimas

    @atlyginimas.setter
    def atlyginimas(self, suma):
        if suma < 500:
            raise ValueError("Atlyginimas negali būti mažesnis nei 500.")
        self.__atlyginimas = suma

    @property
    def mokesciai(self):
        return self.__atlyginimas * 0.20 if self.__atlyginimas else 0

    def __str__(self):
        return f'Darbuotojas: {self.vardas} {self.pavarde}, Atlyginimas: {self.atlyginimas}, Mokesčiai: {self.mokesciai}'


try:
    darbuotojas1 = Darbuotojas("Ramunas", "Ramunaitis", 600)
    print(darbuotojas1)

    darbuotojas1.atlyginimas = 800
    print(darbuotojas1)

    darbuotojas1.atlyginimas = 400
except ValueError as e:
    print(e)