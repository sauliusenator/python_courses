# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return "Sveiki atvykę į Flask aplikaciją!"
#
# @app.route('/apie')
# def about():
#     return "Tai yra apie mus puslapis."
#
# @app.route('/vartotojas/<vardas>')
# def user(vardas):
#     return f"Sveiki, {vardas}!"
#
# @app.route('/skaicius/<int:nr>')
# def number(nr):
#     return f"Jūs įvedėte skaičių: {nr}"
#
# @app.route('/kelione/<start>/<end>')
# def journey(start, end):
#     return f"Kelionės maršrutas: iš {start} į {end}"
#
#
# app.run()
