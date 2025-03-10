from flask import Flask

app = Flask(__name__)
@app.route('/')

def home():
    return "<h1>Home page</h1>"

if __name__ == '__main__':
    app.run()












# class Darbuotojas:
#     def __int__(self, vardas, pavarde, pareigos):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pareigos = pareigos
#
#     def change_employee_name(self, vardas):
#         if not vardas:
#             raise ValueError('Name is not provided')
#         self.vardas = vardas
#
#     @staticmethod
#     def divide(a, b):
#         if a == 0:
#             raise ZeroDivisionError('Can not devide by zero')
#         return a / b
#
#     @classmethod
#     def super_constructor(cls, vardas, pavarde, pareigos):
#         return cls(vardas, pavarde, pareigos)
#
#     @property
#     def atlyginimas(self):
#         return self.__atlyginimas

    #------------------------------------------

def registratorius(funkcija):
    print(f' funkcija: {funkcija}')
    def apvalkalas(argumentas):
        print(f'argumentas: {argumentas}')
        rezultatas = funkcija(argumentas)
        if rezultatas % 2 == 0:
            print(f'{rezultatas} yra lyginis')
        else:
            print(f'{rezultatas} yra nelyginis')
        return rezultatas
    return apvalkalas

@registratorius
def kvadratu(skaicius):
    return skaicius ** 2
print(kvadratu(8))


def top_level_delay(seconds):
    def returner_of_delayed_func(func):
        def wrapper(*args, **kwargs):
            print(f'Funkcijos darbas prasides po: {seconds}')
            time.sleep(seconds)
            res = func(*args, *kwargs)
            return res
        return wrapper
    return returner_of_delayed_func

@top_level_delay(9)
def grazink500():
    return 500

@top_level_delay(15)
def vykdyk_aritmetika(skaicius1, skaicius2, veiksmas=None):
    if veiksmas == 'atimtis':
        return skaicius1 - skaicius2

res = grazink500()
print(res)

res = vykdyk_aritmetika(100, 1, )