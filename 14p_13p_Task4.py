# 7. ############################################
import datetime

a = '2023-01-01'
b = '2024-01-01'

a = datetime.datetime(2023, 1,1)
b = datetime.datetime(2024, 1, 1)
res = b - a

print(res)

# 8. ############################################

now = datetime.datetime.today()
res = now + datetime.timedelta(days=90)

print("Dabartinė data:", now)
print("Data po 90 dienų:", res)

# 9. ############################################

a = '2000-01-01'
date_a = datetime.datetime.strptime(a, '%Y-%m-%d')
b = datetime.datetime.today()

res = b - date_a

print("Dienų skaičius:", res.days)  # Dienų skaičius
print("Valandų skaičius:", res.seconds // 3600)  # Valandų skaičius
print("Bendras sekundžių skaičius:", res.total_seconds())  # Bendras sekundžių skaičius