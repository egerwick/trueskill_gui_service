from trueskill_lib import *
from json_import import extract

def get_rating():
    games = extract()
    games.reverse()
    f_mu = 25.0
    f_tau = 0.083333
    track_mu_over_time = False
    list_players = games_in_trueskill(games, f_mu, f_tau, track_mu_over_time, 0	)
    min_number_games = 20
    return player_ranking_to_json(list_players,min_number_games)