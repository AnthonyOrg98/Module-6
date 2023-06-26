import sys
from datetime import datetime, timedelta

dt = datetime.now()

time_string = dt.strftime("%X")

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        _date, _time, store, item, cost, payment = data

        print (f'{dt}\t{time_string}\t{store}\t{item}\t{cost}\t{payment}')
        break

x= dt - timedelta(days=730,seconds=60)
print(x)

day = timedelta(days=10, hours=10, minutes=13)
print(day)