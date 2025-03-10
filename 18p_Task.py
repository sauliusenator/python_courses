
# 4. is 17 pamokos
class Matematika:
    @staticmethod
    def sudeti(a, b):
        return a + b

    @staticmethod
    def atimti(a, b):
        return a - b

    @staticmethod
    def dauginti(a, b):
        return a * b

    @staticmethod
    def dalinti(a, b):
        if b == 0:
            raise ValueError("Negalima dalinti iš nulio!")
        return a / b

# Pavyzdys, kaip naudoti klasę
a = 10
b = 5

print("Suma:", Matematika.sudeti(a, b))
print("Skirtumas:", Matematika.atimti(a, b))
print("Sandauga:", Matematika.dauginti(a, b))
print("Dalmuo:", Matematika.dalinti(a, b))

try:
    print("Dalmuo:", Matematika.dalinti(a, 0))
except ValueError as e:
    print(e)

# 5. is 17 pamokos



class matematika:
    @staticmethod
    def add(a, b):
        suma = a + b
        sandauga = a * b
        skirtumas = a - b
        dalinti = (a / b) >= 1 if b != 0 else False
        return suma, sandauga, skirtumas, int(dalinti)


rezultatai = matematika.add(5, 30)
print("Suma:", rezultatai[0])
print("Sandauga:", rezultatai[1])
print("Skirtumas:", rezultatai[2])
print("Ar a/b >= 1:", rezultatai[3])