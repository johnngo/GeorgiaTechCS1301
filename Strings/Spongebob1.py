def mock(a_str):
    result=""
    for i in range(0,len(a_str)):
        current_character = a_str[i]
        cc_ord = ord(current_character)
        if i % 2 == 0 and ((65 <= cc_ord <= 90) or (97 <= cc_ord <= 122)):
            if cc_ord <= 90:
                new_ord = cc_ord -32
            else:
                new_ord = cc_ord - 32
            result += chr(new_ord)
        else:
            result += current_character            
    return result


#First thing's first: we need to define our function:
def mock(a_str):
    
    #There are a lot of ways to go from here. My personal
    #approach would be to create a new string, and build
    #that over time. So, let's create a new empty string:
    
    result = ""
    
    #Next we want to iterate through each character in the
    #string. However, we need to track whether the current
    #letter's index is even or odd, so let's use a for
    #loop instead of a for-each loop: that way we have the
    #current index stored in i:
    for i in range(len(a_str)):
        
        #Then we need to get the actual character:
        current_char = a_str[i]
        
        #Now we have a decision to make. When do we want to
        #change the current character? We want to change it
        #if (a) its index is even, and (b) if it isn't a
        #space. So, that's our conditional:
        if i % 2 == 0 and not current_char == " ":
            
            #This block runs if the index is even and the
            #character is a lowercase letter. So, we know
            #that current_char is a lower-case letter. So,
            #let's first find its ordinal:
            current_char_ord = ord(current_char)
            
            #Now let's find the ordinal of its uppercase
            #version. We know that that's always 32 less
            #from the exercise directions:
            new_char_ord = current_char_ord - 32
            
            #Now let's convert the new ordinal back to a
            #character:
            new_char = chr(new_char_ord)
            
            #Finally, let's add it to the string:
            result += new_char
            
            #We did that step-by-step, but it could have
            #all been done in one line as well:
            #result += chr(ord(current_char)-32)
            
        else:
            
            #If current character was a space or it was
            #at an odd index, we just add it to the string
            #as-is:
            result += current_char
            
    #Once we're done building the string, we return the
    #result:
    return result
        



print(mock("abcd efgh ijkl"))
