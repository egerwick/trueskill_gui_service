# python-getting-started

A barebones Python app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started

$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)


App under:
https://trueskill-service.herokuapp.com/games/


To redeploy cleanly need to reset database

heroku pg:reset DATABASE

The make the migrations 
python manage.py makemigrations


Then commit 

git add .
git commit -m ""
git push heroku master

heroku run python manage.py migrate

App should then respond to 

curl -H "Content-Type: application/json" -X POST -d @test_data.json https://trueskill-service.herokuapp.com/games/ -u trueskilluser:password123

with appropriate test_data.json file

If a new user identity is needed then 

heroku run python manage.py createsuperuser
	


Run the App locally

heroku local

and then consume service

curl -H "Content-Type: application/json" -X POST -d @test_data.json http://localhost:5000 -u user:password123	


curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET https://trueskill-service.herokuapp.com/players/?format=json -u trueskilluser:password123