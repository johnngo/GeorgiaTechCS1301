#For this problem your initial thought should be that we need to iterate through
#the given list of integers NOT list of strings.
#This is because we only need to change the values of the given indexes, not all
#the values of the list of strings. If we did iterate through list of strings instead
#this would causes problems of if we had to change from upper to lower twice.

def alter_list (list_strings, list_int):
    for index in list_int:

#From the index we are iterating through, we check to see if it is upper.
#Python has a build in function that checks for us if it is upper.

        if list_strings[index].isupper():
            list_strings[index] = list_strings[index].lower()
        else:
            list_strings[index] = list_strings[index].upper()

#If the string in the list_strings is not upper then we know it is lower so
#in our else block we upper() the string.

#When we are done iterating through the list_int we know that we
#don't need to edit any more strings so we return our list_strings
#We can return the same list_strings that was passed in because
#lists are mutable.

    return list_strings

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#["HELLO", "WORLD", "how", "are", "you"]
#["HELLO", "WORLD", "HOW", "are", "you"]
print(alter_list(["hello", "WORLD", "HOW", "are", "you"], [0, 2]))
print(alter_list(["hello", "WORLD", "HOW", "are", "you"], [0, 2, 2]))

