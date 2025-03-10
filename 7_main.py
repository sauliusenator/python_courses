# TASK_ mokymas
# from idlelib.autocomplete import FORCE
#
# from Tools.scripts.texi2html import goodchars
# from pkg_resources import iter_entry_points

# marke = 'Audi'
# modelis = ' A6'
# auto = {}
# print(auto)
# if marke == 'Audi':
#     auto['marke'] = marke
#     auto['modelis'] = modelis
# print(auto)
#
# auto['marke'] = 'BMW'
# auto['modelis'] = '5'
#
# auto['colors'] = ['red', 'white', 'black']
#
# car_technical_characteristics = {
#         'engine': 3.0,
#         'interior': 'leather'
#     }
# auto.update(car_technical_characteristics)
# auto.update({
#         'year': 2023,
#         'eco2000': True
#     })
# print(auto)
#
# del auto['eco2000']
# interior = auto.pop('interior')
# print(f'Interior: {interior}')
# auto['gas_engine'] = auto.pop('engine')
# auto['year'] = 2000
# auto['year'] += 5
# auto['colors'].append('yellow')
#
# print(auto)

# TASK_1 _patiems su delete

# import pprint
# store = {
#     "name": "E-Shop",
#     "categories": ["Electronics", "Books", "Clothing"],
#     "products": [
#         {"name": "Loptop", "price": 1000, "stock": 10},
#         {"name": "Book", "price": 20, "stock": 50},
#         {"name": "T-shirt", "price": 15, "stock": 100}
#     ],
#     "rating": 4.5
# }
#
# store["categories"].remove("Clothing")
# pprint.pprint(store["categories"])
#
# for product in store["products"]:
#     if product["price"] > 50:
#         product["price"] *= 0.95
#     if product["name"] == ("Loptop:"):
#         product["stock"] = 15


# for product in store["products"]:
#     if product["name"] == ("Loptop:"):
#         product["stock"] = 15
#         pprint.pprint(store["product"])

# if store["rating"] < 4.6:
#     store["rating"] += 0.1
#     pprint.pprint(store["rating"])

# store = 'goods'
# for goods in store['categories']:
#     print(f'goods: {categories["Clothing"]}')
# print('categories')


# print('goods:')
# for book in library['books']:
#     print(f'Pavadinimas: {book["title"]}, autorius: {book["author"]}')

### Sekantis ciklas ### #---------------------------#



# a = True
# while a:
#     print('123')
#     # a = False   # sustabdo cikla
#     break  # sustabdo cikla

# objektas = [1, 2, 3, 4, 5]
# for elementas in objektas:
#     if elementas == 2:
#         continue
#     print(elementas)
#
#     skaitiklis = 0
#     while skaitiklis < 5:
#
#         print(f' skaitiklis yra: {skaitiklis}')
#         print('------------')
#         skaitiklis +=1
#
#         while True:
#             user_input = input('Provide number: ')
#             if user_input != 'stop':
#                 break
#                 print(f'Your number {user_input}')
#


            #---------------------------#

# while True:
#     print('kartojimo pradzia')
#     print('1. sis meniu punktas nedaro nieko\n'
#           '2. iseiti is kartojimo bloko\n'
#           '3 vel parodyti meniu')
#     pasirinikimas = input('pasirinkimas: ')
#     if pasirinikimas == '2':
#         break
#     elif pasirinkimas == '3':
#         continue
#     else:
#         print('nieko nebuvo pasirinkta')
#         print('kartojimo pabaiga')


# total_sum = 0
# number = 1
#
# while number <= 10:
#     user_input = input(f"Įveskite skaičių {number} (arba '5', kad nutrauktumėte): ")
#
#     if user_input == '5':
#         print("Ciklas nutrauktas.")
#         break
#     try:
#         num = int(user_input)
#     except ValueError:
#         print("Prašome įvesti skaičių.")
#         continue
#     if num != 5:
#         total_sum += num
#
#     number += 1
#
# print(f"Visų įvestų skaičių suma (neskaičiuojant 5): {total_sum}")

# summ = 0
#
# while True:
#     number = int(input(' Iveskite numeri tarp 1 ir 10: '))
#     if number < 1 or number > 10:
#         print('f the number you provided is not in range from 1 to 10. Please provide correct number')
#         continue
#         if nuber == 5:
#             break
#             res += numbersprint(f' Sum of all provided numbers: {res}')

# for skaicius in range(1, 6):
#     print(f'dabartinis skaicius yra: {skaicius}')

# liskas = [1,2,3,4,5,6,7,8,9]
# flag5 = False
# Flag3 = False
# for elem in listas:
#     print(elem)
#     if elem % 5 ==0:
#         frlag5 = True
#     if elem % 3 ==0:
#         flag3 = True
#
#     if flag3 and flag5:
#         break
# if flag5:
#         print('Liste yra elementas kuris dalinasi is 5')
# if flag3:
#         print('Liste yra elementas kuris dalinasi is 3')

# listas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# minimalus = listas[0]
# print(minimalus)
# for elem in listas:
#     if elem > minimalus:
#         minimalus = elem
# print("minimalus yra: ", minimalus)

# 6 TASK

skaicius = [5, 7, 15, 6, 3, 20, 12]
for sk in skaicius:

    if sk > 10:
        print("Rastas skaičius didesnis nei 10, nutraukiame iteraciją.")
        break


    if sk % 2 == 0 or sk % 5 == 0:
        print(sk)

# 7 TASK

skaiciai = [-10, -5, 0, 5, 10, 15, 20]

teigiami_suma = 0
neigiami_suma = 0

for sk in skaiciai:
    if sk > 0:
        teigiami_suma += sk
    elif sk < 0:
        neigiami_suma += sk

print(f"Teigiamų skaičių suma: {teigiami_suma}")
print(f"Neigiamų skaičių suma: {neigiami_suma}")

didziausias = max(skaiciai)
maziausias = min(skaiciai)

print(f"Didžiausia reikšmė sąraše: {didziausias}")
print(f"Mažiausia reikšmė sąraše: {maziausias}")