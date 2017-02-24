import json


def extract():
    games = []
    #make path environment variable
    with open('/app/hello/trueskill/all_games.json') as data_file:
        data = json.load(data_file)

    for item in data:
        goals = [None] * 8
        
        goals[0] = item.get('team1').get('offenseGoals')
        goals[1] = item.get('team1').get('defenseGoals')
        goals[2] = item.get('team2').get('offenseGoals')
        goals[3] = item.get('team2').get('defenseGoals')

        goals[4] = item.get('team1').get('offenseOwnGoals')
        goals[5] = item.get('team1').get('defenseOwnGoals')
        goals[6] = item.get('team2').get('offenseOwnGoals')
        goals[7] = item.get('team2').get('defenseOwnGoals')

        for i in range(len(goals)):
            if not goals[i] > 0:
                goals[i] = 0

        goals_team1 = goals[0] + goals[1] + goals[6] + goals[7]
        goals_team2 = goals[2] + goals[3] + goals[4] + goals[5]

        #
        if goals_team1 == 10:
            current_game = [
                item.get('team1').get('defense').get('nickname').encode('utf-8'),
                item.get('team1').get('offense').get('nickname').encode('utf-8'),
                item.get('team2').get('defense').get('nickname').encode('utf-8'),
                item.get('team2').get('offense').get('nickname').encode('utf-8'),
                item.get('team1').get('defenseGoals'),
                item.get('team1').get('offenseGoals'),
                item.get('team2').get('defenseGoals'),
                item.get('team2').get('offenseGoals'),
                item.get('submissionDate'),
                item.get('crawling')
            ]
        else:
            current_game = [
                item.get('team2').get('defense').get('nickname').encode('utf-8'),
                item.get('team2').get('offense').get('nickname').encode('utf-8'),
                item.get('team1').get('defense').get('nickname').encode('utf-8'),
                item.get('team1').get('offense').get('nickname').encode('utf-8'),
                item.get('team2').get('defenseGoals'),
                item.get('team2').get('offenseGoals'),
                item.get('team1').get('defenseGoals'),
                item.get('team1').get('offenseGoals'),
                item.get('submissionDate'),
                item.get('crawling')
            ]
        games.append(current_game)
    return games
