import sqlite3

conn = sqlite3.connect('sql_injection.db')

inp_username = input('Įveskite username: ')
inp_password = input('Įveskite pasword: ')

query = f'SELECT * FROM user WHERE user.username="{inp_username}" AND user.password="{inp_password}"'

with conn:

    c.execute(query)
    res = c.fetchall()
    if res:
        print('Jusu profilio nuomenys yra: ')
        print(res)
    else: print(f'Vartotojas {inp_username} negzistuoja arba neteisingas slaptazodis')

c = (conn.cursor())
print(c.fetchall())



query = '''CREATE TABLE IF NOT EXISTS user (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
username TEXT NOT NULL,
password TEXT NOT NULL,
email TEXT NOT NULL
);
'''

with conn:
    c.execute(query)

    with conn:
        c.execute('INSERT INTO user VALUES(MULL, "adomas", "123456", "adas@gmail.com")')
        c.execute('INSERT INTO user VALUES(MULL, "tomas", "654123", "tom@gmail.com")')
        c.execute('INSERT INTO user VALUES(MULL, "saulius", "123458", "saul@gmail.com")')