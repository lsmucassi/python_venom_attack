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
 def get_mandates(file):
    date_fmt = '%m/%d/%Y, %H:%M:%S'
    pending = []
    with open(file, 'r') as f:
        data = f.read().splitlines()
    
    for i, d in enumerate(data):
         data[i] = ast.literal_eval(d)

    # get pending mandates older than 24HR
    for mandate in data:
        '''
            [2] - year
            [0] - Month
            [1] - Day
        '''
        now = datetime.datetime.now()
        man_time = mandate['timestamp'][:]
        today_time = now.strftime(date_fmt)
        man_dtime = datetime.datetime.strptime(man_time, date_fmt)
        today_dtime = datetime.datetime.strptime(today_time, date_fmt)

        if man_dtime > today_dtime:
            time_diff = man_dtime - today_dtime
        else:
            time_diff = today_dtime - man_dtime
        # time_diff_mins = int(round(time_diff.total_seconds() / 60))
        if time_diff.days >= 1:
            pending.append(mandate)
            print("\n==============================================================================")
            print(man_time)
            print(today_time)
            print(f'Total days {time_diff.days}')
            print(f'Total hours {time_diff / datetime.timedelta(hours=1)}')
            print(f'The difference is approx. {time_diff}')
            print("==============================================================================")
        
    print(f"\nTOTAL NUMBER OF OVERDUE MANDATES: {len(pending)}\n")
    return pending

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
