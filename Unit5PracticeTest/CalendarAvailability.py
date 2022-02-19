#This is a very simple problem where we are given a start and end time
#However, these are given in a list. The list contains instances of the
#Meeting. We have to access these times individually by writing for-each loop.

def check_availability (list_meeting, proposed_time):
    for time in list_meeting:

#The next thing we need to do is access the start_time and end_time which
#are attributes to the Meeting class. The 'time' variable is an instance of
#Meeting, which means that time.start_time and time.end_time will give us
#the appropriate start and end time for that specific instance.
#We write a condition that will determine whether the proposed_time we are
#given interfere with the start and end time.

        if time.start_time <= proposed_time <= time.end_time:
            return False
    return True

#If one of the 'time' conflict then we return False.
#We only return True when all the times do not conflict with the


#Imagine you're writing a program to check if a person is
#available at a certain time.
#
#To do this, you want to write a function called
#check_availability. check_availability will have two
#parameters: a list of instances of the Meeting class, and
#proposed_time, a particular date and time.
#
#check_availability should return True (meaning the person
#is available) if there are no instances of Meeting that
#conflict with the proposed_time. In other words, it should
#return False if proposed_time is between the start_time and
#end_time for any meeting in the list of meetings.
#
#The Meeting class is defined below. It has two attributes:
#start_time and end_time. start_time is an instance of the
#datetime class showing when the meeting starts, and
#end_time is an instance of the datetime class indicating
#when the meeting ends.
#
#Hint: Instances of the datetime have at least six
#attributes: year, month, day, hour, minute, and second.
#
#Hint 2: Comparison operators work with instances of the
#datetime class. time_1 < time_2 will be True if time_1 is
#earlier than time_2, and False otherwise.
#
#You should not assume that the list is sorted.

#Here is our definition of the Meeting class:
from datetime import datetime
from typing import List

class Meeting:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

#Write your function here!
def check_availability(lst_meeting: List[Meeting], proposed_time: datetime) -> bool:
    for time in lst_meeting:
        if  time.start_time <= proposed_time <= time.end_time:
            return False
    return True


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, then False
meetings = [Meeting(datetime(2018, 8, 1, 9, 0, 0), datetime(2018, 8, 1, 11, 0, 0)),
            Meeting(datetime(2018, 8, 1, 15, 0, 0), datetime(2018, 8, 1, 16, 0, 0)),
            Meeting(datetime(2018, 8, 2, 9, 0, 0), datetime(2018, 8, 2, 10, 0, 0))]
print(check_availability(meetings, datetime(2018, 8, 1, 12, 0, 0)))
print(check_availability(meetings, datetime(2018, 8, 1, 10, 0, 0)))
