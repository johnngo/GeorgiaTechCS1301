#Remember that Fibonacci's sequence is a sequence of numbers
#where every number is the sum of the previous two numbers.
#
#For this problem, implement Fibonacci recursively, with a
#twist! Imagine that we want to create a new number sequence
#called Fibonacci-3. In Fibonacci-3, each number in the
#sequence is the sum of the previous three numbers. The
#sequence will start with three 1s, so the fourth Fibonacci-3
#number would be 3 (1+1+1), the fifth would be 5 (1+1+3),
#the sixth would be 9 (1+3+5), the seventh would be 17
#(3+5+9), etc.
#
#Name your function fib3, and make sure to use recursion.


#Write your code here!
def fib3(fib_number):
    if fib_number <= 3:
        return 1
    else:
        return fib3(fib_number -1) + fib3(fib_number -2) + fib3(fib_number -3)

#The lines below will test your code. If your funciton is
#correct, they will print 1, 3, 17, and 57.
print(fib3(3))
print(fib3(4))
print(fib3(7))
print(fib3(9))


#This problem can be hard to think about, but it's a good
#example of how elegant the solutions to recursion problems
#often are.
#
#First, we define the function:
def fib3(n):
    
    #If n is our base case, we return 1. Our base case is
    #that if n is 1, 2, or 3, then the corresponding Fib3
    #number is 1:
    if n in [1, 2, 3]:
        return 1
    
    #Otherwise, we return the sum of the previous three
    #numbers:
    else:
        return fib3(n-1) + fib3(n-2) + fib3(n-3)
    
    #That will keep recursing until we ultimately call
    #fib3(3) + fib3(2) + fib3(1), which would return
    #1 + 1 + 1 because those are all three base cases.
    #From there, the answer flows back up the chain.
    
    
print(fib3(3))
print(fib3(4))
print(fib3(7))
print(fib3(30))

