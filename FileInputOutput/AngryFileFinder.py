def angry_file_finder(filename):
  inputfile = open(filename, "r")
  for line in inputfile:
    lineTest = inputfile.readline()
    if "!" in lineTest:
      return True
    else:
      return False
  file.close()

print(angry_file_finder("AngryFileFinderInput.txt"))

def angry_file_finder(filename):
    
    #There are a couple ways to do this, but they're slight
    #variations of the same overall pattern. There are also
    #more dramatically different approaches, but this one
    #is probably the most efficient.
    #
    #First, we open the file:
    
    file_reader = open(filename)
    
    #Next, we need to iterate over the lines in the file.
    #We could either get all the lines using
    #file_reader.readlines() and iterate over that list,
    #or we can use our loop syntax, which does the same
    #thing. Let's use the latter:
    
    for line in file_reader:
        
        #This will look at each line in the file one-by-one.
        #Now, we want to check to see if an exclamation
        #point is on this line -- or, specifically, we want
        #to check if it's *not* on this line:
        
        if not "!" in line:
            
            #We want to return False if there is a line of
            #this file without an exclamation point. If
            #there is no ! on this line, then we already
            #know to return False. So, let's go ahead and
            #do that, after closing the file:
            
            file_reader.close()
            return False
        
    #If that loop runs to completion without ever reaching
    #line 34, it means that every line had an exclamation
    #point. If that's the case, then we want to close the
    #file, then return True:
    
    file_reader.close()
    return True
        
    
    
print(angry_file_finder("AngryFileFinderInput.txt"))
