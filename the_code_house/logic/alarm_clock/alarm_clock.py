
def alarm_clock(week_day, vacation):
    result = ''
    if (week_day >= 1 and week_day <= 5) and vacation == False:
        result = '07:00'
    elif (week_day == 0  or week_day == 6) and vacation == False:
        result = '10:00'
    elif (week_day >= 1 and week_day <= 5) and vacation == True:
        result = '10:00'
    elif (week_day == 0 or week_day == 6) and vacation == True:
        result = 'off'
    return result

