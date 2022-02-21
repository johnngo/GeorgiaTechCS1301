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

games = list(reader)[1:] #puts data in a list


dates = [] # empty list to prepare list of dates
for game in games:
   
    dates.append(game[0]) # append column 1 into a list

dates.sort()
first = dates[0]
print(first)
if game[0] == first:
    print("First Team " + game[1])


#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.
print(games[0:2])

#Q2, how many points has Georgia Tech scored all-time against Auburn
points = 0
for game in games:
    if game[1] == "Auburn":
        points += int(game[3])
print(points)

#Q3, how many points has Auburn scored all time against Georgia Tech?
points = 0
for game in games:
    if game[1] == "Auburn":
        points += int(game[4])
print(points)
#Q4, GT all time record in home games
wins = 0
ties = 0
losses = 0
points = 0
for game in games:
    if game[2] == "Home":
        points +=int(game[3])
        if int(game[3]) > int(game[4]):
            wins += 1
        if int(game[3]) == int(game[4]):
            ties += 1
        if int(game[3]) < int(game[4]):
            losses += 1
print("Q4 Records in  homes: " + str(points))
print("\twins:" + str(wins))
print("\tties: "+str(ties))
print("\tlosses: "+str(losses))

#Q5, all games played in 2009,
wins = 0
ties = 0
losses = 0
points = 0
for game in games:
    d=game[0]
    y=int(d.split("-")[0]) # the year is at index 0
    if y == 2009:
        points +=int(game[3])
        if int(game[3]) > int(game[4]):
            wins += 1
        if int(game[3]) == int(game[4]):
            ties += 1
        if int(game[3]) < int(game[4]):
            losses += 1
print("Q5 Records in  2009: " + str(points))
print("\twins:" + str(wins))
print("\tties: "+str(ties))
print("\tlosses: "+str(losses))

#Q6, records in October
wins = 0
ties = 0
losses = 0
points = 0
for game in games:
    d=game[0]
    m=int(d.split('-')[1])
   
    if m == 10:
        points += int(game[3])
        if int(game[3]) > int(game[4]):
            wins += 1
        if int(game[3]) == int(game[4]):
            ties += 1
        if int(game[3]) < int(game[4]):
            losses += 1

print("Q6 Records in 0ctober: "+str(points))
print("\twins: "+str(wins))
print("\tties: "+str(ties))
print("\tloses: "+str(losses))
