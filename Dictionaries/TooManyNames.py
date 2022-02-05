#Write a function called name_counts. name_counts will take
#as input a list of full names. Each name will be two words
#separated by a space, like "David Joyner".
#
#The function should return a dictionary. The keys to the
#dictionary will be the first names from the list, and the
#values should be the number of times that first name
#appeared.
#
#HINT: Use split() to split names into first and last.


#Add your function here!
def name_counts(names):
    dict ={}
    for item in names:
        item = item.split()        
        if item[0] in dict:
            dict[item[0]] +=1
        else:
            dict[item[0]] = 1
    return dict
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'Shelba': 5, 'Maren': 1, 'Nicol': 1, 'David': 2, 'Brenton': 2}
name_list = ["David Joyner", "David Zuber", "Brenton Joyner",
             "Brenton Zuber", "Nicol Barthel", "Shelba Barthel",
             "Shelba Crowley", "Shelba Fernald", "Shelba Odle",
             "Shelba Fry", "Maren Fry"]
print(name_counts(name_list))

#First we define the function:
def name_counts(names):
    
    #We will want to eventually return a dictionary of
    #name-count pairs, so let's create an empty dictionary
    #to populate over time:
    name_dict = {}
    
    #Now, we iterate through each name in the list:
    for name in names:
        
        #The names are first-last pairs like "David Joyner",
        #but we only care about the first name. So, we split
        #the current name:
        split_name = name.split()
        
        #Then pull out the first name, which is at index 0:
        first_name = split_name[0]
        
        #We could also pull out both first and last name with
        #first_name, last_name = split_name
        #
        #That way, we could ignore the index.
        
        #Next, we want to check if we've already added this
        #name to the dictionary:
        if not first_name in name_dict:
            
            #If not, we can't increment it yet! We need to
            #add it first. So, we create a new key in the
            #dictionary for first_name and set its value to
            #0:
            name_dict[first_name] = 0
            
        #Now, we know that name_dict[first_name] exists
        #because if it didn't on line 27, we created it. So,
        #we can feel safe incrementing it:
        name_dict[first_name] += 1
    
    
    #When we're done, we return the dictionary:
    return name_dict



name_list = ["David Joyner", "David Zuber", "Brenton Joyner",
             "Brenton Zuber", "Nicol Barthel", "Shelba Barthel",
             "Shelba Crowley", "Shelba Fernald", "Shelba Odle",
             "Shelba Fry", "Maren Fry"]
print(name_counts(name_list))
