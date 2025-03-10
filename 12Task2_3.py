# 3. uzduotis
#
# def dalinti_skaicius():
#     while True:
#         try:
#             ivestis1 = input('Įveskite pirmą skaičių: ')
#             ivestis2 = input('Įveskite antrą skaičių (daliklį): ')
#
#
#             skaicius1 = float(ivestis1)
#             skaicius2 = float(ivestis2)
#
#             rezultatas = skaicius1 / skaicius2
#
#             print(f'Rezultatas: {rezultatas}')
#             break
#
#         except ValueError:
#             print('Klaida: Prašome įvesti skaičių.')
#         except ZeroDivisionError:
#             print('Klaida: Dalyba iš nulio negalima. Prašome įvesti kitą skaičių.')
from sys import exec_prefix

# dalinti_skaicius()

# ////////////////////

# try:
#     res = 100 / 19
# except ZeroDivisionError:
#     print('Dalyba is 0 negalima')
# else:
#     print(f'Gerbiameas, useri stai jusu taip laukiamas rezultatas: {res}')

# //// FINALY BLOKAS ///////////////

# ivestis = input('Iveskite float skaiciu')
# try:
#     float_skaicius = float(ivestis)
#     print(f'Ivestis tinkama {float_skaicius}')
# except ValueError:
#     print('Ivestis netinkama, pakartokite.')
# else:
#     print('Jus saunuolis nes nesulauzete programos')
# finally:
#     print('Viso gero!')
# def create_user(value: dict):
#     print('User created', value)
#
# users_to_create = {
#
#     'user1': {'name': 'Darius', id: '123456789'},
#     'user2': {'name': 'Tomas', id: '123456789123456'},
#     'user3': {'name': 'Gedas', id: '123456789123456789'},
# }
# created_users = {}
# for key, value in users_to_create.items():
#     try:
#         create_user(value)
#         created_users[key] = value
#     except Exception as e:
#         print(e)
#     finally:
#         print('Already created values was saved')
# ///////////////////////////////////////////////////
# def konvertuoti_i_int():
#     while True:
#         try:
#             ivestis = input('Įveskite skaičių: ')
#             skaicius = int(ivestis)
#         except ValueError:
#             print('Klaida: Prašome įvesti galiojantį skaičių.')
#         else:
#             print(f'Konversija sėkminga: {skaicius}')
#             break
#         finally:
#             print('Programa baigė darbą.')
#
# konvertuoti_i_int()
# ////////////////////////////////////////

#
# try:
#     skaicius = int(input('Iveskite skaiciu: '))
# except ValueError:
#     print('Ivesta bloga reiksme')
# else:
#     print(f'konvensija sekminga <{skaicius}>')
# finally:
#     print('Programa baige darba')


# //////////////////
# import time
# time_limit = 3
#
# def get_password():
#    print("Please enter your password:")
#    start_time = time.time()
#    password = input("Password: ")
#    end_time = time.time()
#
#    time_taken = end_time - start_time
#    if time_taken < time_limit:
#        print("Password incorrect! Try again.")
#    else:
#        print("Password submitted successfully.")
# get_password()
# ////////////////////////

# RAISE /////////////////////////////////////////RAISE

# def susumuok_int_skaicius(sk1: int, sk2: int) -> int:
#     if not (type(sk1) is int and type(sk2) is int):
#         raise ValueError
#     return sk1 + sk2
# res = susumuok_int_skaicius(4, '5')
# print(res)

# current_user = 'Manager'
#
# employee_salaries = {
#     'Jim': 1000,
#     'Tom': 2000
# }
#
# def show_employee_salary(employee: str) -> int:
#     if current_user not in ['Admin', 'Manager']:
#         raise ValueError('You are not allowed to see employee salaries')
#     return employee_salaries[employee]
#
# print(show_employee_salary('Jim'))
# RAISE /////////////////////////////////////////RAISE

# def tikrinti_amziu(amzius):
#     if amzius < 0:
#         raise ValueError("Amžius negali būti neigiamas!")
#     elif amzius >= 18:
#         print("Vartotojas pilnametis.")
#     else:
#         print("Vartotojas nepilnametis.")
#
#
# tikrinti_amziu(15)
# tikrinti_amziu(-5)
# tikrinti_amziu(21)


def amziaus_tikrinimas(amzius):
    if amzius < 0:
        raise ValueError(f'amzius negali buti neigiamas')
    elif amzius >= 18:
        print(f'Vartotojas pilnametis')
    else:
        print('Varotojas nepilnametis')


amziaus_tikrinimas(15)
amziaus_tikrinimas(20)
amziaus_tikrinimas(-5)
