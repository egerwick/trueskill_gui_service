import json

def extract():
    games = []
    with open('./hello/trueskill/test_data.json') as data_file:
        data = json.load(data_file)
    i = 0
    for item in data:
        goals = [None] * 8
        
        goals[0] = item.get('team1of').get('goals')
        goals[1] = item.get('team1def').get('goals')
        goals[2] = item.get('team2of').get('goals')
        goals[3] = item.get('team2def').get('goals')

        goals[4] = item.get('team1of').get('owngoals')
        goals[5] = item.get('team1def').get('owngoals')
        goals[6] = item.get('team2of').get('owngoals')
        goals[7] = item.get('team2def').get('owngoals')

        for i in range(len(goals)):
            if not goals[i] > 0:
                goals[i] = 0

        goals_team1 = goals[0] + goals[1] + goals[6] + goals[7]
        goals_team2 = goals[2] + goals[3] + goals[4] + goals[5]

        #
        if goals_team1 == 10:
            current_game = [
                str(item.get('team1def').get('player').get('id')),
                str(item.get('team1of').get('player').get('id')),
                str(item.get('team2def').get('player').get('id')),
                str(item.get('team2of').get('player').get('id')),
                item.get('team1def').get('goals'),
                item.get('team1of').get('goals'),
                item.get('team2def').get('goals'),
                item.get('team2of').get('goals'),
                item.get('timestamp'),
                item.get('crawling')
            ]
        else:
            current_game = [
                str(item.get('team2def').get('player').get('id')),
                str(item.get('team2of').get('player').get('id')),
                str(item.get('team1def').get('player').get('id')),
                str(item.get('team1of').get('player').get('id')),
                item.get('team2def').get('goals'),
                item.get('team2of').get('goals'),
                item.get('team1def').get('goals'),
                item.get('team1of').get('goals'),
                item.get('timestamp'),
                item.get('crawling')
            ]
        games.append(current_game)
    return games
