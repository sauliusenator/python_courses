# def sveikink():
#     print('ssveikink')
# for i in range(3):
#     sveikink()


# name = 'Saulius'
# def create_greetings(user):
#     if not user:
#         return
#     res = f'Greetings,{user}!'
#     return res
#
# greetings = create_greetings(name)
# if greetings:
#     print(greetings)
# else:
#     print('user not found')
#
# def daugyba(x, y):
#     if isinstance(x, (int, float)) and isinstance(y, (int, float)):
#         return x * y
#     else:
#         return None  # Grąžiname None, jei x arba y nėra skaičius
#
# res = daugyba(5, 10)
#
# if res is not None:
#     print(res)
# else:
#     print('Numbers are wrong or not provided.')


# def greet(name='Jimm'):
#     print(f'Hello, {name}!')
#
# greet('Saulius')
# greet()

# def priimk_pasienta(pacientas, gydytojas='gyd. Pagalnutylenis'):
#     irasas_gyd_zurnale = f'Pacientas {pacientas}, prieme {gydytojas}'
#     return irasas_gyd_zurnale
#
# res = priimk_pasienta('Adomas')
# print(res)
#
# res = priimk_pasienta('Rolandas')
# print(res)
#
# res = priimk_pasienta(
#         gydytojas='gyd. Pakeitenis',
#         pacientas='Adomas',
# )
# print(res)

# def trys_sveikinimai(vardas1, vardas2, vardas3):
#     print(f'Labas, {vardas1}!')
#     print(f'Labas, {vardas2}!')
#     print(f'Labas, {vardas3}!')
# trys_sveikinimai('Jonas', 'Asta', 'Mantas')
#
# def trys(name1, name2):
#     print(f'Hello, {name1}!')
#     print(f'Hellou, {name2}!')
# trys('Kestas', 'Mantas')


# a = ('123', '321')
# print(a)

# def sveikink_su_pavadinimu(vardas, pavadinimas="drauge"):
#     print(f'Sveikas, {vardas}! Ką veiki, {pavadinimas}?')
#
# sveikink_su_pavadinimu('Jonas')
# sveikink_su_pavadinimu('Asta', 'kolega')

# Klaida: negalima dalyti iš nulio.
# def dalink_spec(sk1, sk2, iki_sveiko_sk=False):
#     if not iki_sveiko_sk:
#         return sk1 / sk2
#     return sk1 // sk2
#  nesigauna nieko

# def dalink_spec(sk1, sk2, iki_sveiko_sk=False):
#     if sk2 == 0:
#         return "Klaida: negalima dalyti iš nulio."
#
#     if not iki_sveiko_sk:
#         return sk1 / sk2
#     return sk1 // sk2
# # Klaida: negalima dalyti iš nulio.
#
#
# # Pavyzdžiai
# print(dalink_spec(10, 2))  # 5.0
# print(dalink_spec(10, 2, True))  # 5
# print(dalink_spec(10, 0))  # Klaida: negalima dalyti iš nulio.

# say_hello('Jerry')

# print()


# def add(x: int,  y: int) -> int:
#     return x + y
#
# a = 1 + add(1, 3)

# ----------------------------------------------------------
# 5. TASK
# Užduotis 5:
# Sukurkite funkciją skaiciuoti_sumos_tipą(x, y, tik_teigiama=False), kuri
# priimtų du skaičius ir grąžintų jų sumą.
# • Jei tik_teigiama=True, funkcija grąžintų tik teigiamą sumą (jei suma neigiama,
# grąžintų 0).
# Docstringai funkcijose

# def skaiciuoti_sumos_tipą(x, y, tik_teigiama=True):
#     res =  x + y
#     if not tik_teigiama:
#         return  res
#     if res < 0:
#         return 0
#     return res
# print(skaiciuoti_sumos_tipą(15, 17, False))


# def skaiciuoti_sumos_tipa(x: int, y: int, tik_teigiama: bool=False) -> int:
#     suma = x + y
#     if tik_teigiama:
#         return max(suma, 0)
#     return suma
#
# print(skaiciuoti_sumos_tipa(5, 3))
# print(skaiciuoti_sumos_tipa(5, -30, True))

# ----------------------------------------------------------

# 6 TASK -----------------------------------------

# def skaiciuoti_sumos_tipa(x: int, y: int, tik_teigiama: bool=False) -> int:
#     suma = x + y
#     if tik_teigiama:
#         return max(suma, 0)
#     return suma

# print(skaiciuoti_sumos_tipa(5, 3))
# print(skaiciuoti_sumos_tipa(5, -30, True))
#
# def apskaiciuok_vidurki(skaiciai: list) -> float:
#     if not skaiciai:
#         return 0
#     return sum(skaiciai) / len(skaiciai)
#
# print(apskaiciuok_vidurki([1, 2, 3, 4, 5]))
#
# # Užduotis 7: -------------------------------------
# # Sukurkite funkciją prideti_zodi(tekstas: str, zodis: str) -> str, kuri priimtų
# # sakinį ir pridedamą žodį, o tada grąžintų sakinį su tuo žodžiu gale.
#
# def prieti_zodi(tektas: str, zodis: str) -> str:
#
#     return tektas + " " + zodis
# print()

# ///////// 2025-01-28  /////////////

def dalink(x: int, y: int) -> float:
    return  x / y

def daugink(x: int, y: int) -> int:
    return  x * y

def atimk(x: int, y: int) -> int:
    return  x - y

def pridek(x: int, y: int) -> int:
    return  x + y