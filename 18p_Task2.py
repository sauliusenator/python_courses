# 1. prideti_zenkliuka(tekstas) – prideda žvaigždutę * prie teksto pabaigos.
# 2. apversti_teksta(tekstas) – apverčia pateiktą tekstą.
# 3. Sukurkite funkciją apdoroti_teksta(tekstas, funkcija=None), kuri:
# a. Jei nurodyta funkcija, pritaiko ją tekstui.
# b. Jei funkcija nenurodyta, tiesiog grąžina tekstą mažosiomis raidėmis.

def prideti_zenkliuka(tekstas):
    return prideti_zenkliuka + "*"

def apversti_teksta(tekstas):
    return apversti_teksta[::-1]


def funkcija(func):
    if i in range[1, 5]:
        print(func('Lietuva ir Latvija'))

def sudet_funkcija(func):
    def i_mazasias(tekstas, funkcija=None):
        if funkcija:
            tekstas = funkcija(tekstas)
        return tekstas.lower()
print(
    i_mazasias('Lietuva ir Latvija', apversti_teksta)
)

