#Write a function called sum_lists. sum_lists should take
#one parameter, which will be a list of lists of integers.
#sum_lists should return the sum of adding every number from
#every list.
#
#For example:
#
# list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# sum_list(list_of_lists) -> 67


#Add your code here!
def sum_lists(list):
    total = 0
    for i in list:
        sum = 0
        for j in i:
            sum +=j
        total +=sum
    return total


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 78
list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(sum_lists(list_of_lists))


#First, we define the function:
def sum_lists(list_of_lists):
    
    #We know that we want to calculate a running total, so
    #we probably want to create a variable for our total
    #and start it at 0:
    total = 0
    
    #Now, we want to go through each list in the list of
    #lists...
    for a_list in list_of_lists:
        
        #And within each list, we want to go through each
        #item...
        for item in a_list:
            
            #And then we want to add that item to our
            #running total:
            total += item
            
    #Then, *after* we've gone through every item in every
    #list (so outside either loop), we return the result:
    return total



list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(sum_lists(list_of_lists))

