from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'mokinys.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Mokiniai(db.Model):
    __tablename__ = 'mokiniai'

    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String)
    pavarde = db.Column(db.String)

    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde

    def __repr__(self):
        return f'{self.id} {self.vardas} {self.pavarde}'

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def home():
    paieska = request.args.get('paieska')
    if paieska:
        mokiniai = Mokiniai.query.filter(Mokiniai.vardas.startswith(paieska)).all()
    else:
        mokiniai = Mokiniai.query.all()
    return render_template('31p_index.html', mokiniai=mokiniai)

if __name__ == '__main__':
    app.run(debug=True)