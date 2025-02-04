import datetime
#5. ###################################
ivestis = '2020-01-01'
my_datetime = datetime.datetime.strptime(ivestis, '%Y-%m-%d')
print(my_datetime)
#6. ###################################


# Įvedame datą ir laiką
ivedam = '2022-12-31, 23:59:59'

my_datetime = datetime.datetime.strptime(ivedam, '%Y-%m-%d, %H:%M:%S')
formatted_time = my_datetime.strftime('%d/%m/%Y, %H:%M:%S')
print(formatted_time)


data_laikas = datetime(2022, 12, 31, 23, 59, 59)
