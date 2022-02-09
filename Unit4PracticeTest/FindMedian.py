#We open the file from the parameter and store it into a variable.

def find_median(fileName):
    file = open(fileName)

#We create an empty list where we will store integers into the list
#as currently, the file has a list of numbers which are in strings
#so it becomes difficult to sort them numerically.

    num = []
    for i in file:
        num.append(int(i))
    num.sort()

#Now, .sort() will correctly order the numbers. When using .sort()
#with strings 16 will come before 6 since the first digit is 1 for
#16 while 6 for 6
#
#Next we check to see if the length of the list is an odd number
#if so, we return the middle index. If even length, we find
#the average of the two middle numbers.
    print(len(num))
    if (len(num) % 2 == 1):
      
        return num[int(len(num) / 2)]
    else:
        return (num[int(len(num) / 2)] + num[int(len(num) / 2) - 1]) / 2

#The long line of code is simply writing the indexes. Try to write the
#math down if you don't understand why those indexes are needed. In short,
#if a list is length 7, we need the 3rd index because indexing starts at 0

