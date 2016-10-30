from trueskill_library import *
games = extract()
new_ratings = games_in_trueskill(games)
json_rankings = player_ranking_to_json(new_ratings)