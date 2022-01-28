#Write a function called unpack_and_reverse that will
#accept one parameter, a tuple with at least three items.
#The function should return a new tuple with only the first
#three items, but listed in reverse order.
#
#For example:
#
# a_tuple = ("a", "b", "c", "d", "e")
# unpack_and_reverse(a_tuple) -> ("c", "b", "a")
#
#However, to do this, you should not access any value in
#the tuple directly (e.g. with a_tuple[1]). Instead, you
#should use tuple unpacking to unpack them into variables.
#You also should not touch any items past the third item
#in the tuple: use tuple slicing instead to only access
#the first three.


#Write your function here!
def unpack_and_reverse(a_tuple):
    return a_tuple[:3][::-1]


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#('c', 'b', 'a')
#('h', 'g', 'f')
#('k', 'j', 'i')
print(unpack_and_reverse(("a", "b", "c", "d", "e")))
print(unpack_and_reverse(("f", "g", "h")))
print(unpack_and_reverse(("i", "j", "k", "l", "m", "n", "o", "p", "q", "r")))

def unpack_and_reverse(a_tuple):
    
    #Here, first we want to unpack the tuple into three
    #variables for us to use in the next tuple. However,
    #we were told not to do this by accessing the elements
    #by index, and we were told not to access any items
    #later than item #3. So, how can we accomplish both?
    #
    #Here's how:
    
    item1, item2, item3 = a_tuple[0:3]
    
    #We create three variables on the left, separate them
    #with commas, and set them equal to the tuple. This will
    #unpack the tuple into these three variables. However,
    #this would fail if the tuple had more than three
    #items... unless we slice off any later items. By
    #setting these variables equal to a_tuple[0:3], we only
    #get the first three items in a_tuple.
    #
    #Then, we need to create and return a tuple with these
    #three items, but in reverse order:
    
    return (item3, item2, item1)



print(unpack_and_reverse(("a", "b", "c", "d", "e")))
print(unpack_and_reverse(("f", "g", "h")))
print(unpack_and_reverse(("i", "j", "k", "l", "m", "n", "o", "p", "q", "r")))
