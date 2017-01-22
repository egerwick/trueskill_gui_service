from django.db import models

# Create your models here.

class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    nickname = models.CharField(max_length=100, blank=True, default='')
    mu = models.FloatField(default = 25.0)
    sigma = models.FloatField(default = 8.33333)

class GamePerformance(models.Model):
    goals = models.IntegerField(default = 0)
    owngoals = models.IntegerField(default = 0, null=True, blank=True)
    playerposition = models.CharField(max_length=100, blank=True, default='')
    winner = models.BooleanField(default = False)
    player = models.OneToOneField(Player,null=True)
    crawling = models.BooleanField(default = False)

class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.CharField(max_length=100, blank=True, default='')
    team1of = models.OneToOneField(GamePerformance, related_name = "team1of_per", null=True) 
    team1def = models.OneToOneField(GamePerformance, related_name = "team1def_per", null=True)
    team2of = models.OneToOneField(GamePerformance, related_name = "team2of_per", null=True)
    team2def = models.OneToOneField(GamePerformance, related_name = "team2def_per", null=True)

class RatingList(models.Model):
    players = models.ForeignKey(Player)
    timestamp = models.CharField(max_length=100, blank=True, default='')