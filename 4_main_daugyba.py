# months_str = 'sausis vasariis kovas'
# print(months_str)
#
# months_list = months_str.split(' ')
# print(months_list)
#
# # months_list2 = months_str.split('ii')
# # print(months_list2)
#
# joined_str = ', -NEREALIAI--'.join(months_list)
# print(joined_str)
#
# x_list = ['Adomas']
# print(', '.join(x_list))


# a = 'obuolys bananai kriaušės'
# b  = a.split(' ')
# print(b)
#
# join_str = '--'
# print('---'.join(b))

# OPERATORIAI

# >
# >=
# <
# <=
# ==
# !=
# is
# in

# numb1 = 100
# numb2 = 500
# numb3 = 100
#
# char = 'A'
# text = 'ABCD'
# text2 = 'QWER'
#
# name = 'John'
# names_list = ['Donald', 'Darius', 'Ona']
#
# print(
#     name in names_list
# )
#
#
# print(
#     char in text
# )
# print(
#     char in text2
# )
# print(
#     'o' in 'Project'  # Tikrina ar o yra project zodyje
# )




# a = numb1 == numb2
# print(type(a))
# print(type(a) is bool) # Yes True
# print(type(numb1) is bool) # No False

#

# print(numb1 < numb2)
# print(numb1 > numb2)
# print(numb1 == numb3)
# print(numb1 != numb3)
#
# print(numb1 >= numb3)
# print(numb1 <= numb3)

# a = 5
# b = 10
# c = 15
# d = 5.5
# e = 'operatorius naminukas ane'
# print( c > b)
# print( c < b)
# print(a % d)
# print(
#     'ane' in e
# )


# a = int(input('skaicius 1: '))
# b = int(input('skaicius 2: '))
# zodis = input("iveskite zodi: ")
# zodziai = [' labas', 'kaip', 'sekasi']
# print(a > b)
# print(a % 2 == 0)
# print(zodis in zodziai)

# numb1 = 100
# numb2 = 500
# numb3 = 300

# if numb2 > numb3 < numb1:
#     print(f'{numb1} yra mazesnis uz {numb2}')
# else:
#     print('else')
#     a = 1
#     b = 2
#     c = 3
#     num1 = numb2
#
#         if numb2 > numb3:
#             print(f'{numb1} yra mazesnis uz {numb2}')
#         else:
#             print('else')

# age = int(iput('pateikite amz: '))
# if age < 18:
#     print('Nepilnametis')
# if age >= 18:
#         print('Pilnametis: ')
#
# temperatura = int(input('pateik jusu amz: '))
# if temperatura < 0:
#         print('salta')
# if 20 <= temperatura >= 0:
#         print('Vidutinis')
# if temperatura > 20:
#         print('silta')

# numb1 = 100
# numb2 = 500
#
# if numb1 > numb2:
#     print(f'{numb1} yra didesnis uz {numb2}')
# elif numb1 == numb2:
#     print(f'{numb1} yra toks pat kaip {numb2}')
# else:
#     print(f'{numb1} yra mazesnis ir nelygus {numb2}')


# task4
# vartotojas = int(input('pateik bala: '))
# res = 'Neteisingai ivestas skaicius'
# if 0 <= balas <= 4:
#     res = 'Nepatenkinamas'
# elif 5 <= balas <= 7:
#     res = 'Vidutinias'
# elif 8 <= balas <= 10:
#     res = 'Puikus'
#
#     print(res)

# task4
# sezonas = input('Iveskite metu laika: ').strip.(lower)
# menesiai = 0
# if sezonas == 'ziema':
#     menesiai = ['gruodis', 'sausis', 'vasaris']
#     elif sezonas == 'pavasaris'
#     menesiai



numb1 = 100
numb2 = 500
numb3 = 300

if numb1 < numb2 and numb1 == 100:
    print('True')

    # 100    < 500     100   = 500
if (numb1 < numb2) or (numb1 == 500):
    print('True')

if not 100 > 500:
    print('True')

employee = ''
if numb1 > 1000:
    employee = 'Adomas'  # Reikia įtraukos čia
elif numb1 > 2000:
    employee = 'John'    # Reikia įtraukos čia
if not employee:
    print('Employee is missing. Program vill crash.')

# NEAISKI KLAIDA
# auto = 'Audi'
# autos_ger = ['BMW', 'AUDI', 'MB']
# autos_it = ['Ferrari', 'Lamborgini']
# autos_sport = ['BMW', 'Ferrari']
#
# if (auto in autos_ger or auto in autos_it) and auto in autos_sport:
#     print(f'{auto} yra vokiskas sportinis arba italiskas sportinis')

# ----------------

# skaicius = int(input('ivesk skaiciu: '))
# if (skaicius < 0):
#         print('neigiamas')
# if (skaicius > 1):
#         print('teigiamas')


# auto = int(input('iveskite automobilio marke: '))
# auto_ger = ['BMW', 'AUDI']
# auto_sport = ['M3', 'RS6']
# if ('BMW', 'AUDI'):
#     print('Vokiškas')
# if ('M3', 'RS6'):
#     print('Sportinis')



