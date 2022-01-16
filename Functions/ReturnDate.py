#Write a function called get_todays_date that returns
#today's date as a string, in the form year/month/day.
#For example, if today is January 15th, 2017, then it
#would return 2017/1/15.
#
#Remember, you took care of the string formatting part of
#this exercise in 2.2.9 Coding Exercise 1! Now, you're
#converting it to a function that returns the string.
#
#Note that the line below will let you access today's date
#using date.today() anywhere in your code.
from datetime import date


#Write your function here!
def get_todays_date():
    today = date.today()
    d1 = today.strftime("%Y/X%m/%d").replace("X0","")
    return d1

#If you want to test your code, you can do so by calling
#your function below. However, this is no longer required
#for grading.
print(get_todays_date())

#alternative
from datetime import date

#First, we know we want a function called get_todays_date.
#So, let's create it:

def get_todays_date():
    #Next, we know we need to actually access today's date
    #to be able to print it. The comments in the directions
    #tell us how: date.today()
    
    todays_date = date.today()
    
    #By default, str(todays_date) doesn't give us the format
    #we want. So, we need to create our result manually.
    #
    #We could do this in one long line, but let's break it
    #up. First, let's just create the empty string that we
    #will eventually return:
    
    date_string = ""
    
    #Now, let's add each piece that we need to it one by one.
    #Remember, to add an integer to a string, we first need
    #to convert it to a string using str(). It might have
    #been a while since you've done that since until now,
    #you've been mostly printing integers directly.
    
    date_string += str(todays_date.year)
    date_string += "/"
    date_string += str(todays_date.month)
    date_string += "/"
    date_string += str(todays_date.day)
    
    #Now, date_string has the value we wanted to return. So,
    #we return it:
    
    return date_string

#Now, outside the function, we'll find that if we call the
#function, it will print the right output:
print(get_todays_date())