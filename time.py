import datetime

date = datetime.date(2020, 1, 2)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()
now1 = now.strftime("%H:%M:%S")
now2 = now.strftime("%H:%M:%S %m-%d-%Y")

print(date)
print(today)
print(time)
print(now)
print(now1)
print(now2)

target_datetime = datetime.datetime(2026, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date hasnt passed")