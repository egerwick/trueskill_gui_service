from trueskill_lib import *
from combination_analysis import *
from json_import import extract

#----------------------------------------------
# Main rating scipt
#----------------------------------------------

def apply_trueskill(game):    
    games = extract()
    f_mu = 25.0
    f_tau = 0
    track_mu_over_time = False
    list_players = games_in_trueskill(games, f_mu, f_tau, track_mu_over_time, 0)

    min_number_games = 0
    player_ranking_to_json(list_players, min_number_games, track_mu_over_time)
    return "hallo"