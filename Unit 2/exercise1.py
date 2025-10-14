import pandas as pd
import nfl_data_py as nfl 

schedules = nfl.import_schedules([2024])

from helperFunctions import get_team_records

#print(schedules.colums.tolist())

records =get_team_records(2024)
print(records)


