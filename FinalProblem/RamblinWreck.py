#Last problem, you wrote a function that generated the all-
#time win-loss-tie record for Georgia Tech against any other
#team.
#
#That dataset had a lot of other information in it. Let's
#use it to answer some more questions. As a reminder, the
#data will be a CSV file, meaning that each line will be a
#comma-separated list of values. Each line will describe one
#game.
#
#The columns, from left-to-right, are:
#
# - Date: the date of the game, in Year-Month-Day format.
# - Opponent: the name of the opposing team
# - Location: Home, Away, or Neutral
# - Points For: Points scored by Georgia Tech
# - Points Against: Points scored by the opponent

import csv # helps to read a csv data
#This line will open the file:
record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')

reader = csv.reader(record_file)

games = list(reader) #puts data in a list


dates = [] # empty list to prepare list of dates
for game in games:
   
    dates.append(game[0]) # append column 1 into a list

dates.sort()
first = dates[0]
print(first)
if game[0] == first:
    print("first team " + game[1])
#Q1. Who was the first team Georgia Tech ever played against? Auburn



#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.
