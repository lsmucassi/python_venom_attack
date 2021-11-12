 from functools import reduce
from datetime import timedelta
import datetime
import time
import ast
import json

def deep_get(dictionary, keys, default=None):
    return reduce(
        lambda d, 
        key: d.get(key, default) if isinstance(d, dict) else default, 
        keys.split("."), 
        dictionary
    )

man_date = (mandate['timestamp'][:10]).split('/')
man_date = [int(integer) for integer in man_date]
print(man_date)

date = datetime.date(man_date[2], man_date[0], man_date[1])
date_of_today = datetime.date.today()

# if date != date_of_today:
#     print(True)
# else:
#     print(False)
    
# s1 = data[0]['timestamp'][12:] #10:33:26'
# print(s1)
# # s2 = '11:15:49' # for example

# now = datetime.datetime.now()

# s2 = now.strftime("%H:%M:%S")
# print("Current Time =", s2)

# FMT = '%H:%M:%S'
# tdelta = datetime.datetime.strptime(s2, FMT) - datetime.datetime.strptime(s1, FMT)
# print(tdelta)


# print(data[0]['timestamp'][:10])
# datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
