# x = 1.125
#
# res = round(x, 2)
#
# print(res)

#  - - -- - - - lietuviskos raides sortinimas - - - - - - -import localelocale.setlocale(locale.LC_ALL, 'lt_LT')list_lt = ['Žemė', 'Ąžuolas', 'Vilnius']res = sorted(list_lt, key=locale.strxfrm)print(res)

# x = ['1.234', '3.14159', '2.71282', '0.57721']
# print(sorted)
# res = round(x, 2)
#
# print(res)

# 1
# x = [1.234, 3.14159, 2.71828, 0.57721]
# for numb in x:
#     numb= round(numb,3)
#     print(numb)
#
# # 2
# import locale
# locale.setlocale(locale.LC_ALL, 'lt_LT')
# list_lt = ["Žalgiris", "Ąžuolas", "Lietuva", "Vilnius"]
# res = sorted(list_lt, key=locale.strxfrm)
# print(res)
#
# # 3
# y = [10, 3, 7, 1, 15]
# result = sorted(y)
# print(result)

# x = [1.234, 3.14159, 2.71828, 0.57721]
# apvalinti_x = []
# for x in x:
#     apvalinti_x.append(round(x, 3))
#     print(apvalinti_x)

# print(', '.join([str(round(x, 3)) for x in x ]))

# person_info = {
#     'name' :  'Albert',
#     'surname': 'Einstein',
#     'language': {
#         'German': {
#             'level': '100',
#             'sound': '100',
#         },
#
#
#         # ' Latin', 'Italian', 'English'],
#
#     'ocupation': {
#         'role': 'Profession',
#         'workplace': ' University of Berlin',
#         'students': {
#             'student1':  {
#                 'name': 'Saulius'
#                     }
#             }
#     }
# }
# }
# print(person_info)
# print(type(person_info))
# # print(person_info['Profession'])

# print(
#     person_info['ocupation'], ['role'], ['workplace'], ['studen1']
# )
#
# mokykla = {
#     'name': 'Gimnazija',
#     'mokytojas': {
#         'mokytojai1': {
#         'vardas': 'Petras',
#         'pavarde': 'Petrulis',
#         'dalykas': 'biologija',
#         }
#     },
# 'moksleiviu_nr': 100
# }
# #
#
# print(mokykla[f"Mokytojas name is {mokykla['mokytojas']['mokytojai']['vardas']}")

#
# mokykla = {
#     'name': 'Gimnazija',
#     'mokytojas': {
#         'mokytojai1': {
#             'vardas': 'Petras',
#             'pavarde': 'Petrulis',
#             'dalykas': 'biologija',
#         },
#         'mokytojai2': {
#             'vardas': 'Tomas',
#             'pavarde': 'Tomukas',
#             'dalykas': 'fiziakas',
#         }
#     },
#     'moksleiviu_nr': 100
# }
#
# # Teisingas būdas pasiekti mokytojo vardą:
# print(f"Mokytojas name is {mokykla['mokytojas']['mokytojai1']['vardas']}")
# print(mokykla['moksleiviu_nr'])
# print(f"Mokytojas name is {mokykla['mokytojas']['mokytojai2']['vardas']} ir jo dalykas yra {mokykla['mokytojas']['mokytojai2']['dalykas']}")
# if mokykla['moksleiviu_nr'] > 101:
#     print('Daugiau už 120 moksleiviu')
# else:print('Maziau nei 100 moksleiviu')


company = { "name": "TechCorp", "employees":
    [ {"name": "Jonas", "role": "Developer","salary": 3000},
      {"name": "Asta", "role": "Designer", "salary": 2500},
      {"name": "Tomas","role": "Manager", "salary": 4000} ],
            "location": "Vilnius", "industry": "IT" }

print(f"Company name: {company['name']}")
print(f"Company name: {company['name']}, Employee name: {company['employees'][0]['name']}")

total_salary = 0
for employee in company['employees']:
    total_salary += employee['salary']

average_salary = total_salary / len(company['employees'])
print(f"Vidutinis atlyginimas: {average_salary}")

average_salary = sum(emp['salary'] for emp in company['employees']) / len(company['employees'])
print(f"Vidutinis atlyginimas: {average_salary}")


if 'location' in company:
   print(f"Company address {company['location']}")
else:
   print("Location place is not")


location = company.get('location', 'Location place is not"')
print(f"Company address: {location}")

print(f'Darbuotojų atlyginimų vidurkis: {average_salary:.2f} EUR')

# 3 TASK

library = {
    "books": [
        {"title": "1984", "author": "George Orwell", "copies": 3},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "copies": 5},
        {"title": "The Great Gatsby", "author": "F.Scott Fitzgerald", "copies": 2}
    ],
    "location": "Kaunas", "open_hours": {"start": "8:00", "end":  "20:00"} }

print('Knyg sarasas: ')
for book in library['books']:
    print(f'Pavadinimas: {book["title"]}, autorius: {book["author"]}')

min_copies_book = library['books'][0]
for book in library['books']:
    if book['copies'] < min_copies_book['copies']:
        min_copies_book = book
print(f'Knyga su mažiausiai kopijų: {min_copies_book["title"]}')

