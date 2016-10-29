from trueskill_lib import *
from combination_analysis import *
from json_import import extract
import time
start_time = time.time()
#----------------------------------------------
# Main rating scipt
#----------------------------------------------

# get the games from json
games = extract()
# execute the ranking (last argument is starting game)
# return the list of sorted, ranked players
f_mu = 25.0
f_tau = 0
track_mu_over_time = True
list_players = games_in_trueskill(games, f_mu, f_tau, track_mu_over_time, 0)

# Present the ranking results to terminal
min_number_games = 10
#player_ranking_to_json(list_players, min_number_games, track_mu_over_time)
#output_player_results(list_players, min_number_games)

# Pairs analysis
players_for_ranking = str([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
combination_analysis(games,players_for_ranking,min_number_games,f_mu,f_tau)

print("--- %s seconds ---" % (time.time() - start_time))
