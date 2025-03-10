
import sqlite3

conn = sqlite3.connect('sql_injection.db')
c = conn.cursor()

inp_username = input('Username: ')
inp_password = input('Password: ')

with conn:
    c.execute('SELECT * FROM user WHERE user.username=? AND user.password=?;', (inp_username, inp_password))
    res = c.fetchall()
    if res:
        print('Jūsų profilio duomenyts yra: ')
        print(res)
    else:
        print(f"Vartotojas {inp_username} neegzistuoja arba neteisingas slaptažodis")

# - STEP 3: Get all users with sql injection
# inp_username = input('Username: ') "' OR True;--"
# inp_password = input('Password: ') ""
#
# query = f"SELECT * FROM user WHERE user.username='{inp_username}' AND user.password='{inp_password}';"
#
# with conn:
#     print("=>>>>> ", query)
#     c.execute(query)
#     res = c.fetchall()
#     print("Jūsų profilio duomenys yra:", res)

# STEP 2: Check if users created
# with conn:
#     c.execute('SELECT * FROM user;')
# print(c.fetchall())

# - STEP1: DB and table creation
# query = '''CREATE TABLE IF NOT EXISTS user (
#     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#     username TEXT NOT NULL,
#     password TEXT NOT NULL,
#     email TEXT NOT NULL
# );
# '''
#
# with conn:
#     c.execute(query)
#
# with conn:
#     c.execute('INSERT INTO user VALUES(NULL, "adomas", "123456", "adas@gmail.com")')
#     c.execute('INSERT INTO user(username, password, email) VALUES("Tomas", "Tomas123321", "t@gmail.com")')
#     c.execute('INSERT INTO user(username, password, email) VALUES("Romas", "SuperRomas321!", "romas@gmail.com")')
