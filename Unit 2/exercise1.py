import pandas as pd
import nfl_data_py as nfl 

#schedules = nfl.import_schedules([2024])

from helperFunctions import get_team_records, get_season_Results_By_team

#print(schedules.colums.tolist())

records =get_team_records(2025)

#birds = get_season_Results_By_team(2025, 'PHI')
#print(birds)

top6_Teams = ['TB','IND','LA','BUF','SF','SEA']

team1 =get_season_Results_By_team(2025,'TB')
team2 =get_season_Results_By_team(2025,'IND')
team3 =get_season_Results_By_team(2025,'LA')
team4 =get_season_Results_By_team(2025,'SF')
team5 = get_season_Results_By_team(2025,'SEA')


print(team_1)
print(team_2)
print(team_3)
print(team_4)
print(team_6)
print(team_6)

# 1. Which team has the best point differential this season?
    # The best overall Pd is INDY. They ha
# 2. Which team has the worst point differential this season?
     # The worst Pd is 
# 3. Which team has the best home point differential season?
     #
#4. Which     



