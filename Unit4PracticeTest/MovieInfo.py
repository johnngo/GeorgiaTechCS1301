#Write a function called write_movie_info. write_movie_info
#will take as input two parameters: a string and a
#dictionary.
#
#The string will represent the filename to which to write.
#
#The keys in the dictionary will be strings representing
#movie titles. The values in the dictionary will be lists
#of strings representing performers in the corresponding
#movie.
#
#write_movie_info should write the list of movies to the file
#given by the filename using the following format:
#
# Title: Actor 1, Actor 2, Actor 3, etc.
#
#The movies and the actor names should be sorted
#alphabetically.
#
#So, for this dictionary:
#
# {"Chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"],
#  "Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"]}
#
#The file printed would look like this:
#
# Chocolat: Alfred Molina, Johnny Depp, Judi Dench, Juliette Binoche
# Skyfall: Daniel Craig, Javier Bardem, Judi Dench, Naomie Harris
#
#HINT: the keys() method of a Dictionary will return a list
#of the dictionary's keys. So, to get a sorted list of a_dict's
#keys, you could call key_list = a_dict.keys(), then call 
#key_list.sort().


#Write your function here!
def write_movie_info(file,dict):
    sortedMovies = {}  #empty dictionary
    f = open(file,'w') #open method assign to f
    keys = list(dict.keys()) # list method, returns the keys in a list
      #['Chocolat', 'Skyfall']
    keys.sort() # sort keys in list alphabetically
    for i in keys:
        
        sortedMovies[i] = sorted(dict[i]) # assigning sorted values alphabetically
      
    
    
    for i in sortedMovies:
        
        f.write(i+': ')
        for j in range(len(sortedMovies[i])): # looping through the range value 0,1,2,3
            
                     
            f.write(sortedMovies[i][j]) # write key title : actors to txt
            
            if j !=len(sortedMovies[i])-1: #if j =3, execute else line
                f.write(", ")
            else:
                f.write("\n")

        

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print nothing -- however, it should write the same contents
#as Sample.txt to Test.txt.
movies = {"Chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"], "Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"]}
write_movie_info("Test.txt", movies)


#You open the file that is given in the parameters and make sure you
#set the mode to "w".

def write_movie_info(string, dictionary):
    file = open(string, "w")

#We create a for each loop that will iterate through the dictionary
#However, we will do so when sorted. sorted(dictionary) puts the keys
#in order.

    for movie in sorted (dictionary):

#We write the movie into our file and add ": " because that is the way
#the problem wants us to format our dictionary

        file.write(movie + ": ")

#We then sort the actor names within the dictionary by writing:

        dictionary[movie].sort()

#We use .sort() because we want to have the actors in alphabetical order

#Create a for loop that will iterate through the list of actors
#from that particular movie. However, we iterate through till the second
#last actor because the last actor should not have a comma and add
#a new line.

        for i in range(0, len(dictionary[movie]) - 1):
            file.write(dictionary[movie][i] + ", ")
        file.write(dictionary[movie][len(dictionary[movie]) - 1] + "\n")

#Since we are now done iterating through the file, we close the file
#and return

    file.close()
    return