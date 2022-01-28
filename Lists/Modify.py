#Write a function called modify_list. modify_list will
#take one parameter, a list. It should then modify the
#list in the following ways, in this order:
#
# - Sort the list (using the default sort method).
# - Reverse the order of the list.
# - Delete the last three items of the list.
# - Removes one instance the integer 7 from the list, if
#   it's present.
# - Double the values of the first and third items in
#   the list.
#
#It should then return the resulting list. You may assume
#the list will start with at least six items.
#
#Hint: Remember Python is 0-indexed. The second item
#does not have an index of 2.
#
#Hint 2: Remember, the list.remove() function removes items
#by value, not by index. Note also that if the item you're
#trying to remove is not found in the list, remove() will
#throw an error: so, you'll want to avoid that one way or
#another!


#Write your code here!
def modify_list(a_list):
    a_list.sort()
    a_list.reverse()
    del a_list[-3:]
    for i in a_list:
        if i == 7:
            a_list.remove(7)
    a_list[0] *= 2
    a_list[2] *= 2
    return a_list
    

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#[178, 81, 75.0, 4, 3.141592653589793, 3]
import math
print(modify_list([7, 4, 3, 2.0, 81, 37.5, 89, math.pi, -2, math.e]))

def modify_list(a_list):
    
    #In this problem, we're asked to perform a series of
    #random operations to show that we know how to work with
    #lists. Some are relatively straightforward:
    
    a_list.sort()
    a_list.reverse()
    
    #Notice, however, that unlike strings, we don't need to
    #set a_list equal to the result of these operations.
    #Whereas a_string.upper() would not modify the value of
    #a_string, a_list.sort() *does* modify the value of
    #a_list. That's because lists are mutable, but strings
    #are immutable.
    #
    #Don't worry if that's a little confusing, you'll get
    #used to it! It's weird that the exact same syntax
    #gives different results, but that's because Python
    #treats lists and strings differently.
    #
    #To delete the last three items, we use the del operator
    #along with the slice of a_list holding the last three
    #items:
    
    del a_list[-3:]
    
    #If you weren't sure how to do this with slicing, you
    #could have also run del a_list[-1], del a_list[-2], and
    #del a_list[-3].
    #
    #Next, we need to remove 7 if it occurs. The remove()
    #method removes by value, so we call a_list.remove(7)...
    #but that will cause an error if 7 isn't in a_list. So,
    #let's check to see if it's there first, and only call
    #remove(7) if it is:
    
    if 7 in a_list:
        a_list.remove(7)
    
    #Finally, we modify the values of the first and third
    #items in place -- those are the items at indices 0 and
    #2:
    
    a_list[0] *= 2
    a_list[2] *= 2
    
    #And finally we return the result:
    
    return a_list
    
    #Note that we actually don't *need* to return the result
    #in most cases. Lists are mutable, so if we print the
    #value of the list after calling modify_list, its value
    #will be changed even if we didn't return the result.
    #In our work, we'll generally return the list because
    #that allows our autograders to keep separate copies of
    #the variable: the correct result and your result.


import math
print(modify_list([7, 4, 3, 2.0, 81, 37.5, 89, math.pi, -2, math.e]))