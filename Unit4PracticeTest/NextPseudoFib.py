#Write a function called next_fib. next_fib should take
#have two parameters: a list of integers and a single integer.
#For this description, we'll call the single integer n.
#
#next_fib should modify the list to add the next n pseudo-
#Fibonacci numbers to the end of the sequence. A pseudo-
#Fibonacci number is the sum of the previous two numbers in
#the sequence, but in our case, the previous two numbers may
#not be the original numbers from the Fibonacci sequence.
#
#For example, if the original list given was:
#
# a_list = [5, 5, 10, 15, 25, 40, 65]
#
# Then next_fib(a_list, 3) would return:
#       [5, 5, 10, 15, 25, 40, 65, 105, 170, 275]
#
#All the original numbers in the list are still there, and
#three new ones have been added.
#
#You may assume the list parameter will always have at least
#two numbers.
#
#HINT: Python gets mad if you try to change a list while
#iterating over it with a for-each loop. You'll have to get
#clever with a for or while loop to do this!


#Add your code here!
def next_fib(int_list, a_single_int):
    list = []
    for i in int_list:
        list.append(i)
    for i in range(a_single_int):
        add=list[-1] + list[-2]
        list.append(add)
    return list

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#[5, 5, 10, 15, 25, 40, 65, 105, 170, 275] 
a_list = [5, 5, 10, 15, 25, 40, 65]
print(next_fib(a_list, 3))

#We create a counter so that we stop when we are at
#the number of extra fibonacci numbers we were asked to find

def next_fib(list_int, num):
    count = 0
    while (count < num):

#We know that the next number will be the sum of the last two
#numbers of the sequence, so we access them through indexes

        next_num = list_int[len(list_int) - 1] + list_int[len(list_int) - 2]

#To clarify, the reason why len(list_int) - 1 is the last number
#is because the last index is one less than the length of the
#actual list since indexing starts from 0
#
#Since we now have the next number stored, we append it to the list.

        list_int.append(next_num)

#We increment count so that we stop after creating 'num' number
#of fibonacci numbers

        count += 1

#Once done, we return the updated list of integers.

    return list_int

#Side note: We are able to return the same list as the one
#that was inputted because list are mutable, which means that
#once we edit them, their values are changed. This was unlike
#with strings, which are immutable.
