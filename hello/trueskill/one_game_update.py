from trueskill_library import *


def get_rating(data):
    games = extract(data)
    new_ratings = games_in_trueskill(games)
    json_rankings = player_ranking_to_json(new_ratings) 
    print json_rankings
    return json_rankings