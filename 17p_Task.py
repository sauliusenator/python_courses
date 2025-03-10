class BankoSaskaita:
    def __init__(self, savininkas, pradiniai_pinigai=0):
        self.savininkas = savininkas
        self.__balansas = pradiniai_pinigai  # Privatūs atributas

    def gauti_balansa(self):
        return self.__balansas

    def prideti_pinigus(self, suma):
        if suma > 0:
            self.__balansas += suma
            print(f"Pridėta {suma} eurų. Naujas balansas: {self.__balansas} eurų.")
        else:
            print("Suma turi būti teigiama.")

    def nuskaičiuoti_pinigus(self, suma):
        if suma > 0:
            if suma <= self.__balansas:
                self.__balansas -= suma
                print(f"Nuskaičiuota {suma} eurų. Naujas balansas: {self.__balansas} eurų.")
            else:
                print("Nepakanka lėšų sąskaitoje.")
        else:
            print("Suma turi būti teigiama.")

# Pavyzdys, kaip naudoti klasę
saskaita = BankoSaskaita("Jonas", 100)  # Sukuriame sąskaitą su 100 eurų

print(f"Savininkas: {saskaita.savininkas}, Balansas: {saskaita.gauti_balansa()} eurų")

saskaita.prideti_pinigus(50)  # Pridedame 50 eurų
saskaita.nuskaičiuoti_pinigus(30)  # Nuskaičiuojame 30 eurų
saskaita.nuskaičiuoti_pinigus(150)  # Bandome nuskaičiuoti daugiau nei yra
print(f"Galutinis balansas: {saskaita.gauti_balansa()} eurų")

# Bandome tiesiogiai pasiekti privatų atributą (tai turėtų sukelti klaidą)
# print(saskaita.__balansas)  # Tai sukels AttributeError