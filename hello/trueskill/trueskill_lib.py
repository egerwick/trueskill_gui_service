from trueskill import Rating, rate, TrueSkill
from json_import import extract
from collections import OrderedDict
import sys
import json

#----------------------------------------------


class player(object):

    def __init__(self, name, position, rating):
        self.name = name
        self.position = position
        self.rating = Rating(rating)
        self.rating_history = []
        self.skill = player_skill(self)
        self.goals = 0
        self.ngame = 0
        self.crawl = 0
        self.goal_average = 0
        self.won = 0
        self.played_in_last_day = False


def goal_average(p):
    p.goal_average = p.goals / p.ngame


def add_game(p):
    p.ngame = p.ngame + 1


def add_win(p):
    p.won = p.won + 1


def add_crawl(p):
    p.crawl = p.crawl + 1


def add_goals(p, goals):
    if not goals > 0:
        goals = 0
    p.goals = p.goals + goals


def player_skill(p):
    p.skill = p.rating.mu - 3 * p.rating.sigma
#----------------------------------------------


def add_or_find_player(listn, name, pos, av_rating):
    index_player = 0
    for items in listn:
        index_player = index_player + 1
        if(name == items.name and pos == items.position):
            return index_player - 1
    listn.append(player(name, pos, av_rating))
    return index_player


def get_players_instances(f_game, f_list_players, av_rating, player_combination=None):
    if player_combination:
        p1 = player_combination[0]
        p2 = player_combination[1]
        if f_game[0] == p1 and f_game[1] == p2:
            f_game[0] = p1 + "-w-" + p2
            f_game[1] = p2 + "-w-" + p1
        if f_game[2] == p1 and f_game[3] == p2:
            f_game[2] = p1 + "-w-" + p2
            f_game[3] = p2 + "-w-" + p1
    # returns the indices of the corresponding players
    # if players don't exist, create new instance
    # if combination p1 and p2 are set then games
    # with this combination are given own instance
    # Make new game instances for matching players
    num = 0
    ip = []
    for name in f_game:
        if (num == 0 or num == 2):
            position = 'defense'
        else:
            position = 'offense'
        ip.append(add_or_find_player(
            f_list_players, name, position, av_rating))
        num = num + 1
    return ip


def get_average_player_mu(players):
    average = 0
    for player in players:
        average = average + player.rating.mu
    return average / len(players)


def game_in_trueskill(winnerBack, winnerForw, loserBack, loserForw, f_game):
    team1 = [winnerBack.rating, winnerForw.rating]
    team2 = [loserBack.rating, loserForw.rating]
    add_game(winnerBack)
    add_game(winnerForw)
    add_win(winnerBack)
    add_win(winnerForw)

    add_game(loserBack)
    add_game(loserForw)

    if f_game[9] == True:
        add_crawl(loserBack)
        add_crawl(loserForw)

    add_goals(winnerBack, f_game[4])
    add_goals(winnerForw, f_game[5])
    add_goals(loserBack, f_game[6])
    add_goals(loserForw, f_game[7])

    winnerBack.played_in_last_day = True
    winnerForw.played_in_last_day = True
    loserBack.played_in_last_day = True
    loserForw.played_in_last_day = True

    # Call to the trueskill algorithm
    (winnerBack.rating, winnerForw.rating), (loserBack.rating,
                                             loserForw.rating) = rate([team1, team2], ranks=[0, 1])
    return


def number_of_games(f_playerb, f_playerf, f_games):
    count_games = 0
    for game in f_games: 
         if (f_playerb == game[0] and f_playerf == game[1]) or (f_playerb == game[2] and f_playerf == game[3]):
            count_games = count_games + 1
    return count_games


def number_of_wins(f_playerb, f_playerf, f_games):
    wins = 0
    for game in games:
        if (f_playerb == game[0] and f_playerf == game[1]):
            wins = wins + 1
    return wins


def calc_player_skill(f_list_players):
    for player in f_list_players:
        player_skill(player)


def record_skill_over_time(lplayers, timestamp):
    for player in lplayers:
        if player.played_in_last_day is True:
            player.rating_history.append( {"timestamp": timestamp, "mu": player.rating.mu} )
            player.played_in_last_day = False


def games_in_trueskill(f_games, f_mu, f_tau, track_mu_over_time, player_combination=None):
    # define the rating parameters and environment
    list_players = []
    env = TrueSkill(mu=f_mu, tau=f_tau, beta=4.167, draw_probability=0)
    env.make_as_global()
    average_rating = 25
    game_number = 0
    last_game_day = f_games[0][8]
    for game in f_games:
        game_number = game_number + 1
        list(game)
        if track_mu_over_time:
            game_day = game[8]
            if game_day[0:10] != last_game_day[0:10]:
                record_skill_over_time(list_players, last_game_day)
                last_game_day = game_day
        ip = get_players_instances(
            game, list_players, average_rating, player_combination)
        game_in_trueskill(list_players[ip[0]], list_players[
                          ip[1]], list_players[ip[2]], list_players[ip[3]], game)
        #average_rating = get_average_player_mu(list_players)
    # records final game day
    if track_mu_over_time:
        record_skill_over_time(list_players, game_day)

    calc_player_skill(list_players)
    return list_players


def print_games(f_games, name1=None, name2=None):
    game_number = 0
    for game in f_games:
        game_number = game_number + 1
        print_game_results(game_number, game, name1, name2)

def encode_json(data):
    print json.dumps(data)

def player_ranking_to_json(f_list_players, f_min_number_games):
    total_games = 0
    tmp_data = []
    f_list_players.sort(key=lambda player: player.rating.mu, reverse=True)
    for p in f_list_players:
        total_games = total_games + float(p.ngame)
        if(p.ngame > f_min_number_games):
            p_tmp = {"name": p.name.encode('utf-8'),"position": p.position ,"mu": p.rating.mu, "sigma": p.rating.sigma, "winnerPercentage": float(p.won) / float(p.ngame), "goalAverage":float(p.goals) / float(p.ngame)}
            tmp_data.append(p_tmp)
    return tmp_data
