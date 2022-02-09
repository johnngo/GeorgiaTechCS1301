#APA citation style cites author names like this:
#
#  Last, F., Joyner, D., & Burdell, G.
#
#Note the following:
#
# - Each individual name is listed as the last name, then a
#   comma, then the first initial, then a period.
# - The names are separated by commas, including the last
#   two.
# - There is also an ampersand and additional space before
#   the final name.
# - There is no space or comma following the last period.
#
#Write a function called names_to_apa. names_to_apa should
#take as input one string, and return a reformatted string
#according to the style given above. You can assume that
#the input string will be of the following format:
#
#  First Last, David Joyner, and George Burdell
#
#You may assume the following:
#
# - There will be at least three names, with "and" before
#   the last name.
# - Each name will have exactly two words.
# - There will be commas between each pair of names.
# - The word 'and' will precede the last name.
# - The names will only be letters (no punctuation, special
#   characters, etc.), and first and last name will both be
#   capitalized.


#Write your function below!
def names_to_apa(a_string):
    string = a_string.split(",")
    finalstring =""
    for i in string:
     
        if " and " in i:
            i =i.split()
          
            finalstring += "& " + i[2] + ", " + i[1][:1] + "."
            
        else:
            i = i.split()
       
            finalstring +=i[1] +", " + i[0][:1]+"., "
    return finalstring


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Last, F., Joyner, D., & Burdell, G.
print(names_to_apa("First Last, David Joyner, and George Burdell"))


#As you can through the code, it might look confusing, but
#most of it is formatting it to what the problem should print!
#
#We first create a list of names by splitting the string
#with "," since the names are separated with commas
#We also create an empty string where we will concatenate all
#the abbreviated APA versions of the names.

    list_names = string.split(",")
    result = ""

#Now, from the list of names we have made, we iterate through
#with a for each loop. 'name' variable is currently a string.
#In order to separately access the first and last name of each
#author, we have to further split the 'name' string.
#Note that name (for example) will be: and George Burdell

    for name in list_names:
        fullName = name.split() 

#Now, fullName is, for example, is ["David", "Joyner"]
#
#Since the last name will always have the world "and"
#if the 0th index of the fullName list is NOT "and"
#we have the format of: Last, F.,
#
#Last name is accessed by fullName[1]
#The first letter of the first name is accessed by fullName[0][0]
#The first [0] means the index of the list and the second [0]
#means the first letter of the string
#We concatenate appropriately with spaces, commas and periods.

        if fullName[0] != "and":
            result += fullName[1] + ", " + fullName[0][0] + "., "

#From the condition, we know that if the first index is "and"
#then it is the last name on the list.
#For example, fullName would be ["and", "George", "Burdell"]
#Thus we will format it and correctly access the index and
#concatenate to the result string

        else:
            result += "& " + fullName[2] + ", " + fullName[1][0] + "."

#Once done, we return the result

    return result