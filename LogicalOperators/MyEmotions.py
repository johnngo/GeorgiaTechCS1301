busy = True
hungry = False
tired = True
stressed = False

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Logical operators get more complex when we start using them
#with the results of other logical operators. So, let's try
#it out!
#
#Using the variables above, we want to assess whether the
#person is happy, sad, bored, confused, or anxious.
#
# - The person is happy if they're busy but not stressed.
# - The person is sad if they're either hungry or tired.
# - The person is confused if they're both happy and sad.
# - The person is bored if they're neither happy, sad,
#   nor busy.
# - The person is anxious if they're neither happy nor sad,
#   but they are stressed.
#
#Add code below whose output will list whether each of these
#emotions is true or false. For example, with the original
#values of the variables above, this would print:
#
#Happy: True
#Sad: True
#Confused: True
#Bored: False
#Anxious: False


#Add your code here!
happy = busy and not(stressed)
sad = hungry or tired
confused = happy and sad
bored = not(happy or sad or busy)
anxious = not(happy or sad) and stressed
print("Happy:", happy)
print("Sad:", sad)
print("Confused:", confused)
print("Bored:", bored)
print("Anxious:", anxious)



busy = True
hungry = False
tired = True
stressed = False

#-----------------------------------------------------------
#Let's start by finding the things that are based solely on
#the variables given above: happy and sad.

happy = busy and not stressed
sad = hungry or tired

#Now that we have values for happy and sad, we can use them
#in our other logic. We can pretend at this point that happy
#and sad were given to us: they exist just as if they had
#been provided initially.

confused = happy and sad

bored = not (happy or sad or busy)
#We could also write this line as:
#bored = not happy and not sad and not busy

anxious = not (happy or sad) and stressed
#We could also write this line as:
#anxious = not happy and not sad and stressed

#Then, we print our results:
print("Happy:", happy)
print("Sad:", sad)
print("Confused:", confused)
print("Bored:", bored)
print("Anxious:", anxious)
