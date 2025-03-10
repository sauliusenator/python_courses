class Studentas:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        self._pazymiai = []

    def prideti_pazymi(self, pazymys):
        if 1 <= pazymys <= 10:
            self._pazymiai.append(pazymys)
        else:
            print("Pažymys turi būti tarp 1 ir 10.")

    def rodyti_vidurki(self):
        if not self._pazymiai:
            print("Nėra pažymių.")
        vidurkis = sum(self._pazymiai) / len(self._pazymiai)
        return vidurkis

    def __str__(self):
        return f'Studentas: {self.vardas} {self.pavarde}, Vidurkis: {self.rodyti_vidurki()}'


class StudentasLyderis(Studentas):
    def __init__(self, vardas, pavarde):
        super().__init__(vardas, pavarde)

    def prideti_bonus(self, bonus):
        if bonus > 0:
            vidurkis = self.rodyti_vidurki()
            if isinstance(vidurkis, str):
                return vidurkis
            return vidurkis + bonus
        else:
            print("Bonus taškai turi būti teigiami.")


studentas1 = Studentas("Jonas", "Jonaitis")
studentas1.prideti_pazymi(8)
studentas1.prideti_pazymi(9)
studentas1.prideti_pazymi(10)
print(studentas1)

lyderis1 = StudentasLyderis("Marytė", "Marytuks")
lyderis1.prideti_pazymi(7)
lyderis1.prideti_pazymi(9)
print(lyderis1)

bonus_vidurkis = lyderis1.prideti_bonus(2)
print(f"Lyderio vidurkis su bonus taškais: {bonus_vidurkis}")