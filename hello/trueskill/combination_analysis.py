from trueskill_lib import *  
import math

def combination_analysis(games,players_for_ranking,min_number_games,f_mu,f_tau):
	for forwards in players_for_ranking:
		for backs in players_for_ranking:
			if forwards != backs:
				player_combination = [backs,forwards]
 				if number_of_games(backs,forwards,games) > min_number_games:
 					list_players = games_in_trueskill(games, f_mu, f_tau, False, player_combination)
	 				gain = compare_players_to_combination(list_players , player_combination)

	
def compare_players_to_combination(f_list_players,f_player_combination):
	p1 = f_player_combination[0]
	p2 = f_player_combination[1]
	pair = p1 + "-w-" + p2

	#loop over players and identify 
	for players in f_list_players:
		if players.name == p1 and players.position == 'offense':
			playerBack = players
		if players.name == p2 and players.position == 'defense':
			playerForward = players
		if players.name == pair:
			playerCombined = players

	gain = compute_gain(playerBack,playerForward,playerCombined)
	print p1,p2,playerCombined.ngame,float(playerCombined.won)/float(playerCombined.ngame),gain[0],gain[1],gain[2]
	return

def compute_gain(f_playerBack,f_playerForward,f_playerCombined):
	g = f_playerCombined.rating.mu**2-f_playerBack.rating.mu*f_playerForward.rating.mu
	g = g/math.sqrt(abs(g))
	return [f_playerCombined.rating.mu, g, f_playerCombined.rating.sigma]