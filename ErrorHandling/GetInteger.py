#Write a function called get_integer that takes as input one
#variable, my_var. If my_var can be converted to an integer,
#do so and return that integer. If my_var cannot be converted
#to an integer, return a message that says, "Cannot convert!"
#
#For example, for "5" as the value of my_var, get_integer would
#return the integer 5. If the value of my_var is the string
#"Boggle.", then get_integer would return a string with the
#value "Cannot convert!"
#
#Do not use any conditionals or the type() function.


#Write your function here!
def get_integer(my_var):
    try:
        return int(my_var)
    except Exception as error:
        return "Cannot convert!"

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 5, Cannot convert!, and 5.

print(get_integer("5"))
print(get_integer("Boggle."))
print(get_integer(5.1))


#alternative
#Going back to functions, we start with our function name
#and its parameter list:
def get_integer(my_var):
    
    #Next, we want to try to convert the variable to an
    #integer. Since we just said 'try', it makes sense that
    #here is where our try block should start:
    try:
        
        #Inside the try block, we put the code we want to
        #try: here, we want to convert my_var to an
        #integer. We could store the result of int(my_var)
        #to a variable and then return that variable, or
        #we can just return it directly:
        
        return int(my_var)
    
    #If that line failed, we'll jump down to this except
    #block, where we want to print our message indicating
    #it failed:
    except:
        return "Cannot convert!"


print(get_integer("5"))
print(get_integer("Boggle."))
print(get_integer(5.1))
