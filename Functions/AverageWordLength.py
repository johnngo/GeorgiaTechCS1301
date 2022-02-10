#-----------------------------------------------------------
#In this problem, you should write three functions:
#word_count, letter_count, and average_word_length.
#
#word_count should take as input a string. It should return
#the number of words in the string. You may assume that the
#number of words in the string will be one more than the
#number of spaces in the string.
#
#letter_count should take as input a string. It should return
#the number of letters in the string. You may assume that
#the string is only letters and spaces: no punctuation or
#numbers.
#
#average_word_length should take as input a string. It should
#return the average length of the words in the string. You
#can find the average length by dividing the number of letters
#by the number of words.
#
#Your implementation for average_word_length *must* call
#word_count and letter_count.


#Add your code here!
def word_count(a_string):
    count =0
    word = a_string.split()
  
    for i in word:
        count += 1

    return count

def letter_count(a_string):
    count = 0
    for i in a_string:
        if i !=" ":
        
            count +=1

    return count

def average_word_length(a_string):
    word = word_count(a_string)
    letter = letter_count(a_string)
    return letter/word
                   


#Below are some lines of code that will test your function.
#You can change the value of the variable to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 3.5
a_string = "Up with the white and gold"

print(average_word_length(a_string))


#-----------------------------------------------------------
#First, let's start with letter count. There are a few ways
#we could implement letter count, but because we know our
#string is only spaces and letters, we can do this an easy
#way.
#
#First, we create the function:
def letter_count(a_string):
    
    #Then, start the counter:
    letters = 0
    
    #Then, we loop through each letter in the function:
    for character in a_string:
        
        #If it's not a space, then it must be a letter!
        if not character == " ":
            letters += 1
            
    #Finally, we return how many letters we found.
    return letters

#word_count is the exact opposite. Instead of counting the
#characters that are not spaces, we only want to count the
#spaces:
def word_count(a_string):
    
    #Here, we'll initialize our initial count to 1 because
    #each space starts a new word -- that means we have one
    #word to begin with.
    words = 1
    
    #Now, same loop:
    for character in a_string:
        
        #But opposite condition:
        if character == " ":
            words += 1
            
    return words

#With those two functions, our word length function is simple.
#We divide the results of letter_count by the results of
#word_count.
def average_word_length(a_string):
    return letter_count(a_string) / word_count(a_string)



a_string = "Up with the white and gold"

print(average_word_length(a_string))
