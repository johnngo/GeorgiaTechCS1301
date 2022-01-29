#We've learned a lot in this chapter. Let's try to use a lot
#of it for one final exercise.
#
#Write a function called sort_artists. sort_artists will
#take as input a list of tuples. Each tuple will have two
#items: the first item will be a string holding an artist's
#name, and the second will be an integer representing their
#total album sales (in millions).
#
#Return a tuple of two lists. The first list in the
#resulting tuple should be all the artists sorted
#alphabetically. The second list should be all the revenues
#sorted in descending numerical order.
#
#For example:
# artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
# sort_artists(artists) -> (["Elvis Presley", "Michael Jackson", "The Beatles"], [270.8, 211.5, 183.9])
#
#Notice that artists is a list of tuples (brackets first,
#then parentheses), but sort_artists outputs a tuple of
#lists (parentheses first, then brackets).


#Write your function here!
def sort_artists(a_list):
    artist = []
    earnings = []
    z = (artist, earnings)
    for i in a_list:
        artist.append(i[0])
        earnings.append(i[1])
        artist.sort()
        earnings.sort(reverse=1)
    return z


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#(['Elvis Presley', 'Michael Jackson', 'The Beatles'], [270.8, 211.5, 183.9])  
artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
print(sort_artists(artists))


def sort_artists(artist_list):
    
    #To start, we know we're going to want to end up with
    #separate lists of artists and sales -- after all, that's
    #what we're returning. So, let's go ahead and create
    #those empty lists:
    
    artists = []
    sales = []
    
    #Now, we want to go through each artist in artist_list.
    #Each one will be a tuple where the first item is a name,
    #and the second is a float:
    
    for artist_tuple in artist_list:
        
        #Add the first item to the list of artists...
        
        artists.append(artist_tuple[0])
        
        #...and the second item to the list of sales:
        
        sales.append(artist_tuple[1])
    
    #At this point, artists is a list of all the artist names
    #in the order of the original tuples, and sales is a list
    #of the sales numbers in that order, too. Next, we want
    #to sort them.
    #
    #Names should be sorted alphabetically:
    
    artists.sort()
    
    #Sales should be sorted in descending order. We can do that
    #by sorting them, then reversing the order:
    sales.sort()
    sales.reverse()
    
    #Finally, we return a tuple with the sorted artist list as
    #the first item, and the sorted sales list as the second
    #item:
    
    return (artists, sales)


artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
print(sort_artists(artists))