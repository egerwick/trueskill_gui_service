from trueskill_library import *

def get_rating(igame):
    games = extract(igame)
    new_ratings = games_in_trueskill(games)
    json_rankings = player_ranking_to_json(new_ratings) 
    print json_rankings
    return json_rankings