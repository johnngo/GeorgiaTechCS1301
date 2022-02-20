#This question is best if you solve it recursively
#
#Your first thought process (if you were planning on solving this recursively)
#should have been to ask yourself what the base case should be.
#From reading the instructions, you should gather that the base case should
#be when the string passed in the rabbit_hole function does not exist in the
#dictionary, since then is when our rabbit hole finishes.
#
#Ignore the try block for now!

def rabbit_hole (dictionary, string):
    try:
        if string not in dictionary:
            return string

#If the string passed in is a key in the dictionary, then we need to
#find out what the key's value value. Thus we pass in recursively the
#key's value to find out the key's value value.

        else:
            return rabbit_hole(dictionary, dictionary[string])

#However, we run into an edge case where there might be an infinite loop
#of the key and the key's value value are the same. Like the rat and ram 
#case. Thus we need to have a try except block so that we can catch those
#exceptions and simply return False

    except:
        return False

 #Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: ant, hen, doe, yak, False, each on their own line.
d = {"bat": "pig", "pig": "cat", "cat": "dog", "dog": "ant",
     "cow": "bee", "bee": "elk", "elk": "fly", "ewe": "cod",
     "cod": "hen", "hog": "fox", "fox": "jay", "jay": "doe",
     "rat": "ram", "ram": "rat"}

print(rabbit_hole(d, "bat"))
print(rabbit_hole(d, "ewe"))
print(rabbit_hole(d, "jay"))
print(rabbit_hole(d, "yak"))
print(rabbit_hole(d, "rat"))       