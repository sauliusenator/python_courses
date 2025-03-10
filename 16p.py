from math import degrees


########################################################
# class Gyvunas:
#     def __init__(self, vardas, spalva):
#         self.vardas = vardas
#         self.spalva = spalva
# # def begti(self):
# #     print(f"{self.vardas} {self.spalva} begu!!!")
#
# # class Kate:
# #     def miaukseti(self):
# #         print(f"{self.vardas} sako MIAU!!!")
#
# class Suo(Gyvunas):
#     def loti(self):
#
#         print(f"{self.vardas} loja!!")
# # cat = Kate('Murkis', 'Geltonas')
# # cat.begti()
#
# dog = Suo('Jim', 'Margas')
# dog.loti()
# # cat = Kate('Lora')
# # Kate.miaukseti()
########################################################

class Stack:
    def __init__(self):
        self.data = []

    def push(self, elem):
        self.data.append(elem)

    def pop(self):
        return self.data.pop()

class Element:
    def __init__(self, item1, item2):
        self.item1 = item1
        self.item2 = item2

    def __str__(self):
        return f"{self.item1} {self.item2}"

elems = [
    Element(1,2),
    Element(3,4),
    Element(5,6)
]

stck = Stack()

for i in elems:
    stck.push(i)

a = stck.pop()

for i in stck.data:
    print(i)
print('-' * 11)
print(a)

