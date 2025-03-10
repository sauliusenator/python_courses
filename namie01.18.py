# darbuotojai = [
#     ['Valdas', 'programuotojas', 2000],
#     ['Adomas', 'direktorius', 3000],
#     ['Aldona', 'vadybininkas', 1800],
#     ['Jogaila', 'programuotojas', 2500]
# ]
#
# print(darbuotojai[0])  # ['Valdas', 'programuotojas', 2000]
# print(darbuotojai[0][1])  # programuotojas
# print(darbuotojai[0][1].upper())  # PROGRAMUOTOJAS
#
# # printinam po 1 vidinį pilną listą
# for listas in darbuotojai:
#     print(listas)  # ['Valdas', 'programuotojas', 2000], ..
#
# # printinam atskirus elementus iš kiekvieno vidinio listo
# # imdami per indeksą
# for listas in darbuotojai:
#     print(listas[0], listas[2])  # Valdas programuotojas, ..
#
# # python priimta yra išardyti listus for eilutėje
# for vardas, pareigos, atlyginimas in darbuotojai:
#     print(atlyginimas, vardas, pareigos)  # Valdas 2000 programuotojas, ..
#
# # susumuojam atlyginimus
# # variantas 1
# suma = 0
# for vardas, pareigos, atlyginimas in darbuotojai:
#     suma += atlyginimas
#
# print(suma)  # 9300

numb1 = 100
numb2 = 500

if numb1 < numb2:

    print(f"numb1 yra {numb1}, numb2 yra {numb2}")

    if numb1 > numb2:
        print("numb1 yra didesnis už numb2")
    else:
        print("numb1 nėra didesnis už numb2")

        if numb1 > numb2:
            print("numb1 yra didesnis už numb2")
        elif numb1 == numb2:
            print("numb1 yra lygus numb2")
        else:
            print("numb1 yra mažesnis už numb2")
