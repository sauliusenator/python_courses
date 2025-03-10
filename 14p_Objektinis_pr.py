#
# class House:
#     country = 'LT'
#
#     def __init__(self, price, year):
#         self.price = price
#         self.year = year
#
# def __str__(self):
#     print(self)
#
# house1 = House(19900, 2025)
# house2 = House(16500, 2008)
#
# house1.country = 'LV'
# house_instance_1 = House(10_000,1989)
# house_instance_2 = House(13_000,1989)
#
# print(
#     house1.country, house1.price, house1.year
# )
# print(
#     house2.country, house2.price, house2.year
# )
#
# print(house_instance_1)
# print(house_instance_2)
############################################
# from datetime import datetime
# class House:
#     country = 'LT'
#     def __init__(self, price, year):
#         self.price = price
#         self.year = year
#
#     def get_age(self):
#         return datetime.today().year - self.year
#
# house_instance_1 = House(10_000, 1990)
# age = house_instance_1.get_age()
# print(age)
#
# house_instance_1 = House(5_000_000, 2001)
# age = house_instance_1.get_age()
# print(age)
############################################
# from datetime import datetime
# 
# class House:
#     country = 'LT'
# 
#     def __init__(self, price, year):
#         self.price = price
#         self.year = year
# 
#     def __str__(self):
#         return f'Namas {self.year} pastatytas, kaina - {self.price} Eur, amžius - {self.get_age()}'
# 
#     def get_age(self):
#         return datetime.today().year - self.year
# 
# book1 = House(190_000, 2024)
# houses = [
#     House(190_000, 1980),
#     House(115_000, 1970),
#     House(90_000, 1970),
# ]
# 
# 
# for house in houses:
#     print(house)

    # print(f'Sena kaina: {house.price}')
    # house.price = round(house.price * 1.21)
    # print(f'Nauja kaina: {house.price}')
    # print('-' * 40)
    # print(house)


# assert isinstance(book1, object)
#
# print(book1)

############################################

from datetime import datetime
 
class House:
     country = 'LT'
 
     def __init__(self, price, year):
         self.price = price
         self.year = year
 
     def __str__(self):
         return f'Namas {self.year} pastatytas, kaina - {self.price} Eur, amžius - {self.get_age()}'
 
     def get_age(self):
         return datetime.today().year - self.year
 
houses_kaupiklis = []
while True:
        quit_choice = input('iveskite EXIT, kad iseiti. Spauskite Enter, kad testi')
        if quit_choice:
            break
            
        year = int(input('Iveskite metus '))
        price = int(input('Iveskite kaina '))
        
        house_instance = House(price, year)
        houses_kaupiklis.append(house_instance)
        
        print('Spausdinam ka sukaupem: ')
        for house in houses_kaupiklis:
            print(house)