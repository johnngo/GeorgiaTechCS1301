#Write a function called snowed_in that will determine
#whether school is closed based on the weather and
#temperature. We'll pretend the school is in Georgia, where
#a little snow or sub-freezing temperatures are enough to
#close down schools!
#
#The function should take three parameters:
#
# - temperature, a float
# - weather, a string
# - is_celsius, a boolean
#
#The function should return True if temperature is below
#freezing (32 if is_celsius is False, 0 if is_celsius is
#True) or if weather is "snowy". Otherwise, it should
#return False.
#
#Note, however, that is_celsius should be an optional
#argument. If the function call does not supply a value for
#is_celsius, assume it is True.
#
#For example:
#
# snowed_in(15, "sunny") -> False
# is_celsius is assumed to be True, so 15 is not below
# freezing.
#
# snowed_in(15, "sunny", is_celsius = False) -> True
# is_celsius is False, so 15 is below freezing.
#
# snowed_in(15, "snowy", is_celsius = True) -> True
# The weather is "snowy", so the temperature doesn't matter.


#Write your function here!


def snowed_in(temperature, weather, is_celsius=True):
    if weather == "snowy":
        return True
    elif is_celsius:
        return temperature < 0
    else:
        return temperature < 32

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print False, True, and True, each on their own line.

print(snowed_in(15, "sunny")) #Should print False
print(snowed_in(15, "sunny", is_celsius = False)) #Should print True
print(snowed_in(15, "snowy", is_celsius = True)) #Should print True

#alternative
def snowed_in(temperature, weather, is_celsius = True):
    
    #Inside the function, we don't have to worry about
    #where is_celsius's value came from. So, we can start
    #with our reasoning.
    #
    #As soon as we find one reason that school would be
    #closed, we can go ahead and return True. For
    #example, if the weather is snowy, then the
    #temperature doesn't matter. So, let's go ahead and
    #return True if the weather is snowy:
    
    if weather == "snowy":
        return True
    
    #If the weather is not snowy, though, then we don't
    #need to check weather again; we just need to check
    #temperature. First, we can check if it's freezing
    #as measured in Celsius:
    elif temperature < 0 and is_celsius:
        return True
    
    #Then we can check if it's freezing as measured in
    #Fahrenheit:
    elif temperature < 32 and not is_celsius:
        return True
    
    #Below, we're doing something a little clever. The
    #only way to reach this part of the function is if
    #the weather wasn't snowy and the temperature wasn't
    #freezing. If either of those were True, then the
    #returns on lines 35 or 40 would have been called,
    #which ends the function. So, if we've gotten this
    #far, we know that school is not closed, so we go
    #ahead and return False:
    
    return False
    
    #This is like inferring an 'else'. An 'else' is for
    #code that can only be reached if other conditions
    #were False. Similarly, line 51 is only reachable if
    #the function did not already return.

#alternative
def snowed_in(temperature, weather, is_celsius = True):
    
    #Note that we could accomplish this entire function
    #in only one line. Here's the line:
    
    return weather == "snowy" or temperature < 0 or (temperature < 32 and not is_celsius)
    
    #How does that line work? It's one long boolean statement.
    #At the top level, the logical operators are all 'or'. So,
    #only one of the three parts needs to be True for the
    #statement as a whole to be True:
    #
    # - If weather is snowy, then the statement is True.
    # - If temperature is less than 0, then it doesn't matter
    #   if we're in Celsius or Fahrenheit: both are freezing,
    #   so the statement is True.
    # - If temperature is less than 32 and we're in Fahrenheit,
    #   then the statement is True.
    #
    #If all of those things are False, the statement is False.
    #So, we just return the result of that expression.
