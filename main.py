from flask import Flask, render_template, request


app = Flask(__name__)

valid_users = ['hello', 'labas', 'ate']

@app.route('/prisijungti', methods=['GET', 'POST'])
def prisijungti():
    if request.method == 'POST':
        vartotojo_vardas = request.form['vartotojo_vardas']
        return f'Prisijungėte kaip: {vartotojo_vardas}'
    return render_template('forma_post.html')


@app.route('/login', methods=['post', 'get'])
def login_user():
    if request.method == 'GET':
        return render_template('forma_post.html')
    elif request.method == 'POST':
        username = request.form.get('loginlaukelis')
        if username in valid_users:
            return render_template('login_result.html', user_login=username)
        else:
            return render_template('forma_post.html')


app.run()

