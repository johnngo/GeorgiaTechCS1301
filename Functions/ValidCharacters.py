#There are a lot of use cases where we want to check to see
#if a string has any invalid characters in it. For example,
#when asking for a credit card number, we want to make sure
#there are no non-numerals (although we might accept dashes
#or spaces). When asking for a name, we want to make sure
#all the characters are letters, spaces, or the occasional
#punctuation mark.
#
#Write a function called is_valid. is_valid should take two
#parameters: a string to check, and a string of all valid
#characters.
#
#is_valid should return the boolean True if all the
#characters in the string to check are present in the string
#of valid characters. It should return False if any character
#in the checked string does not appear.


#Add your code here!
def is_valid(string, validcharacters):
    for character in string:
        print(character)
        if character not in validcharacters:
            print(validcharacters)
            return False
    return True 


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print True, then False
sample_valid_string = "1234-5678-9011-1111"
sample_invalid_string = "1234!5678.9011?1111"
valid_characters = "0123456789-"

print(is_valid(sample_valid_string, valid_characters))
print(is_valid(sample_invalid_string, valid_characters))



#There are a lot of ways we could do this problem. Some are
#extremely complicated. One, however, is very easy.
#
#To write this easy solution, we have to understand: once
#we find a *single* invalid character, we can go ahead and
#quit searching and return False. It only takes one invalid
#character to invalidate the string.
#
#That means also that if we search to the end of the string
#and find *no* invalid characters, then we can return True.
#If we finish searching and the function hasn't ended, then
#no invalid characters were found.
#
#So, we start by defining the function:

def is_valid(a_string, valid_characters):
    
    #Then we loop through each character in the string:
    for character in a_string:
        
        #And check to see if it's in the string of valid
        #characters. If it's not...
        if not character in valid_characters:
            
            #Then we're done! We go ahead and return
            #False right here and now.
            return False
        
    #Then if that loop runs to completion, that means that
    #no invalid characters were ever found. If that's the
    #case, the string is valid, and we can return that:
    return True

    #Note that line 32 is *not* indented under the for loop.
    #It's only indented under the function. That means this
    #line will only be reached if the loop finishes running,
    #which will only happen if line 27 never runs, which
    #will only happen if every character is valid.
    
    
sample_valid_string = "1234-5678-9011-1111"
sample_invalid_string = "1234!5678.9011?1111"
valid_characters = "0123456789-"

print(is_valid(sample_valid_string, valid_characters))
print(is_valid(sample_invalid_string, valid_characters))
