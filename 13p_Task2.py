
################################
#2. #
import datetime

res = datetime.datetime(1995,7,14,15,30)

liepos_15 = datetime.datetime(1995,7,14,15,30)
print(liepos_15)
dt_without_time = datetime.datetime(2023,1,1)
print(dt_without_time)
print(res)
res = datetime.datetime(2023, 1, 1)
metai = res.year
menesis = res.month
diena = res.day
# print(res)
# print(f"{metai}-{menesis}-{diena}")

################################
#3. #
time_from_2000 = datetime.datetime.today() - datetime.datetime(2000,1,1)
print(time_from_2000)


