# https://github.com/swar/nba_api/blob/master/docs/examples/Finding%20Games.ipynb
from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd

def season_str(x):
    return str(x) + '-' + str(x+1)[-2:]

# Get all playoff games from 2015 to 2020
playoff_games = {}
for season in range(2015, 2020):
    playoff_games[str(season)] = leaguegamefinder.LeagueGameFinder(season_nullable=season_str(season),                                  
    season_type_nullable='Playoffs').get_data_frames()[0]

playoff_games_all = pd.concat(playoff_games)
playoff_games_all.to_csv("./data/playoff_games.csv", index = False)
