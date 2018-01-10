
from datetime import date

birthday = date(2000,1,29)
print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.isoformat())
print(date.today())

from datetime import time

tm = time(11,22,33,444)
print(tm.hour)
print(tm.microsecond)
print(tm.isoformat())

from datetime import datetime

someDay = datetime(2000, 3, 28, 11, 22, 33, 12345)
print(someDay.isoformat())
