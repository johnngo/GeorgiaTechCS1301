years = 2
months = 5
days = 24

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Ever been at a loss for what to do for your significant
#other for Valentine's Day? Let's right some code to generate
#a gift recommendation!
#
#The variables above give the length of the relationship in
#number of years, months, and days. Add some code below to
#print a gift recommendation based on these values:
#
# - If you've been dating for at least 4 years, give them a
#   dog ("dog").
# - If you've been dating for at least 1 year but less than
#   4 years, give them a watch ("watch").
# - If you've been dating for at least 6 months but less than
#   1 year, give them concert tickets ("concert tickets").
# - If you've been dating for at least a day but less than 6
#   months, give them candy ("candy").
# - If aren't actually dating, go big or go home: give them
#   a yacht to sail away together ("yacht").
#
#Note that no matter what, you should only print one gift.


#Add your code here!

if years >= 4:
    print("dog")
elif years >= 1 and years < 4:
    print("watch")
elif years < 1 and months >= 6:
    print("concert tickets")
elif months < 6 and days >= 0 and months >=1:
    print("candy")
elif months <6 and days >=1 and months >=0:
    print("candy")
else:
    print("yacht")

#alternate
#However, this answer is far more complicated than it needs
#to be. elif lets us "automatically" incorporate each
#condition into the next one because we know the only way
#for the next one to be reached is if the previous one was
#false.
#
#So, let's start by checking the one variable that overrules
#them all. If years is greater than or equal to 4, we're done.

if years >= 4:
    print("dog")

#Now, all our next blocks will be elif or else blocks. That
#means we know these are only checked if the one above was
#False. So, we don't need to re-check whether years is less
#than 4: if it wasn't, we would never reach these blocks! So,
#next we just need to check if years is greater than or equal
#to 1.
elif years >= 1:
    print("watch")

#Note that if years is greater than 4 or greater than 1, we
#didn't need to worry about the value of months or days. Now,
#though, we do. However, as before, we don't have to recheck
#years each time: the only way to reach this next part is if
#years was 0.
elif months >= 6:
    print("concert tickets")

#If months was greater than or equal to 6, we didn't need to
#check days.
#
#The last block is interesting, though. We should print
#"candy" if either months or days is greater than 1: "candy"
#is the right result if we've been dating for 5 months and 0
#days, or for 0 months and 5 days. So, we need to use an or:
elif months >=1 or days >= 1:
    print("candy")

#Finally, this last one is an 'else' because it only runs if
#none of the previous cases were true. We've systematically
#ruled out everything except for months, days, and years, all
#being 0:
else:
    print("yacht")

#Note that a potential alternate approach would be to use
#years, months, and days to calculate the relationship length
#in total days (e.g. 1825 days for a 5-year relationship).
#However, because months and years can have different numbers
#of days, that might present issues.
