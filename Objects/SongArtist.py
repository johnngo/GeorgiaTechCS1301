class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label

class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist
        

#The key trick here is that we want to use the same instance of
#artist in both song_1 and song_2. The easiest way to do that is
#going to be to create our artists separately from our songs, then
#pass them in as arguments. So, first we create our artists...
        
artist_1 = Artist("Taylor Swift", "Big Machine Records, LLC")
artist_2 = Artist("LiGHTS", "Warner Bros. Records Inc.")

#Then we create our songs using the right instances of artist as
#the fourth argument:

song_1 = Song("You Belong With Me", "Fearless", 2008, artist_1)
song_2 = Song("All Too Well", "Red", 2012, artist_1)
song_3 = Song("Up We Go", "Midnight Machines", 2016, artist_2)

#There are other ways we could have done this. For example, we could
#have created the artist inside the Song constructor on line 25, but
#then used song_1's artist as the argument for song_2, like this:
#
#song_2 = Song("All Too Well", "Red", 2012, song_1.artist)
