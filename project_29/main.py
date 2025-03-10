from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/vardusarasas')
def names_list():
    names = ['Adomas', 'Antanas', 'Valdas', 'Jonas']

    return render_template('vardai.html', names_for_template=names)


app.run()