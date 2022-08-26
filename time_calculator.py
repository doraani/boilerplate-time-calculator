import math
# adds n days to day and returns the new day string
def add_day(day,n):
    days_str = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    new_day_index = 0
    num_days = 7
    for i in range(0,num_days):
        if day.lower() == days_str[i].lower():
            new_day_index = (i + n) % num_days
            break
    new_day = days_str[new_day_index]
    return new_day

def add_time(start, duration, day=''):
    # start time cleanup
    start_arr = start.split(' ')
    start_time = start_arr[0]
    pm = 0
    if start_arr[1] == 'PM':
        pm = 1
    start_time = start_time.split(':')
    start_time = [int(start_time[0])+12*pm,int(start_time[1])]
    # duration cleanup
    add_time = duration.split(':')
    add_time = [int(add_time[0]),int(add_time[1])]
    mins = (start_time[1] + add_time[1]) % 60
    hours = math.floor(((start_time[0] + add_time[0])*60 + start_time[1] + add_time[1])/ 60)
    days = math.floor(hours/24)
    # day of the week and n days later display text
    days_later = ''
    if day != '':
        days_later += ', '+ add_day(day,days)
    if days == 1:
        days_later += ' (next day)'
    elif days > 1:   
        days_later += ' ('+str(days)+' days later)'
    # hours and minutes display
    hours_str = str(hours%12)
    if hours%12 < 10:
        if hours%12 == 0:
            hours_str = '12'
    mins_str = str(mins)
    if mins < 10:
        mins_str = '0'+str(mins)
    am_pm = 'AM'
    if (hours%24) >= 12:
        am_pm = 'PM'
    
    new_time = hours_str+':'+mins_str+' '+am_pm + days_later
    return new_time