from trueskill import Rating, rate, TrueSkill
import json

#----------------------------------------------

class Player(object):

    def __init__(self, nickname, playerposition, rating, pid):
        self.pid = pid
        self.nickname = nickname
        self.playerposition = playerposition
        self.rating = Rating(rating) 
        self.rating_history = []
        self.skill = player_skill(self)
        self.goals = 0
        self.ngame = 0
        self.crawl = 0
        self.goal_average = 0
        self.won = 0
        self.winner_flag = False
        self.played_in_last_day = False

def player_skill(p):
    p.skill = p.rating.mu - 3 * p.rating.sigma

#----------------------------------------------
def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result


def extract(game):
    data = json.loads(game)
    i = 0
    positions = ['team1def','team1of','team2def','team2of']
    games = []
    for item in data:
        game_rep = []
        for position in positions:
            id_tmp = item.get(position).get('player').get('id')
            nickname_tmp = item.get(position).get('player').get('nickname')
            playerposition_tmp = item.get(position).get('playerposition')
            mu_tmp = item.get(position).get('player').get('mu')
            sigma_tmp = item.get(position).get('player').get('sigma')
            rating_tmp = TrueSkill(mu=mu_tmp, sigma=sigma_tmp)
            rating_tmp.create_rating()
            p_tmp = Player(nickname_tmp,playerposition_tmp,25,id_tmp)
            p_tmp.rating = rating_tmp
            p_tmp.winner_flag = item.get(position).get('winner')
            game_rep.append(p_tmp)
        games.append(game_rep)
    return games     


def game_in_trueskill(game):
    Winners = [p for p in game if p.winner_flag == True]
    Losers = [p for p in game if p.winner_flag == False]
    WinR = [Winners[0].rating,Winners[1].rating]
    LosR = [Losers[0].rating,Losers[1].rating]
    (Winners[0].rating, Winners[1].rating), (Losers[0].rating,Losers[1].rating) = rate([WinR,LosR],ranks=[0, 1])
    return [Winners,Losers]


def games_in_trueskill(games):
    results = []
    for game in games:
        results.append(game_in_trueskill(game))
    return flatten(results) 


def player_ranking_to_json(rankings):
    tmp_data = []
    for p in rankings:
        p_tmp = {"id": p.pid, "nickname": p.nickname, "mu": p.rating.mu, "sigma": p.rating.sigma }
        tmp_data.append(p_tmp)
    return tmp_data







