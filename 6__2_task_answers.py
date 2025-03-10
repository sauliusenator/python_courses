#
# # 1
# mokykla = {
#     'pavadinimas': 'Vilniaus gimnazija',
#     'mokytojai': [
#         {'vardas': 'Jonas', 'pavarde': 'Petrauskas', 'mokomas_dalykas': 'Matematika'},
#         {'vardas': 'Asta', 'pavarde': 'Kazlauskienė', 'mokomas_dalykas': 'Lietuvių kalba'},
#         {'vardas': 'Tomas', 'pavarde': 'Stankevičius', 'mokomas_dalykas': 'Fizika'}
#     ],
#     'mokinių_skaičius': 550
# }
#
# pirmas_mokytojas = mokykla['mokytojai'][0]
# print(f'Pirmas mokytojas: {pirmas_mokytojas["vardas"]}, mokomas dalykas: {pirmas_mokytojas["mokomas_dalykas"]}')
#
# if mokykla['mokinių_skaičius'] > 500:
#     print('Mokykloje yra daugiau nei 500 mokinių.')
# else:
#     print('Mokykloje yra 500 arba mažiau mokinių.')
#
# # 2
# company = {
#     'name': 'TechCorp',
#     'employees': [
#         {'name': 'Jonas', 'role': 'Developer', 'salary': 3000},
#         {'name': 'Asta', 'role': 'Designer', 'salary': 2500},
#         {'name': 'Tomas', 'role': 'Manager', 'salary': 4000}
#     ],
#     'location': 'Vilnius',
#     'industry': 'IT'
# }
#
# print('Darbuotojai ir jų pareigos:')
# for employee in company['employees']:
#     print(f'{employee["name"]} - {employee["role"]}')
#
# salaries = [employee['salary'] for employee in company['employees']]
# average_salary = round(sum(salaries) / len(salaries), 2)
# print(f'Darbuotojų atlyginimų vidurkis: {average_salary:.2f} EUR')
#
# if 'location' in company:
#     print(f'Įmonės vieta: {company["location"]}')
# if company.get('location'):
#     print(f'Įmonės vieta: {company["location"]}')
# if company['location']:
#     print(f'Įmonės vieta: {company["location"]}')
#
# # 3
# library = {
#     'books': [
#         {'title': '1984', 'author': 'George Orwell', 'copies': 3},
#         {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'copies': 5},
#         {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'copies': 2}
#     ],
#     'location': 'Kaunas',
#     'open_hours': {'start': '8:00', 'end': '20:00'}
# }
#
# print('Knygų sąrašas:')
# for book in library['books']:
#     print(f'Pavadinimas: {book["title"]}, autorius: {book["author"]}')
#
# min_copies_book = library['books'][0]
# for book in library['books']:
#     if book['copies'] < min_copies_book['copies']:
#         min_copies_book = book
# print(f'Knyga su mažiausiai kopijų: {min_copies_book["title"]}')
