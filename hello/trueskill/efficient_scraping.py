import urllib2
import os

def scrape_games():
    #Make path an environement variable
    url = 'https://kickerlytics.herokuapp.com/api/games'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path+'/all_games.json','w') as file_:
        file_.write(the_page)
    return
