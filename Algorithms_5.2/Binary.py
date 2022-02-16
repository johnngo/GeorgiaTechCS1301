#Recall in Worked Example 5.2.5 that we showed you the code
#for two versions of binary_search: one using recursion, one
#using loops. For this problem, use the recursive one.
#
#In this problem, we want to implement a new version of
#binary_search, called binary_search_year. binary_search_year
#will take in two parameters: a list of instances of Date,
#and a year as an integer. It will return True if any date
#in the list occurred within that year, False if not.
#
#For example, imagine if listOfDates had three instances of
#date: one for January 1st 2016, one for January 1st 2017,
#and one for January 1st 2018. Then:
#
#  binary_search_year(listOfDates, 2016) -> True
#  binary_search_year(listOfDates, 2015) -> False
#
#You should not assume that the list is pre-sorted, but you
#should know that the sort() method works on lists of dates.
#
#Instances of the Date class have three attributes: year,
#month, and day. You can access them directly, you don't
#have to use getters (e.g. myDate.month will access the
#month of myDate).
#
#You may copy the code from Worked Example 5.2.5 and modify
#it instead of starting from scratch. You must implement
#binary_search_year recursively.
#
#Don't move this line:
from datetime import date


#Write your code here!
def binary_search_year(lst, y):
    lst.sort()
    if len(lst) == 0:
        return False
    mid = len(lst)//2
    if lst[mid].year == y:
        return True
    else:
        if y < lst[mid].year:
            return binary_search_year(lst[:mid], y)
        elif y > lst[mid].year:
            return binary_search_year(lst[mid+1:], y)
        
        
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, then False
listOfDates = [date(2016, 11, 26), date(2014, 11, 29), 
               date(2008, 11, 29), date(2000, 11, 25), 
               date(1999, 11, 27), date(1998, 11, 28), 
               date(1990, 12, 1), date(1989, 12, 2), 
               date(1985, 11, 30)]

print(binary_search_year(listOfDates, 2016))
print(binary_search_year(listOfDates, 2007))


from datetime import date

#Most of our code is identical to the worked example:
#everything until the next comment is unchanged except
#the name of the function.
def binary_search_year(searchList, searchTerm):

    searchList.sort()
    
    if len(searchList) == 0:
        return False

    middle = len(searchList) // 2

    #All we have to do is check not if the current middle
    #term is equal to the search term, but rather if its
    #year attribute is equal to the search year:
    if searchList[middle].year == searchTerm:
        return True

    #We also need to change the comparison to compare the
    #year to the search term.
    elif searchTerm < searchList[middle].year:
        return binary_search_year(searchList[:middle], searchTerm)

    
    else:
        return binary_search_year(searchList[middle + 1:], searchTerm)

listOfDates = [date(2016, 11, 26), date(2014, 11, 29), 
               date(2008, 11, 29), date(2000, 11, 25), 
               date(1999, 11, 27), date(1998, 11, 28), 
               date(1990, 12, 1), date(1989, 12, 2), 
               date(1985, 11, 30)]

print(binary_search_year(listOfDates, 2016))
print(binary_search_year(listOfDates, 2007))
