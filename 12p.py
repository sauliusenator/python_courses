produktai = '4'
produktu_skaicius = 0

try:
    produktas = int(produktai)
    res = produktas / produktu_skaicius
except:
    print('Mes crashinom, taciau suvaldem crasha')

# -----------------------------------------------------------------------
# 1 uzduotis    ---------------------------------------------------------
# -----------------------------------------------------------------------
# def dalinti(a, b):
#     try: return a / b
#     except: "dalyba is nulio negalima"
# print(dalinti(10, 2), dalinti(5, 0), dalinti(8, 4))

# dest :
def dalinti(a: (int, float), b: (int, float)) -> (float, str):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Dalyba iš nulio negalima'

# Iškviečiame funkciją ir atspausdiname rezultatą
print(dalinti(10, 2))

while True:
    ivestis1 = input('Įveskite sveiką skaičių: ')
    ivestis2 = input('Įveskite daliklį: ')

    try:
        skaicius = int(ivestis1)  # Pataisyta: čia buvo klaida su '-'
        daliklis = int(ivestis2)
        res = dalinti(skaicius, daliklis)  # Naudojame funkciją dalinti
        print(f'Rezultatas: {res}')
    except ValueError:
        print('Įvestas netinkamas skaičius. Bandykite dar kartą.')
        break


