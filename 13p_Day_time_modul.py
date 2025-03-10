# import datetime

# import datetime

#############################################
# kreipiames i funkc aprasyta datetime faile
# todel kode 2 kartus kartojam datetime
#  antrasis datetime yra kreipimasis i klase
#  .today() metodas sukuria sio laiko momento datos-laiko objekta
#  rezultatas yra daterime.datetime objektas
#############################################

# from datetime import datetime
# # print(type(datetime.datetime))
#
# # dt_res = datetime.datetime.today()
#
# print(datetime)
# print(datetime.today)
# dt_res = datetime.today()
# print(dt_res)

#############################################

# import datetime
# print(f'Start = {datetime.datetime.today()}')
#
# dt_res = datetime.datetime.today()
# print(dt_res)
# print(dt_res.year)
# print(dt_res.month)
# for i in range(1, 1000000):
#     a = 123
# print(dt_res.day)
# print(dt_res.hour)
# print(dt_res.minute)
# print(dt_res.second)
# print(dt_res.microsecond)
# print(f'End - {datetime.datetime.today()}')
#############################################
# import datetime
#
# my_datetime = datetime.datetime(2011, 12, 31, 23, 59)
# today_dt = datetime.datetime.today()
#
# print(my_datetime)
#
# if my_datetime < today_dt:
#     print("yes")

# my_datetime = datetime.datetime(2011,12,31,23,59)
# print(my_datetime)
# my_datetime = datetime.datetime(2011) ###### NEGALIMA TOKIO KURTI
# print(my_datetime) ###### NEGALIMA TOKIO KURTI
#############################################
# def is_save_still_valid(start_dt, end_dt) -> bool:
#     today_dt = datetime.datetime.today()
#     if start_dt < today_dt < end_dt:
#         return True
#     return False
# sales_start_dt = datetime.datetime(2025, 2, 2)
# sales_end_dt = datetime.datetime(2025, 4, 2)
#
# print(is_save_still_valid(sales_start_dt, sales_end_dt))
# if not is_save_still_valid:
#     raise ValueError('Sale is over!')
# print('Thank for buying')
#############################################

# last_payment_dt = datetime.datetime(2000, 1,1)
# time_today = datetime.datetime.today()
# days_last_payment = true_today - last_payment_dt
# print(f' Please pay your bills! Overdue {days_last_payment.days} days.')
#
# time_from_2000 = datetime.datetime.today() - datetime.datetime(2000,1,1)
# print(time_from_2000)

#############################################

# import datetime
#
#
# months = {
#     1: 'Sausis',
#     2: 'Vasaris'
# }
#
#
# ivestis = '2020-02-11'
# my_datetime = datetime.datetime.strptime(ivestis, '%Y-%m-%d')
# print(my_datetime)
#
#
# ivestis = '2020-02-15, 10:11:59'
# my_datetime = datetime.datetime.strptime(ivestis, '%Y-%m-%d, %H:%M:%S')
#
#
# print(months.get(my_datetime.month))
#
# print(my_datetime)
# print(my_datetime.strftime('%d %m %Y'))
# print(my_datetime.strftime('%y %m %d'))
# print(my_datetime.strftime('%y %m %d'))
#############################################
import datetime
from datetime import timedelta

dabar = datetime.datetime.today()

rytoj = datetime.datetime(2025,2,28)
# mileniumas = datetime.datetime(1979, 2,26 )
print(rytoj - dabar)

# skirtumas = dabar - mileniumas
# print(skirtumas)
# print(type(skirtumas))

skirtumas = datetime.timedelta(hours=1000)
res = dabar + skirtumas

print(res)

skirtumas = datetime. timedelta(days=1000, hours=1000, minutes=100)
print(skirtumas)
# res = dabar - skirtumas
# print(res)
print(skirtumas.days / 365)
print(skirtumas.seconds)
print(skirtumas.seconds / 60 / 60)
sekundes = skirtumas.total_seconds()
print(sekundes)