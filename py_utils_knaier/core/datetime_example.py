from datetime import datetime

current_date = datetime.now()
print(current_date)
print(type(current_date)) #<class datetime.datetime>

date_no_time = datetime.strftime(datetime.now(), '%Y-%m-%d')
print(date_no_time)
print(type(date_no_time)) #<class datetime.datetime>

