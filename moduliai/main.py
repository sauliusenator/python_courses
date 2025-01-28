
from aritmetika import atimtis, dalyba

# 11. TASK///// Importai iš folderio /////////
# Užduotis 11:
# 1. Sukurkite folderį moduliai.
# 2. Sukurkite šiame folderyje failą aritmetika.py su funkcijomis atimtis(a, b) ir
# dalyba(a, b).
# 3. Sukurkite main.py, kuris importuoja aritmetika ir iškviečia šias funkcijas.

print(atimtis(9, 10))
print(round(dalyba(15, 3)))
# //////////////////////////////////////////////////////////////////////////////////////

from moduliai import aritmetika

# 12. TASK  /////////////Visas modulio importavimas iš folderio /////////////
# Užduotis 12:
# 1. Sukurkite Python programą, kuri importuoja moduliai.aritmetika.
# 2. Naudokite moduliai.aritmetika.atimtis(20, 5) ir
# moduliai.aritmetika.dalyba(10, 2).
# 3. Išspausdinkite rezultatus.
print(aritmetika.atimtis(20, 5))
print(aritmetika.dalyba(10, 2))
# //////////////////////////////////////////////////////////////////////////////////////



# 13. TASK  ///////////// Specifinių funkcijų importavimas iš folderio /////////////

from aritmetika import atimtis, dalyba

# Užduotis 13:
# 1. Importuokite iš moduliai.aritmetika tik atimtis ir dalyba.
# 2. Paskaičiuokite 50 - 25 ir 100 / 4.
# 3. Išspausdinkite rezultatus.

print(atimtis(50, -25))
print(dalyba(100, 4))
# //////////////////////////////////////////////////////////////////////////////////////

# from moduliai.ar

# 14. Modulio trumpinimas naudojant alias iš folderio
# Užduotis 14:
# 1. Importuokite moduliai.aritmetika kaip ar.
# 2. Naudokite ar.atimtis(30, 10) ir ar.dalyba(50, 5).
# 3. Išspausdinkite rezultatus.

# print(atimtis(30, 1))
# print(dalyba(50,5))
# //////////////////////////////////////////////////////////////////////////////////////

import moduliai
moduliai.aritmetika.atimtis(15, 5)

# 15. Importavimas viso folderio
# Užduotis 15:
# 1. Sukurkite __init__.py failą folderyje moduliai, kad jis būtų laikomas Python
# paketu.
# 2. Importuokite visą folderį import moduliai ir naudokite
# moduliai.aritmetika.atimtis(15, 5).
# 3. Išspausdinkite rezultatą.
print(atimtis(15,5))
# //////////////////////////////////////////////////////////////////////////////////////
