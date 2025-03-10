# kaupiklis = []
# duomenu_listas = [1, 10, 2, 20, 3, 30, 4, 40]

# for elem in duomenu_listas:
#     kaupiklis.append(elem)

# kaupiklis = [elem for elem in duomenu_listas]
#
# print(kaupiklis)
#
# # KAUPIKLIS 3 #
# # kaupiklis3 = [elem for elem in duomenu_listas]
#
# kaupiklis3 = [elem *9 for elem in duomenu_listas] # kiekvienas elementas buvo padaugintas is 9 #
# print(kaupiklis3)
#
# kaupiklis4 = [elem ** 2 for elem in duomenu_listas] # kiekvienas elementas buvo padaugintas is 9 #
# print(kaupiklis4) # pakeltas kvadratu #
# print(duomenu_listas)

# TASK 2 #
# kaup = []
# s_listas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# kaup = [elem * 2 for elem in s_listas]
# print(kaup)
# print('------------')
#
# kaup2 = []
# s_listas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# kaup2 = [elem ** 2 for elem in s_listas]
# print(kaup2)
# print('------------')
#
# dol =  []
# a = [10, 15, 20, 25, 30]
# dol = [round(eu  ** 1.1, 1) for eu in a]
# print(dol)
# # print('------------')
# #
# zinute = [f'kaina: {eu} EUR' for eu in a]
# print(zinute)
# TASK 2 #

# dvejetaine sistema
# 0         0           0
# 1         1           1
# 2         10          2
# 3         11          3
# 4         100         4
# 5         1001        5
# 6         110         6
# 7         111         7
# 8         1000        8
# 9                     9
# 10                    A
# 11                    B
# 12                    C
# ....                  D
# 19                    E
# 20                    F
# 16                    10


# duomenu_listas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# kaupiklis5 = [[elem, elem **2] for elem in duomenu_listas]
# kaupiklis6 = [[elem, elem **2] for elem in duomenu_listas]
# print(kaupiklis5)
# print(kaupiklis6)

# products_amouts = [1, 10, 2, 20, 3, 4, 40, 99, 0, 0, 0]
# existing_products = [products_amouts for products_amouts in products_amouts if products_amouts > 0]
# print(existing_products)

# 3 TASK #


# skaiciai = [1, 2, 3, 4, 5]
# struktura = [[x, x ** 2, x **3, x % 2 == 0] for x in skaiciai]
# print(struktura)

# skaiciai = [5, 8, 12, 18, 25, 30, 35, 40]
#
# didesni_nei_20 = [x for x in skaiciai if x > 20]
#
# print("Skaičiai didesni nei 20:", didesni_nei_20)

# dalijasi_is_5 = [x for x in skaiciai if not x % 5]
# print("Skaičiai, kurie dalijasi iš 5:", dalijasi_is_5)
# lyginis_nelyginis = [f'{x}: {"Lyginis" if x % 2 == 0 else "Nelyginis"}' for x in skaiciai]
# print("Lyginis arba Nelyginis:", lyginis_nelyginis)

# RAIDES + SKAICIAI#
# raides = ['A', 'B', 'C']
# skaiciai = ['1', '2', '3', '4']
#
# ['A1', 'A2', 'A3', 'A4', 'B1']
#
# raides_su_skaiciais = [raid + sk for raid in raides for sk in skaiciai]
# raides_su_skaiciais1 = [raid + sk for raid in raides for sk in skaiciai if int(sk) % 2 ==0]
# print(raides_su_skaiciais)
# print(raides_su_skaiciais1)
# RAIDES + SKAICIAI#


# print('=================')
# listas = [0, 0, 5, 2, 3, 3, 3]


#
# tuple_res = tuple(elem for elem in listas)
# print(tuple_res) #(0, 0, 5, 2, 3, 3, 3)
#
# super_dict = {
#     'name': 'Jimm'
# }
# SET.ADD
# dict_res = {elem: elem ** 2 for elem in listas}
# print(dict_res) #{0: 0, 5: 25, 2: 4, 3: 9}
#
# set_res = {elem for elem in listas}
# set_res.add('saulius')
#
# print(set_res) #{0, 2, 3, 5}
# SET.ADD

# 5. TASK===========
# raides = ['A', 'B', 'C']
# skaiciai = [1, 2, 3]
# raid_sk = [raid + str(sk) for raid in raides for sk in skaiciai]
# print(raid_sk)





