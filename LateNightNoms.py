hour = 3
minute = 45

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Around Georgia Tech, there are plenty of places to get a
#late night bite to eat. However, they have different hours,
#so when choosing where to go, you have to think about who's
#still open!
#
#Imagine you're choosing between the following restaurants:
#
# - Barrelhouse: Closes at 11:00PM
# - Taco Bell: Closes at 2:00AM
# - Cookout: Closes at 3:00AM
# - Waffle House: Never closes. Ever.
#
#Assume that this list is also a priority list: if Barrelhouse
#is open, you choose Barrelhouse. If not, you choose Taco Bell
#if it's open. If not, you choose Cookout if it's open. If
#not, you choose Waffle House.
#
#However, there are two wrinkles:
#
# - We're using 12-hour time.
# - hour will always represent a time from 10PM to 5AM.
#
#That means that if hour is 10 or 11, it's PM; if hour is
#12, 1, 2, 3, 4, or 5, it's AM. This will make your reasoning
#a little more complex. You may assume that all four
#restaurants open later than 6AM, though, so you don't have
#to worry about opening time, just closing time.
#
#Add some code below that will print what restaurant you'll
#go to based on the current values of hour and minute.


#Add your code here!

if hour > 6 and hour < 11:
    print("Barrelhouse")
elif (hour > 6 and hour < 12) or (hour >= 12 and hour < 13) or (hour >= 1 and hour < 2):
     print ("Taco Bell")
elif (hour > 6 and hour < 12) or (hour >= 12 and hour < 13) or (hour >= 1 and hour < 3):
    print ("Cookout")
else:
    print("Waffle House")

#alternative answer
#For starters, we only go to Barrelhouse if hour is 10
#because it closes at 11. So, our first condition to check
#is:
if hour == 10:
    print("Barrelhouse")

#Then, we have a three-hour range where we choose Taco Bell,
#from 11:00PM to 1:59AM. So, we can check if hour is 11, 12,
#or 1:
elif hour == 11 or hour == 12 or hour == 1:
    print("Taco Bell")

#Then, there's only one hour between when Taco Bell closes
#and Cookout closes. So, we only check 2 for Cookout:
elif hour == 2:
    print("Cookout")

#And since we guaranteed that hour will be between 10PM and
#5AM, our only remaining possible outcome is Waffle House:
else:
    print("Waffle House")

#However, there is a more clever way we might do this. Check
#out sample_answer_2.py for that!

#How could we do that conversion? We could use a conditional:

hour += 3
if hour > 12:
    hour -= 12

#Here, we add 3 hours to hour, and then if that pushes it to
#13 or higher, we subtract 12 hours. So, 11:00 becomes 14:00,
#which becomes 2:00.
#
#Now, we can check our opening times more naturally:

if hour < 2:
    print("Barrelhouse")
elif hour < 5:
    print("Taco Bell")
elif hour < 6:
    print("Cookout")
else:
    print("Waffle House")
    
