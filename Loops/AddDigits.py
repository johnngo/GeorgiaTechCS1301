a_string = "F12dav^f%$25d"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#a_string is a string of random characters. Write some code
#that adds all the digits that appear in the string and prints
#their sum.
#
#For example, the digits in the string above are 1, 2, 2, and 5,
#so your code would print 10.
#
#Remember, you can iterate over each character in a string with
#this syntax:
#
#for a_character in a_string:
#
#Remember also, you can check if a character is in a list of other
#characters within this syntax:
#
#if a_character in "ABCDEFG":
#
#If there are no digits in the string, print 0.


#Add your code here!
sum = 0
for i in a_string:
    for j in i:
        if j == "1":
            sum +=1
        elif j =="2":
            sum +=2
        elif j =="3":
            sum +=3
        elif j =="4":
            sum +=4
        elif j =="5":
            sum +=5
        elif j =="6":
            sum +=6
        elif j =="7":
            sum +=7
        elif j =="8":
            sum +=8
        elif j =="9":
            sum +=9
print(sum)
