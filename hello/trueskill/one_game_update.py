from trueskill_lib import *
from json_import import extract
from games_filtering_functions import get_this_months_games

def get_rating(last_month_flag = False):
    games = extract()
    games.reverse()
    min_number_games = 20
    if last_month_flag:
        games = get_this_months_games(games)
        min_number_games = 0
    f_mu = 25.0
    f_tau = 2*0.083333
    track_mu_over_time = False
    list_players = games_in_trueskill(games, f_mu, f_tau, track_mu_over_time, 0	)
    return player_ranking_to_json(list_players,min_number_games)