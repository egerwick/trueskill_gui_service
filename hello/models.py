from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    team1f = models.CharField(max_length=100, blank=True, default='')
    team1b = models.CharField(max_length=100, blank=True, default='')
    team2f = models.CharField(max_length=100, blank=True, default='')
    team2b = models.CharField(max_length=100, blank=True, default='')