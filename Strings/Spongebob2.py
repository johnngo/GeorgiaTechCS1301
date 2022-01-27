#In the previous problem, you wrote a function that would
#convert text like "abcd efgh ijkl" into "AbCd eFgH IjKl".
#
#In the previous problem, you could assume the original
#string would be all lower-case, with no punctuation.
#
#Revise your function so that it no longer makes these
#assumptions. It should leave any punctuation marks or
#numerals unchanged, and it should change the case of
#every letter at an even index. That means if the letter
#is initially uppercase, it should be converted to lower
#case.
#
#For example: mock("Abcd. Efgh.. Ijkl!") would return
#"abCd. efGh.. IJkL!". The even-index letters (A, C, E, g,
#j, l) changed case, all other characters were unchanged.
#
#HINT: Lowercase letters always have an ordinal between
#97 ("a") and 122 ("z"). Uppercase letters always have an
#ordinal between 65 ("A") and 90 ("Z").


#Write your function here!
def mock(word):
    index = 0
    result = ''
    for letter in word:
        if index % 2 == 0:
            if letter.isupper():
                result += letter.lower()
            else:
                result += letter.upper()
        else:
            result += letter
        index += 1
    return result


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "abCd. efGh.. IJkL!".

print(mock("Abcd. Efgh.. Ijkl!"))

#As always, we start the function:
def mock(a_str):
    
    #We'll stick to the same general approach as last time.
    #So, we start by creating an empty string that will hold
    #our result:
    result = ""
    
    #Now, we want to iterate through each character in the
    #string again. We still need to know the current letter's
    #index, so we'll use a for loop...
    for i in range(0, len(a_str)):
        
        #...then get the character at that index.
        current_character = a_str[i]
        
        #Now, whether or not we alter this character depends
        #on what it is. If it's a letter, it will be changed.
        #If it's not, it won't. The easiest way to tell if
        #it's a letter is to check its ordinal. So, let's get
        #its ordinal:
        cc_ord = ord(current_character)
        
        #Now, when do we want to change this character? We want
        #to change it if (a) it's at an even index, and (b) if
        #it's a letter. We can check if it's at an even index
        #using i % 2 == 0. How do we check if it's a letter?
        #
        #Remember, letters have ordinals from 65 to 90 (for
        #uppercase) or 97 to 122 (for lowercase). So, cc_ord
        #needs to be in one of those ranges:
        if i % 2 == 0 and ((65 <= cc_ord <= 90) or (97 <= cc_ord <= 122)):
            
            #We only run these lines if the condition on line
            #32 was true. That means we know that cc_ord is in
            #one of those two ranges.
            #
            #Next, we want to know which range it's in. We could
            #check the entire range, but since we know it's in
            #one of the two, we can just check one number:
            if cc_ord <= 90:
                
                #If this next line is reached, the conditional
                #on line 41 is true. That means cc_ord represents
                #an uppercase letter, so we want to add 32 to
                #convert it to a lowercase letter.
                new_ord = cc_ord + 32
                
            else:
                
                #Otherwise, it's a lowercase letter, and we want
                #to subtract 32 to make it an uppercase letter.
                new_ord = cc_ord - 32
                
            #Either way, though, we want to convert that new
            #ordinal to a character and add it to the string.
            result += chr(new_ord)
            
        else:
            
            #If the index wasn't even or the character wasn't a
            #letter, we just add it as-is:
            result += current_character
            
    #Finally, we return the result:
    return result




print(mock("Abcd. Efgh.. Ijkl!"))