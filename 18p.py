

def apversti_teksta(tekstas):
    return tekstas[::-1]

# print(apversti_teksta('labas'))

def apversti_sakini(tekstas):
    return " ".join(tekstas.split()[::-1])

# print(apversti_sakini('Hello World My Name Is Python'))

def sudetinga_funkcija(func):
    for i in range(1, 10):
        print(func('Super tekstas 123 312'))

def super_sudetinga_funkcija(func):
    for i in range(1, 20):
        print(func('Labas'))

# sudetinga_funkcija(apversti_sakini)
# super_sudetinga_funkcija(apversti_teksta)

def i_didziasias(tekstas, funkcija=None):
    if funkcija:
        tekstas = funkcija(tekstas)
    return tekstas.upper()

print(
    i_didziasias('labas', apversti_teksta)
)
