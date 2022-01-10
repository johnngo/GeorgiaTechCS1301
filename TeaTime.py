mood = "impatient"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#We've written some code below that prints out what kind of
#tea we want to  buy based on our mood. The code has an error,
#though. Rewrite the code so that it runs with the correct
#output.
#
#The correct output if mood is one of the expected moods
#(sad, anxious, tired) is the name of the tea and the cost.
#The correct output if mood is not one of the expected moods
#is None and "free".
#
#Hint: this is a scope problem!
tea=None
cost="free"

if mood == "sad":
    tea = "oolong"
    cost = 3.99
elif mood == "anxious":
    tea = "green tea"
    cost = 5.45
elif mood == "tired":
    tea = "english breakfast"
    cost = 4.35
else:
    tea = None

print(tea)
print(cost)

#alternative answer
mood = "impatient"

#Our issue here is that if mood is not one of our three
#expected moods, then the else block at the end triggers --
#however, it does not create a cost variable, and so the
#second print statement gives us an error. To fix this, we
#need to make sure cost is created no matter what.
#
#To do this, we can either add cost to the beginning or the
#end. The more logical thing is probably to add it to the
#end:

if (mood == "sad"):
    tea = "oolong"
    cost = 3.99
elif (mood == "anxious"):
    tea = "green tea"
    cost = 5.45
elif (mood == "tired"):
    tea = "english breakfast"
    cost = 4.35
else:
    tea = None
    cost = "free"

print(tea)
print(cost)