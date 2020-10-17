def alarm_clock(week_day, vacation):
    if (week_day >= 1  and week_day <= 5) and vacation == False:
        return "07:00"
    elif (week_day == 0  or week_day == 6) and vacation == False:
        return "10:00"
    elif (week_day >= 1  and week_day <= 5) and vacation == True:
        return "10:00"
    elif (week_day == 0  or week_day == 6) and vacation == True:
        return "Off"
    
print(type(alarm_clock(1, False))) #→ '7:00'
print(alarm_clock(5, False)) #→ '7:00'
print(alarm_clock(0, False)) #→ '10:00'