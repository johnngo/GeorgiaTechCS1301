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

#This line will open the file:
record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')


#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.
record = record_file.read().split("\n")[1:]
statistics = {}
for game in record:
    row = game.split(",")
   # print(row)
    opponent_name = row[1]
    row[3], row[4] = int(row[3]), int(row[4])
    if opponent_name not in statistics.keys():
        statistics[opponent_name] = {
                                     'games':[],
                                     'total wins':0,
                                     'home wins': 0,
                                     'away wins': 0,
                                     'neutral wins': 0,
                                     'total losses': 0,
                                     'home losses': 0,
                                     'away losses': 0,
                                     'neutral losses': 0,
                                     'total ties': 0,
                                     'home ties': 0,
                                     'away ties': 0,
                                     'neutral ties': 0,
                                     'points for': 0,
                                     'points against': 0
                                        }
    opponent_info = statistics[opponent_name]
    if row[3] > row[4]:
        opponent_info['total wins'] += 1
        row.append('win')
        if row[2] == 'Home':
            opponent_info['home wins'] += 1
        elif row[2] == 'Away':
            opponent_info['away wins'] += 1
        else:
            opponent_info['neutral wins'] += 1
    elif row[3] == row[4]:
        opponent_info['total ties'] += 1
        row.append('tie')
        if row[2] == 'Home':
            opponent_info['home ties'] += 1
        elif row[2] == 'Away':
            opponent_info['away ties'] += 1
        else:
            opponent_info['neutral ties'] += 1
    else:
        opponent_info['total losses'] += 1
        row.append('loss')
        if row[2] == 'Home':
            opponent_info['home losses'] += 1
        elif row[2] == 'Away':
            opponent_info['away losses'] += 1
        else:
            opponent_info['neutral losses'] += 1
    opponent_info['points for'] += row[3]
    opponent_info['points against'] += row[4]
    statistics[opponent_name]['games'].append(row)