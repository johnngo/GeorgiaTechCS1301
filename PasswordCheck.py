entered = "abc123"
password = "abc123"
tries = 3

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Above we've created three variables representing an attempt
#to enter a password. Add some code below that will print the
#result of this check:
#
# - "Login successful." if entered is the same as password
#   and tries is less than or equal to 3.
# - "Incorrect password." if entered is not the same as 
#   password, but tries is less than or equal to 3.
# - "Tries exceeded." if tries is greater than 3.
#
#You don't need to worry about incrementing tries if the
#password is incorrect.


#Add your code here!

if entered in password and tries <=3:
    print("Login successful.")

if entered not in password and tries <=3:
    print("Incorrect password.")

if tries > 3:
    print("Tries exceeded.")

#alternatively
entered = "abc123"
password = "abc123"
tries = 3

#-----------------------------------------------------------
#The tempting approach here is to check the conditions for
#each of the three possible results separately. However, that
#is a lot more complicated than it needs to be.
#
#First, we should check if tries is greater than 3: if this
#is true, then it doesn't matter whether the password is
#correct.

if tries > 3:
    print("Tries exceeded.")

#Now, if the user has run out of tries, the next two blocks
#will never trigger because they are 'else' blocks to the
#preceding 'if'. So, we don't need to recheck whether tries
#is greater than 3: if we've reached the next blocks, it
#isn't. So instead, we can just check whether the password
#is correct:

elif password == entered:
    print("Login successful.")
else:
    print("Incorect password.")
    
#We could also design this a little differently by using
#nested conditionals:

if tries > 3:
    print("Tries exceeded.")
else:
    if password == entered:
        print("Login successful.")
    else:
        print("Incorrect password.")

#Notice how an 'if' inside an 'else' functions the same as
#an 'else if'. The entire 'else' will only run if the
#preceding 'if' was False.

#This version might be a little easier to read, though,
#because it groups the possible outcomes in a way that
#makes logical sense.
