#
#
# class Darbuotojas:
#     def __init__(self, vardas, pavarde, pareigos):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pareigos = pareigos
#         self._atlyginimas = None
#         self.__asmens_kodas = None
#
#     def get_atlyginimas(self):
#         if self._atlyginimas:
#             return self._atlyginimas
#         return 'Neaišku'
#
#     def set_atlyginimas(self, suma):
#         if int(suma) > 0:
#             self._atlyginimas = suma
#         else:
#             print('Atlyginimas negali būti <= 0')
#
#     def get_asmens_kodas(self):
#         if self.__asmens_kodas:
#             return self.__asmens_kodas
#         return 'Neaišku'
#
#     def set_asmens_kodas(self, asmens_kodas):
#         if int(asmens_kodas) > 0:
#             self.__asmens_kodas = asmens_kodas
#         else:
#             print('Asmens kodas negali būti <= 0')
#
#     def __str__(self):
#         return f'Vardas: {self.vardas} Pavardė: {self.pavarde} Pareigos: {self.pareigos} Atlyginimas: {self.get_atlyginimas()} Asmens kodas: {self.get_asmens_kodas()}'
#
#     def reset_asmens_kodas(self):
#         self.__asmens_kodas = '123123123'
#
# class Vadovas(Darbuotojas):
#     def __init__(self, vardas, pavarde, pareigos, departamentas):
#         super().__init__(vardas, pavarde, pareigos)
#         self.departamentas = departamentas
#
#     def super_change_of_atlyginimas(self):
#         self.set_atlyginimas('123412341234')
#
# class Sarasas:
#     def __init__(self):
#         self.super_sarasas = []
#
#     def change_elemntu_atlyginimas(self):
#         for i in self.super_sarasas:
#             print(i)
#
# # Sukuriame Vadovo objektą
# vadovas1 = Vadovas('Jonas', 'Jonaitis', 'Programuotojas', 'IT')
# vadovas1.super_change_of_atlyginimas()
# vadovas1.reset_asmens_kodas()  # Dabar metodas yra neprivatus
#
# print(vadovas1)
#
# # Pridedame Vadovo objektą į sąrašą
# elem = Sarasas()
# elem.super_sarasas.append(vadovas1)
#
# # Iškviečiame metodą, kad parodytume sąrašo elementus
# elem.change_elemntu_atlyginimas()