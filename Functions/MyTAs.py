#Helping us develop this class are a team of teaching
#assistants, often called TAs for short.
#
#Write a function called my_TAs. The function should take as
#input three strings: first_TA, second_TA, and third_TA. It
#should return as output the string, "[first_TA], [second_TA],
#and [third_TA] are awesome!", with the values replacing the
#variable names.
#
#For example, my_TAs("Sridevi", "Lucy", "Xu") would return
#the string "Sridevi, Lucy, and Xu are awesome!"
#
#Hint: Notice that because you're returning a string instead
#of printing a string, you can't use the print() statement
# -- you'll have to create the string yourself, then return
#it!


#Write your function here!
def my_TAs(first_TA, second_TA, third_TA):
    TA = str(first_TA)+", "+ str(second_TA)+", and " +str(third_TA) +" are awesome!"
    return TA
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "Joshua, Jackie, and Marguerite are awesome!".
test_first_TA = "Joshua"
test_second_TA = "Jackie"
test_third_TA = "Marguerite"
print(my_TAs(test_first_TA, test_second_TA, test_third_TA))

#alternative
#As usual, we'll start with our function declaration. This
#time, we know that the function is named my_TAs, and it has
#three parameters: first_TA, second_TA, and third_TA.

def my_TAs(first_TA, second_TA, third_TA):
    
    #Now that we're in the function, we want to create the
    #string. Because we're creating and returning the string
    #instead of printing it directly, we have to use addition
    #operators to add together the individual parts
    #
    #We could do this piece-by-piece:
    
    result_string = ""
    result_string += first_TA
    result_string += ", "
    result_string += second_TA
    result_string += ", and "
    result_string += third_TA
    result_string += " are awesome!"
    
    #And then return it:
    return result_string

#Now that the function is created, we can run this file and
#see the correct output.
#
#There are other ways we could do this, though. Check out
#sample_answer_2.py and sample_answer_3.py for more advanced
#answers.


test_first_TA = "Joshua"
test_second_TA = "Jackie"
test_third_TA = "Marguerite"
print(my_TAs(test_first_TA, test_second_TA, test_third_TA))

#alternative2
#Because we're still writing the same function, the declaration
#is going to be the same:

def my_TAs(first_TA, second_TA, third_TA):
    
    #However, instead of building the string piece-by-piece, we
    #could declare it all in one line:
    
    result_string = first_TA + ", " + second_TA + ", and " + third_TA + " are awesome!"
    
    #And then, we'll return it:
    return result_string
    
    #Note that we could also skip creating a separate variable
    #for it as well. We could just return the strnig we want
    #in the first place. Comment out lines 9 and 12 and
    #uncomment line 18 to see:
    #return first_TA + ", " + second_TA + ", and " + third_TA + " are awesome!"

#There is one more advanced way to do this using a concept we
#haven't covered. Check out sample_answer_3.py if you'd like
#to see that.


test_first_TA = "Joshua"
test_second_TA = "Jackie"
test_third_TA = "Marguerite"
print(my_TAs(test_first_TA, test_second_TA, test_third_TA))

#alternative3
#Because we're still writing the same function, the declaration
#is going to be the same:

def my_TAs(first_TA, second_TA, third_TA):
    
    #Python's string data type has a method called .format.
    #We'll talk about classes and methods more in Unit 5. For
    #now, though, it's not terribly hard to read:
    
    result_string = "{0}, {1}, and {2} are awesome!".format(first_TA, second_TA, third_TA)
    
    #{0}, {1}, and {2} are placeholders inside the string for
    #where the values of certain variables will go. Then, after
    #the string, we put .format(, and then list the variables
    #in order. The first one will replace {0}, the second will
    #replace {1}, and the third will replace {2}.
    #
    #The result is a shorter line of code that can be a little
    #easier to organize since you don't have to deal with all
    #the addition operators and substrings.
    
    return result_string


test_first_TA = "Joshua"
test_second_TA = "Jackie"
test_third_TA = "Marguerite"
print(my_TAs(test_first_TA, test_second_TA, test_third_TA))