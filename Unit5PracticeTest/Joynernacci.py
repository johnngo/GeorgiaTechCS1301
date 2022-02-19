#Remember that Fibonacci's sequence is a sequence of numbers
#where every number is the sum of the previous two numbers.
#
#Joynernacci numbers are similar to Fibonacci numbers, but
#with two differences:
#
# - Fibonacci numbers are famous, Joynernacci numbers are
#   not (yet).
# - In Joynernacci numbers, even-indexed numbers are the
#   sum of the previous two numbers, while odd-indexed
#   numbers are the absolute value of the difference
#   between the previous two numbers.
#
#For example: the Joynernacci sequence starts with 1 and 1
#as the numbers at index 1 and 2. 3 is an odd index, so
#the third number would be 0 (1 - 1 = 0). 4 is an even
#index, so the fourth number would be 1 (0 + 1). 5 is an
#odd index, so the fifth number would be 1 (1 - 0). And
#so on.
#
#The first several Joynernacci numbers (and their indices)
#are thus:
#
# 1  1  0  1  1  2  1  3  2  5  3  8  5 13  8 21 13 34 21
# 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
#
#Write a function called joynernacci that returns the nth
#Joynernacci number. For example:
#
# joynernacci(5) -> 1
# joynernacci(12) -> 8
#
#We recommend implementing joynernacci recursively, but it
#is not required.


#Write your code here!
def joynernacci(n):
   if n == 1:
       return 1
   elif n == 2:   
       return 1            
   elif n % 2 == 1:
       return joynernacci(n -1) - joynernacci(n -2)
   elif n % 2 == 0:
       return joynernacci(n -1) + joynernacci(n -2) 

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 1, then 8

print(joynernacci(5))
print(joynernacci(12))


#This problem should be solved recursively
#We create the function and we keep in mind that the input
#will be the index.
#We know that the first two numbers are 1 so our base case
#for our recursion will just return 1

def joynernacci(index):
    if index <= 2:
        return 1

#Now that we have finished our base case, now we have to think
#of how to recursively get to our base case.
#Depending on the index, we have to call the function recursively
#differently. if the index is an odd number, we have to find
#the absolute value of the difference between the last two numbers
#However, if the index is an even number, we have to add the last
#two numbers. Therefore, we check to see if the current index we
#are working with is an odd or even and call the function recursively
#respectively.

    elif index % 2 == 0:
        return joynernacci(index -1) + joynernacci(index - 2)
    else:
        return abs(joynernacci(index-1) - joynernacci(index - 2))

#Since it is difficult to verbalize the thought process of recursion
#if you have trouble understanding the concept of why I did it, below
#is step-by-step process of how joynernacci(5) returns 1
#I'm going to use joy because it's shorter.
#joy(5) (is called)
#	index = 5 (index is an odd number so it goes to the else block)
#	return abs(joy(5-1) - joy(5-2))
#		We cannot return anything yet since we do not know the values
#		of joy(5-1) and joy(5-2)
#		joy(5-1) (is called)
#			index = 4 (index is an even number so elif block)
#			return joy(4-1) + joy(4-2)
#				We cannot return anything yet again since we
#				don't know joy(4-1) and joy(4-2)
#				joy(3) (is called)
#					index = 3 (index is odd)
#					return abs(joy(3-1) - joy(3-2))
#						joy(2) (is called)
#						returns 1 (because base case)
#						joy(1) (is called)
#						returns 1 (because base case)
#					Notice that the order matters. joy(3-1) is
#					called before joy(3-2). Since joy(2) and joy(1)
#					return a value now we know abs(joy(2)-joy(1))
#					It returns 0
#				returned 0
#				Now we have to find joy(4-2)since a value is returned
#				joy(2) (is called)
#					returns 1
#				returned 1
#			Now we know joy(4-1) and joy(4-2). We add them together and
#			return 1 (0 + 1)
#		Now we know joy(5-1) is equal to 1
#		We continue the same process with joy(5-2)....

