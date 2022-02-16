#We've started a recursive function below called
#measure_string that should take in one string parameter,
#myStr, and returns its length. However, you may not use
#Python's built-in len function.
#
#Finish our code. We are missing the base case and the
#recursive call.
#
#HINT: Often when we have recursion involving strings, we
#want to break down the string to be in its simplest form.
#Think about how you could splice a string little by little.
#Then think about what your base case might be - what is
#the most basic, minimal string you can have in python?
#
#Hint 2: How can you establish the base case has been
#reached without the len() function?

#You may not use the built-in 'len()' function.

def measure_string(myStr):
    if not myStr:#Complete this line!
    	return 0#Complete this line!
    else:
        return 1 + measure_string(myStr[1:])#Compulete this line!
    
    
#The line below will test your function. As written, this
#should print 13. You may modify this to test your code.
print(measure_string("13 characters"))


#First, we define the function:
def measure_string(myStr):
    
    #If we can't use the length function, then how do we
    #ever know what the string is? Well, eventually if we
    #remove one character at a time, then it will be an
    #empty string with no characters:
    if myStr == "":
        
        #If that's the case, go ahead and return 0!
    	return 0
    
    #If the string isn't empty, then we remove one character,
    #and measure it again, adding one to the result:
    else:
        return 1 + measure_string(myStr[:-1])
    
    

print(measure_string("13 characters"))
