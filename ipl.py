import pandas as pd
import numpy as np

ipl_matches = r"D:\LEARNINGS\Self_Learn\CampusX\Pandas\02_pandas_dataframes\ipl-matches.csv"
matches = pd.read_csv(ipl_matches)

print(matches.head())

def teamsAPI():
    teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
    team_dict = {
        "teams": teams
    }
    return team_dict