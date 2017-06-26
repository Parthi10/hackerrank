from collections import defaultdict
from operator import itemgetter

def solution(S):
    meeting_map = defaultdict(list)
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for line in S.strip().split('\n'):
        day, timings = line.strip().split(' ')
        start, end = timings.split('-')
        start_hours, start_minutes = map(int, start.split(':'))
        end_hours, end_minutes = map(int, end.split(':'))
        timings = [start_hours, start_minutes], [end_hours, end_minutes]
        meeting_map[day].append(timings)
    max_sleep_time = 0
    i=0
    #set meetings in ascending order
    for i in meeting_map:
        meetings = meeting_map[i]
        order_list = []
        for j in meetings:
            order_list.append(j[0][0])
        print(order_list)
    while i<7:
        day = days[i]
        meetings =  meeting_map[day]
        # print day, meetings
        morning_sleep = meetings[0][0][0]*60 + meetings[0][0][0]
        # print "morning sleep", morning_sleep
        max_inbetween_sleep = 0
        num_of_meetings = len(meetings)
        # print "number of meetings", num_of_meetings
        if num_of_meetings>1:
            j = 0
            while j < num_of_meetings-1:
                sleep = (meetings[j+1][0][0] - meetings[j][1][0]) * 60
                sleep += meetings[j+1][0][1] - meetings[j][1][1]
                if max_inbetween_sleep < sleep:
                    max_inbetween_sleep = sleep
                j+=1
            # print "max_inbetween_sleep", max_inbetween_sleep

        night_sleep = ((24 - meetings[-1][1][0]) * 60) + meetings[-1][1][1]
        # print "night_sleep", night_sleep
        if i<6:
            next_day = days[i+1]
            meetings =  meeting_map[next_day]
            morning_sleep = meetings[0][0][0]*60 + meetings[0][0][0]
            # print "next morning sleep", morning_sleep
        i+=1
        temp_sleep = max(morning_sleep, max_inbetween_sleep, night_sleep+morning_sleep)
        if max_sleep_time<temp_sleep:
            max_sleep_time=temp_sleep
        # print "\n"
    return max(max_sleep_time, 180)


S = '''Sun 10:00-20:00
Fri 05:00-10:00
Fri 16:30-23:50
Sat 10:00-24:00
Sun 01:00-04:00
Sat 02:00-06:00
Tue 03:30-18:15
Tue 19:00-20:00
Wed 04:25-15:14
Wed 15:14-22:40
Thu 00:00-23:59
Mon 05:00-13:00
Mon 15:00-21:00'''

print solution(S)
