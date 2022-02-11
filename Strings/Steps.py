#Now, let's improve our steps() function to take one parameter
#that represents the number of 'steps' to print. It should
#then return a string that, when printed, shows output like
#the following:
#
#print(steps(3))
#111
#	222
#		333
#
#print(steps(6))
#111
#	222
#		333
#			444
#				555
#					666
#
#Specifically, it should start with 1, and show three of each
#number from 1 to the inputted value, each on a separate
#line. The first line should have no tabs in front, but each
#subsequent line should have one more tab than the line
#before it. You may assume that we will not call steps() with
#a value greater than 9.
#
#Hint: You'll want to use a loop, and you'll want to create
#the string you're building before the loop starts, then add
#to it with every iteration.


#Write your function here!
def steps(no_steps):
    st = ''
    j = 0
    for i in range(0, no_steps):
        st += (("\t" *(i)) + (str(i+1) * 3) + '\n')
        j+=1
    return st


#The following two lines will test your code, but are not
#required for grading, so feel free to modify them.
print(steps(3))
print(steps(6))

#We'll start with the function definition. The function is
#called steps(), and we'll call its parameter num_steps:
def steps(num_steps):
    
    #Next, we're going to be building a string as the
    #function runs. So, we want to go ahead and create it
    #so we have something to add to:
    
    result_string = ""
    
    #Now, we want to run a loop for the number of steps we
    #want to have. So, we create a range from 1 to
    #num_steps + 1 since Python stops one short of the
    #second argument to range():
    for i in range(1, num_steps + 1):
        
        #Now, what do we do for each step? We need three
        #things. First, we need the tabs at the start of
        #the line. We can do that by multiplying the tab
        #character "\t" by i - 1 (minus 1 since we don't
        #want tabs on the first line):
        
        result_string += "\t" * (i - 1)
        
        #Next, we add the current value of i, as a string,
        #times 3:
        
        result_string += str(i) * 3
        
        #Finally, we need to add our line break:
        
        result_string += "\n"
        
        #We could also do all three of these lines at once:
        #
        #result_string += ("\t" * (i - 1)) + (str(i) * 3) + "\n"
        
    #After the loop is done (notice we're no longer
    #indented under the for loop), we want to return the
    #string that we just built:
    
    return result_string


print(steps(3))
print(steps(6))
