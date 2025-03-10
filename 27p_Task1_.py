import sqlite3

# Sukuriame ryšį su SQLite duomenų baze
conn = sqlite3.connect('example.db')
c = conn.cursor()

# 1. Sukuriame lentelę admin_users
c.execute('''
CREATE TABLE IF NOT EXISTS admin_users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT NOT NULL,
    role TEXT DEFAULT 'user'
)
''')

# 2. Įterpiame tris vartotojus
c.execute("INSERT INTO admin_users (username, password, role) VALUES ('admin', 'adminpass', 'admin')")
c.execute("INSERT INTO admin_users (username, password, role) VALUES ('user1', 'user1pass', 'user')")
c.execute("INSERT INTO admin_users (username, password, role) VALUES ('user2', 'user2pass', 'user')")

# Išsaugome pokyčius
conn.commit()


# 3. SQL užklausa prisijungimui (nenaudojant parametrizuotų užklausų)
def login(username, password):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    # SQL užklausa be parametrizuotų užklausų
    query = f"SELECT * FROM admin_users WHERE username='{username}' AND password='{password}';"
    c.execute(query)
    result = c.fetchall()

    conn.close()
    return result


# Pavyzdys, kaip prisijungti
username_input = input("Username: ")
password_input = input("Password: ")
user_data = login(username_input, password_input)

if user_data:
    print("Prisijungta sėkmingai:", user_data)
else:
    print("Neteisingas vartotojo vardas arba slaptažodis.")

# 4. SQL Injection ataka
print("\nDemonstruojame SQL injekciją:")
username_input = "admin' OR '1'='1"
password_input = "anything"
user_data = login(username_input, password_input)

if user_data:
    print("Prisijungta sėkmingai (SQL injekcija):", user_data)
else:
    print("Neteisingas vartotojo vardas arba slaptažodis.")


# 5. SQL Injection prevencija naudojant parametrizuotas užklausas
def safe_login(username, password):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    # Naudojame parametrizuotą užklausą
    query = "SELECT * FROM admin_users WHERE username=? AND password=?;"
    c.execute(query, (username, password))
    result = c.fetchall()

    conn.close()
    return result


# Pavyzdys, kaip prisijungti su saugia užklausa
username_input = input("\nSaugus prisijungimas - Username: ")
password_input = input("Saugus prisijungimas - Password: ")
user_data = safe_login(username_input, password_input)

if user_data:
    print("Prisijungta sėkmingai (saugus prisijungimas):", user_data)
else:
    print("Neteisingas vartotojo vardas arba slaptažodis.")

# Uždarykite ryšį su duomenų baze
conn.close()_