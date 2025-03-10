import datetime


# Knygos klasė
class Knyga:
    publisher = "Penguin"  # Leidėjas (priklauso visoms knygoms)

    def __init__(self, pavadinimas, autorius, metai):
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.metai = metai
        self.prieinama = True  # Pagal nutylėjimą knyga yra prieinama
        self.paskolos_data = None  # Paskolos data, jei knyga paskolinta

    def __str__(self):
        return f"Knyga(pavadinimas='{self.pavadinimas}', autorius='{self.autorius}', metai={self.metai}, prieinama={self.prieinama})"

    def get_book_age(self):
        """Apskaičiuoja knygos amžių"""
        return datetime.datetime.today().year - self.metai

    def yra_klasika(self):
        """Patikrina, ar knyga yra klasika (daugiau nei 50 metų)"""
        return self.get_book_age() > 50

    def skolinti(self):
        """Skolina knygą"""
        self.prieinama = False
        self.paskolos_data = datetime.datetime.today()

    def grazinti(self):
        """Grąžina knygą"""
        self.prieinama = True
        self.paskolos_data = None

    def grynimo_data(self):
        """Grąžina datą, kada knyga turi būti grąžinta (po 14 dienų)"""
        if self.paskolos_data:
            return self.paskolos_data + datetime.timedelta(days=14)
        return None


# Bibliotekos klasė
class Biblioteka:
    def __init__(self):
        self.knygos = []  # Knygų sąrašas

    def prideti_knyga(self, knyga):
        """Prideda knygą į biblioteką"""
        if isinstance(knyga, Knyga):
            self.knygos.append(knyga)
        else:
            print("Klaida: Tik 'Knyga' objektai gali būti pridėti į biblioteką.")

    def rodyti_knygas(self):
        """Rodo visas knygas bibliotekoje"""
        if not self.knygos:
            print("Bibliotekoje nėra knygų.")
        for knyga in self.knygos:
            print(knyga)

    def skolinti_knyga(self, pavadinimas):
        """Skolina knygą pagal pavadinimą"""
        try:
            knyga = next(k for k in self.knygos if k.pavadinimas == pavadinimas)
            if knyga.prieinama:
                knyga.skolinti()
                print(f"Knyga '{pavadinimas}' paskolinta.")
            else:
                print(f"Knyga '{pavadinimas}' šiuo metu nėra prieinama.")
        except StopIteration:
            print(f"Knyga '{pavadinimas}' nerasta bibliotekoje.")

    def grazinti_knyga(self, pavadinimas):
        """Grąžina knygą pagal pavadinimą"""
        try:
            knyga = next(k for k in self.knygos if k.pavadinimas == pavadinimas)
            if not knyga.prieinama:
                knyga.grazinti()
                print(f"Knyga '{pavadinimas}' grąžinta.")
            else:
                print(f"Knyga '{pavadinimas}' nebuvo paskolinta.")
        except StopIteration:
            print(f"Knyga '{pavadinimas}' nerasta bibliotekoje.")

    def filtruoti_knygas(self, *args, **kwargs):
        """Filtruoja knygas pagal pateiktus parametrus"""
        filtruotos_knygos = self.knygos
        if args:
            filtruotos_knygos = [knyga for knyga in filtruotos_knygos if knyga.pavadinimas in args]
        for key, value in kwargs.items():
            if key == "autorius":
                filtruotos_knygos = [knyga for knyga in filtruotos_knygos if knyga.autorius == value]
            elif key == "metai":
                filtruotos_knygos = [knyga for knyga in filtruotos_knygos if knyga.metai == value]
            elif key == "yra_klasika":
                filtruotos_knygos = [knyga for knyga in filtruotos_knygos if knyga.yra_klasika() == value]
        return filtruotos_knygos


# Programos funkcija
def bibliotekos_sistema():
    biblioteka = Biblioteka()

    while True:
        print("\nBibliotekos sistema")
        print("1. Pridėti knygą")
        print("2. Peržiūrėti knygas")
        print("3. Skolinti knygą")
        print("4. Grąžinti knygą")
        print("5. Filtruoti knygas")
        print("6. Išeiti")

        pasirinkimas = input("Pasirinkite veiksmą: ")

        if pasirinkimas == '1':
            pavadinimas = input("Įveskite knygos pavadin
