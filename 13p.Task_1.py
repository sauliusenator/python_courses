
import datetime

res = datetime.datetime.today()

metai = res.year
menesis = res.month
diena = res.day
valanda = res.hour
minute = res.minute
sekunde = res.second

print(f"Dabar yra {valanda}:{minute}, {diena}-{menesis}-{metai}")