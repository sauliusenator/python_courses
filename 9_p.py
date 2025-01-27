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