import urllib2

def scrape_games():
    url = 'https://kickerlytics.herokuapp.com/api/games'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    with open('/app/hello/trueskill/all_games.json','w') as file_:
        file_.write(the_page)
    return
