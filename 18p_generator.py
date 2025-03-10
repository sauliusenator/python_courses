# def skaiciuok_iki(max_reiksme):
#     skaicius = 0
#     while skaicius < max_reiksme:
#         yield skaicius  # surneka generatorius leidzia fukcija paversti i skaiciu
#         skaicius += 1
#
# for numeris in skaiciuok_iki(5):
#     print(numeris)

employees = [x * x for x in range(10000)]
for employee in employees:
    print(employee)

def squares(lenght):
    for i in range(lenght):
        yield i * i
for square in squares(10000):
    print(square)

