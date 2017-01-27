import time

def get_this_months_games(games):
    ngames = []
    this_month = time.strftime("%Y-%m")
    for game in games:
        sub_date = game[8][0:7]
        if sub_date == this_month:
            ngames.append(game)
    return ngames 