#Write a function called "load_file" that accepts one 
#parameter: a filename. The function should open the
#file and return the contents.#
#
# - If the contents of the file can be interpreted as
#   an integer, return the contents as an integer.
# - Otherwise, if the contents of the file can be
#   interpreted as a float, return the contents as a
#   float.
# - Otherwise, return the contents of the file as a
#   string.
#
#You may assume that the file has only one line.
#
#Hints:
#
# - Don't forget to close the file when you're done!
# - Remember, anything you read from a file is
#   initially interpreted as a string.


#Write your function here!
def load_file(filename):
    inputFile = open(filename,"r")
    contents = inputFile.read()
    inputFile.close()
    if "." in contents:
        try:
            flt_content = float(contents)
            return flt_content
        except:
            return contents
    else:
        try:
            int_content = int(contents)
            return int_content
        except:
            return contents


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 123, followed by <class 'int'>.
contents = load_file("LoadFromFileInput.txt")
print(contents)
print(type(contents))


#This is going to look complex, but it's simpler than it
#looks! We'll take two slightly different approaches.

def load_file(filename):
    
    #First, we need to open the file:
    
    file_reader = open(filename, "r")
    
    #Next, we need to read its contents. Because the
    #directions say that there will only be one line, it
    #actually doesn't matter if we use read() or
    #readline(). We'll use readline().
    
    contents = file_reader.readline()
    
    #Notice that we don't bother stripping the \n off
    #the end of the contents: our type conversion
    #functions do that automatically.
    
    try:
        
        #Now, we want to try to convert it to an integer.
        #If contents can be read as an integer, this line
        #will work, and the function is over*. If this
        #line doesn't work, an error will arise.
        
        return int(contents)
    
    except:
        
        #If we reach this point, an error arose. So, the
        #contents can't be read as an integer. Now let's
        #try to read them as a float:
        
        try:
            
            #If this line works, then contents was a float
            #and the function is over*. If not, it will
            #generate an error.
            
            return float(contents)
        
        except:
            
            #If we reach here, then we encountered an
            #error converting contents to both an int and
            #a float. So, there's nothing left to do but
            #just return the original contents of the file
            #as a string, then the function is over*.
            
            return contents
    
    #See those asterisks where I wrote 'over'? That's
    #because this is a great demonstration of when we might
    #use a finally block. The contents of a finally block
    #after a try-except block will always run no matter what
    #happened inside the try-except blocks. So, since we
    #always need to close the file, we can do that in a
    #finally block:
    
    finally:
        file_reader.close()
        
    #sample_answer_2.py gives another example of how to solve
    #this: it's a little less elegant, but maybe simpler to
    #understand if this was confusing.



contents = load_file("LoadFromFileInput.txt")
print(contents)
print(type(contents))

#If the previous sample answer was confusing, here's
#another one. This one tries to ditch the nested
#try-except structure. It isn't as elegant, but it
#may be easier to follow.

def load_file(filename):
    
    #First, we still need to open the file:
    
    file_reader = open(filename, "r")
    
    #Next, we still need to read its contents:
    
    contents = file_reader.readline()
    
    #With the approach we're going to take, we're going to
    #have multiple try-except blocks that aren't nested.
    #So, we won't know when to close the file. However, we
    #already read the file's contents and stored it to the
    #variable contents, so let's go ahead and close it!
    
    file_reader.close()
    
    try:
        
        #Again, we'll try to conver it to an integer. If
        #this line works, the function is over.
        
        return int(contents)
    
    except:
        
        #What do we do here? Well, we know it's not an
        #integer, but we don't know if it's a float or a
        #string. So, let's do nothing for now.
        
        pass
    
    try:
        
        #Now let's check for floats:
        
        return float(contents)
    
    except:
        
        #If an error occurred that time, we know it's
        #neither an int or a float, so it must be a
        #string:
        
        return contents
    
    #This logic is the same as the other example, except
    #that we're closing the file immediately after reading
    #it so that we don't have to bother with the finally
    #block, and we're using the knowledge that a return
    #will kill the function to avoid a nested try-except
    #structure.


contents = load_file("LoadFromFileInput.txt")
print(contents)
print(type(contents))

