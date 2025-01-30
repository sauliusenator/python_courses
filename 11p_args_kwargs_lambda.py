import c1

# ARGS NAUDOJAMA SU KITAIS KINTAMAISIAIS

# def print_args(*args):
#     print(args)
#     print(type(args))
#
# print_args('Adomas', 'sausis', 1000)
#----------------------------------------------------------------------------

# def give_hello_to_names(*args): # SVARBI ZVAIGZDUTE KARTU SU ARGS pavadinimu
#     res = ' '
#     for name in args:
#         res += f'Hello, {name}!\n' # \n REISKIA KAIP ENTER ZEMYN PO KIEKVIENO ZODZIO
#     return res
#
# # name = ('Ram', 'Adomas', 'Valdas', 'Darius', 'Tomas', 'etc')
# print(give_hello_to_names('Ram', 'Adomas', 'Valdas', 'Darius', 'Tomas', 'etc'))

#----------------------------------------------------------------------------
# def multiply_all_by_numb(numb,*args):
#     for elem in args:
#         print(numb * elem)

# multiply_all_by_numb(1, 2, 3, 4, 5)

# #----------------------------------------------------------------------------
# def take_order(customer_name, *args):
#     """
#     Takes a restaurant order with multiple food items.
#
#     :param customer_name: str
#     :param args: food items
#     :return: None
#     """
#
#     print(f'Order for {customer_name}')
#     for item in args:    # Klaida 1: buvo 'for i in range args'
#         print(f' - {item}')
#     print('Thank you for your order!')  # Klaida 2: buvo netinkamas įtraukimas
#
# take_order('Darius', 'Pizza', 'Burger', 'Milk shake')  # Klaida 3: 'snake' -> 'shake'

#----------------------------------------------------------------------------
#-------------*args naudojimas funkcijose -----------------------------------
# 1 Uzduotis
# Parašykite funkciją sudeti_skaicius(), kuri priimtų neribotą kiekį skaičių kaip
# argumentus ir grąžintų jų sumą.
# 1. Iškvieskite funkciją su (5, 10, 15).
# 2. Iškvieskite funkciją su (100, 200, 300, 400).

# def sudeti_skaicius(*args):
#     return sum(args)
# print(sudeti_skaicius(5, 10, 15))
# print(sudeti_skaicius(100, 200, 300, 400))


#-------------*Funkcija su daugybe vardų  -----------------------------------
# 2 Uzduotis
# Parašykite funkciją sveikinti_vardus(*args), kuri priimtų kelis vardus ir grąžintų žinutę
# su pasisveikinimu kiekvienam vardui.
# Pvz.: sveikinti_vardus("Jonas", "Asta", "Mantas")
# def sveikinti_vardus(*args):
#     res = ''
#     for i in args:
#         res += f'Labas, {i}!\n'
#     return  res
# print(sveikinti_vardus('Jim', 'Tom', 'Jerry'))

#-------------Argumentų derinimas su *args  -----------------------------------
# 3 Uzduotis
# Parašykite funkciją pakelti_laipsniu(n, *args), kuri priimtų
# pagrindinį skaičių n ir keletą kitų skaičių, kuriuos reikia pakelti n
# laipsniu.

# def pakelti_laipsniu(n, *args):
#     return [i ** n for i in args]
#
#     print(i ** n for i in args)

# def multiply_all_by_numb(numb: int, *args, text='* daugyba'):
#     for elem in args:
#         print(f'{numb * elem}')
#----------------------------------------------------------------------------------------------------------------------------
# def return_list_of_multiplied_numbs(numb, *args, info=False): # pirma sk paskui *args, ir pask, default dalis
#     multiplied_numbs = [elem * numb for elem in args]
#     if info:
#         print(f'daugiklis: {numb}, args: {args}, rezultatas: {multiplied_numbs}')
#     return multiplied_numbs
#
# res = return_list_of_multiplied_numbs(7, 10, 11, 50)
# print(res)
#
# res = return_list_of_multiplied_numbs(7, 10, 11, 50, info=True)
# print(res)

#----------------------------------------------------------------------------
#-------------Kelių argumentų tipų derinimas  -----------------------------------
# 4 Uzduotis
# Sukurkite funkciją spausdinti_zinutes(kartai, *args, pabaiga="!"), kuri
# pakartotų kiekvieną perduotą žinutę kartai kartų, o pabaigoje pridėtų pabaiga reikšmę.

# def spausdinti_zinutes(kartai, *args, pabaiga="!"):
#
#     spausdinti_zinutes = [kartai for elem in args]
#     if info:
#         print(f'zinutes: {kartai}, args: {args}, res: {pabaiga}')
#     return *args
#
# print(spausdinti_zinutes(*args))

# def spausdinti_zinutes(kartai, *args, pabaiga="!"):
#     [print(f"{zinute}{pabaiga}") * kartai for zinute in args]
#
# # Testavimas
# spausdinti_zinutes(2, "Labas", "Viso")


# def spausdinti_zinutes(kartai: int, *args: str, pabaiga: str="!") -> None:
#     for zinute in args:
#         print((zinute + ' ') * kartai + pabaiga)
#
# print(spausdinti_zinutes(2, 'Labas', pabaiga='Viso gero'))

#--------------------------------------------------------------
# 5 Užduotis

# def dauginti_skaicius(n: int, *args: int) -> list:
#     return [skaicius * n for skaicius in args]
#
# rezultatas = dauginti_skaicius(2,1,3,5,7)
# print(rezultatas)
# #--------------------------------------------------------------
# def check_type_of_args(*args: (int, float, str)):
#     for arg in args:
#         print(type(arg))
#
# check_type_of_args(1, '2', 34, '58', 99.99)

#--------------------------------------------------------------
#-------------------------KWARGS-------------------------------------
# **kwargs yra Python mechanizmas,
# kuris leidžia funkcijai priimti neribotą kiekį vardinių argumentų
# (keyword arguments).
#--------------------------------------------------------------

# def print_kwargs(**kwargs):
#     print(kwargs['pirmas'])
#     print(type(kwargs))
#
# print_kwargs(pirmas=1, antras=2)

# def print_list(listas, skirtukas= '', eilutes_pabaiga='\n'):
#     for elem in listas:
#         print(elem, 'men.', sep=skirtukas, end=eilutes_pabaiga)

# def print_listas(listas, skirtukas=' ', eilutes_pabaiga='\n'):
#     for elem in listas:
#         print(elem, end=skirtukas)
#     print(eilutes_pabaiga)
#
# listas_duom = ['sausis', 'vasaris', 'kovas']
# print_listas(listas_duom)
# print_listas(listas_duom, skirtukas='|||', eilutes_pabaiga='***\n')
#
# print(listas_duom)
#
#
# def print_kwargs(**kwargs):
#     for elem in listas:
#         print(elem, 'men.', **kwargs)
#
# print_list(listas_duom, sep='>>>')
# print_list(listas_duom, sep='>>>', end='---')
#
# def print_kwargs(**kwargs):
#    for elem in listas_duom:  # Klaida 1: listas neapibrėžtas, naudojame listas_duom
#        print(elem, 'men.', **kwargs)
#
#
# listas_duom = ['sausis', 'vasaris', 'kovas']

#
# print_kwargs(sep='>>>')
# print_kwargs(sep='>>>', end='---')

# def spausdinti_info(**kwargs):
#     if 'vardas' in kwargs:
#         print(f"Vardas: {kwargs['vardas']}")
#     if 'amzius' in kwargs:
#         print(f"Amžius: {kwargs['amzius']}")
#
# # Galime kviesti su skirtingu argumentų kiekiu:
# spausdinti_info(vardas="Ona")
# spausdinti_info(vardas="Jonas", amzius=30)
# spausdinti_info(vardas="Petras", amzius=25, miestas="Kaunas")

#---------------Įvadas į **kwargs -----------------------------------------------
# 6 Užduotis
# def rodyti_duomenis(**kwargs):
#     for raktas, reiksme in kwargs.items():
#         print(f"{raktas}: {reiksme}")
#
# rodyti_duomenis(vardas="Jonas", amzius=30, miestas="Vilnius")

#-------------**kwargs su numatytaisiais argumentais -------------------------------------------------
# 7 Užduotis
# Sukurkite funkciją registruoti_naudotoja(vardas, el_pastas, **kwargs), kuri
# priimtų vardą, el. paštą ir papildomus pasirinktinus duomenis.

# def registruoti_naudotoja(vardas, el_pastas, **kwargs):
#     print(f"Vardas: {vardas}")
#     print(f"El. paštas: {el_pastas}")
#     if kwargs:
#         print("Papildomi duomenys:")
#         for raktas, reiksme in kwargs.items():
#             print(f"{raktas}: {reiksme}")
#     else:
#         print("Papildomų duomenų nėra.")
# registruoti_naudotoja("Jonas", "jonas@example.com", amzius=30, miestas="Vilnius")

#-------------**kwargs naudojimas kitoje funkcijoje -------------------------------------------------
# 8 Užduotis
# Sukurkite funkciją atspausdinti_lista(listas, **kwargs), kuri perduoda **kwargs
# į print(), leisdama valdyti formatavimą.

# def atspausdinti_lista(listas, **kwargs):
#     print(*listas, **kwargs)
# sarasas = ["Pirmas", "Antras", "Trečias"]
# atspausdinti_lista(sarasas)
# atspausdinti_lista(sarasas, sep=" | ", end=".\n")

#----------------------------------------------------------

# def kelk_laipsniu(sk, laipsnis=2, **kwargs):
#     res = sk ** laipsnis
#     return res
# print(kelk_laipsniu(2, laipsnis=3, radianas=2))
#
#
# def call_kelk_laipsniu(sk, **kwargs):
#     return kelk_laipsniu(sk, **kwargs)
#
#
# print(kelk_laipsniu(2, laipsnis=3, radianas=2))

#----------------------------------------------------------
#------------------------LAMBDA-ARGUMENTAI-Naudojama smulkiems skaiciavimamas--------------------------------
#----------------------------------------------------------
# def grazink_index_1(listas):
#     return listas[1]

# darbuotojai = [
#     ['Valdas', 'programuotojas', 2000],
#     ['Adomas', 'direktorius', 3000],
#     ['Aldona', 'vadybininkas', 1800],
#     ['Jogaila', 'programuotojas', 2500],
# ]
# aaa = grazink_index_1
# print(aaa(darbuotojai))
# res = sorted(darbuotojai, key=lambda l: l[1])
# print(res)
##----------------------------------------------------------
# def sudeti(a, b):
#     return  a + b
# print(sudeti(3, 5))
#
# sudeti_lamba = lambda a, b: a + b
# print(sudeti_lamba(3, 15 ))
##----------------------------------------------------------

# skaiciai = [1,2,3,4,5,6,7,8,9,10]
#
# lyginiai_skaiciai = list(filter(lambda x: x % 2 == 0, skaiciai))
# print(lyginiai_skaiciai)

##----------------------------------------------------------
##----------------------------------------------------------
# 11. Įvadas į lambda funkcijas
# Užduotis 11:
# Sukurkite lambda funkciją pakelti_kvadratu, kuri priima vieną skaičių ir grąžina jo
# kvadratą.

# skaiciai = [2,4]
# kvadratu = lambda x: x **2
# print(kvadratu(9))

##----------------------------------------------------------
# 12. Lambda funkcijos ir rūšiavimas
# Užduotis 12:

darbuotojai = [("Jonas", 2500), ("Asta", 3200), ("Mantas", 2100)]
# sort_darbuotojai = sorted(darbuotojai, key=lambda x: x[1])  //// sis irgi geras sprendimas
# print(sort_darbuotojai)
res = sorted(darbuotojai, key = lambda l:l[1],)
print(res)

##----------------------------------------------------------
# 13. Lambda funkcija su filter()
# Užduotis 14:

# Turite sąrašą [5, 10, 15, 20, 25, 30]. Naudodami filter() ir lambda funkciją,
# palikite tik skaičius, kurie dalijasi iš 10.

sk = [5, 10, 15, 20, 25, 30]
dalijasi_is_10 = list(filter(lambda x: x % 10 ==0, sk))
print(dalijasi_is_10)
