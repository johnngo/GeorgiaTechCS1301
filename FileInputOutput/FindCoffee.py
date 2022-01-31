#Write a function called "find_coffee" that expects a 
#filename as a parameter. The function should open the 
#given file and return True if the file contains the word 
#"coffee". Otherwise, the function should return False.
#
#Hint: look up the read() method if you want to do this
#more simply than you might do with readline().


#Write your function here!
def find_coffee(filename):
    inputFile = open(filename, "r")
    if "coffee" in inputFile.read():
        return True
    else:
        return False
    inputFile.close()

#You can test your function with the provided files named 
#"coffeeful.txt" and "coffeeless.txt". With their original
#text, the lines below should print True, then False. You
#may also edit the files by selecting them in the drop
#down in the top left to try your code with different
#input.
print(find_coffee("coffeeful.txt"))
print(find_coffee("coffeeless.txt"))



def find_coffee(filename):
    
    #First we open the file as usual. Note that if we don't
    #supply a read mode, Python assumes "read", so we don't
    #actually need to include the "r" in the call to
    #open() -- but we could.
    
	file_reader = open(filename)
    
    #Then we read the file into a variable called contents:
    
	contents = file_reader.read()
    
    #Then we check if "coffee" appears in that string:
    
	result = "coffee" in contents
    
    #Close the file...
    
	file_reader.close()
    
    #Then return the result!
    
	return result  

    #We could compress this a bit as well, but not down
    #to one line because we need to be able to close the
    #file.
print(find_coffee("coffeeful.txt"))
print(find_coffee("coffeeless.txt"))