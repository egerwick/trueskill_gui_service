from trueskill_library import *

def apply_trueskill(igame):
    games = extract(igame)
    new_ratings = games_in_trueskill(games)
    json_rankings = player_ranking_to_json(new_ratings) 
    return json_rankings