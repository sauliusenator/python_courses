from flask import Flask

app = Flask(__name__)

@app.route('/pagrindinis')
def pagrindinis():
    return '''
    <!doctype html>
    <html lang="lt">
    <head>
        <meta charset="utf-8">
        <title>Mano Flask puslapis</title>
    </head>
    <body>
        <h1>Mano Flask puslapis</h1>
        <p>Tai yra pagrindinis puslapis.</p>
        <a href="/apie">Nuoroda į apie puslapį</a><br>
        <a href="/vartotojas/John">Nuoroda į vartotojo puslapį (pavyzdys: John)</a><br>
        <a href="/skaicius/5">Nuoroda į skaičiaus puslapį (pavyzdys: 5)</a>
    </body>
    </html>
    '''

@app.route('/apie')
def apie():
    return '''
    <!doctype html>
    <html lang="lt">
    <head>
        <meta charset="utf-8">
        <title>Apie puslapį</title>
    </head>
    <body>
        <h1>Apie puslapį</h1>
        <p>Čia galite rasti informaciją apie mūsų Flask programą.</p>
        <a href="/pagrindinis">Grįžti į pagrindinį puslapį</a><br>
        <a href="/vartotojas/John">Nuoroda į vartotojo puslapį (pavyzdys: John)</a><br>
        <a href="/skaicius/5">Nuoroda į skaičiaus puslapį (pavyzdys: 5)</a>
    </body>
    </html>
    '''

@app.route('/vart/<vardas>')
def vartotojas(vardas):
    return f'Jūs esate vartotojas: {vardas}'

@app.route('/sk/<int:nr>')
def skaicius(nr):
    return f'Jūs įvedėte skaičių: {nr}'

if __name__ == '__main__':
    app.run(debug=True)