cold = False
windy = False

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#In this problem, we want to print the message, "You should
#wear a jacket today!" if it's cold or windy, or the message
#"You don't need a jacket today!" if it's not.
#
#At the bottom of this file, we've added some code that
#handles printing these two messages. For this code to work,
#the variable need_jacket needs to exist. Its value should be
#True (the boolean, not the string) if it's cold or windy,
#False if it's neither cold nor windy.
need_jacket = cold or windy

#Add your code to create the variable need_jacket with the
#appropriate value here!


#Do not modify the code below. It will work if you have
#correctly create the variable need_jacket with the
#appropriate value.
if need_jacket:
    print("You should wear a jacket today!")
else:
    print("You don't need a jacket today!")


cold = False
windy = False

#The code we need to write for this is actually pretty much
#the same as the previous problem. If you were assigning the
#value to a variable, it's exactly the same: if you were
#printing it directly, then you just needed to replace print
#with need_jacket = , as shown:

need_jacket = cold or windy

#That creates the variable need_jacket with the appropriate
#True or False value. That then allows the code below to work:
#the first print statement runs if need_jacket is True, and
#the second runs if need_jacket wasn't True. We'll learn more
#about this in Chapter 3.2.

if need_jacket:
    print("You should wear a jacket today!")
else:
    print("You don't need a jacket today!")
