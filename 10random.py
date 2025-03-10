# import random
#
# atsitiktinis_skaicius = random.randint(1, 10)
#
# print(f'Atsitiktinis int skaicius nuo 1 iki 10: {random.randint(1,10)}')
# print(f'Atsitiktinis int skaicius nuo 1 iki 10: {random.randint(1,10)}')
# print(f'Atsitiktinis int skaicius nuo 1 iki 10: {random.randint(1,10)}')
# print(f'Atsitiktinis int skaicius nuo 1 iki 10: {random.randint(1,10)}')
# print(f'Atsitiktinis int skaicius nuo 1 iki 10: {random.randint(1,10)}')
# print(f'Atsitiktinis int skaicius nuo 1 iki 10: {random.randint(1,10)}')
# print(f'Atsitiktinis int skaicius nuo 1 iki 10: {random.randint(1,10)}')

# while True:
#     skaicius = input('Ar jus galite atspeti skaiciu, kol neatspesite tinkamo neiseisite: ')
#     if skaicius == random.randint(1,10):
#         break

# 1. TASK --------------------------------------------
# import random
#
# atsitiktinis_skaicius = random.randint(1, 100)
# print(f'Atsitiktinis int skaicius nuo 1 iki 10: {random.randint(1,100)}')

# random_float = random.uniform(1, 50)
# print(f"Atsitiktinis skaicius nuo 1 iki 50 {random.float(1,100)}")
#
# import random



# 2. Sugeneruojame atsitiktinį skaičių su uniform(), kuris yra tarp 1 ir 50
# random_float = random.uniform(1, 50)
# print(f"Atsitiktinis skaičius su decimalais tarp 1 ir 50: {random_float(1,5)}")

# --------------------------- CHOICE------------------------------------
# import random
# from random import randint, choice, sample, gammavariate
#
# random_number = randint(1,10)
# print(random_number)
#
# random_month = choice(['sausis', 'vasaris', 'kovas'])
# print(random_month)
# ---------------------------------

# kad pastoviai nerasyti random galime rasyti ... rn (vietoj random zodzio
# import random
# random_number = random.randint(20, 25)
# random_month = random.choice(['sausis', "vasaris", 'kovas'])

# 2. TASK  Specifinių funkcijų importavimas------------------
# IR
#  TASK  Modulio trumpinimas naudojant alias ------------------

# from random import randint, choice

# import datetime as dt
# print(randint(1, 10))
# print(choice(['obuolys', 'bananas', 'kriause', 'vysnia']))
# print(dt.datetime.now())




# from random import randint as rnt
# print(rnt(1, 10))
#
#
# from random import randint as rnt
# import random
# def generate_random_nuber(x, y):
#     return random.randint(x, y)

# def sample():
#     print(123)

# ////////////// NENAUDOTI///////////////
# parinktis = sample(['sausis', 'vasaris', 'kovas'], k=3)
# print(parinktis)
# ////////////// NENAUDOTI///////////////

# # 3. TASK     ------------------  Specifinių funkcijų importavimas su alias
# Užduotis 5:

# from math import sqrt as sq
# print(sq(625))
#
# import math as sq
# number = 625 # from math import aqrt as sq
# sqrt = sq.sqrt(number)
# print(sqrt)
#
# # Užduotis 6:
# from math import * #//// NETEISINGAI //// NENAUDOTI " * " nes daug duomenu importuoja
# print(sin(90))
#
# from math import sin  #//// TEISINGIAU
# print(sin(90))


# 7. uzduotis ////////////// Importai iš mūsų sukurto modulio
# galima iportuoti is kito failo
# a = 9
# b = 2
#
# print(a + b)
# print(a * b)
#
# # 8. uzduotis ////////////Visas modulio importavimas
# from mylib import matematika, matematika as m
#
# print(matematika.sudetis(1, 2))
# print(matematika.daugyba(5, 4))

# 9. uzduotis//////////////Specifinių funkcijų importavimas



