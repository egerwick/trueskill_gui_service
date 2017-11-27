import requests
import os
import time
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from models import Game, GamePerformance, Player, Greeting, RatingList, LastMonthRatingList
from serializers import GameSerializer, GamePerformanceSerializer, PlayerSerializer, RatingListSerializer, LastMonthRatingListSerializer
from django.utils.six import BytesIO
from trueskill.one_game_update import get_rating
from trueskill.efficient_scraping import scrape_games
from rest_framework.renderers import JSONRenderer



def get_current_month(month_from_fe):
    cm = time.strftime("%Y-%m")
    print int(cm[5:7]), ":", int(month_from_fe)
    last_month = str((int(cm[5:7]) - int(month_from_fe))%12)
    print last_month, 'here'
    if len(last_month) == 1:
         last_month = '0'+last_month
    cm = cm[0:5]+last_month
    return cm
        
def get_text_month():
    return time.strftime("%B %Y")

def convert_to_player_model(new_rating):
    ps_tmp = []
    for player in new_rating:
        ptmp = Player()
        ptmp.nickname = player['name']
        ptmp.position = player['position']
        ptmp.skill = "%.2f" % round(player['skill'],2)
        ptmp.mu = "%.2f" % round(player['mu'],2)
        ptmp.sigma = "%.2f" % round(player['sigma'],2)
        ptmp.winnerPercentage = "%.2f" % round(player['winnerPercentage'],2)
        ptmp.goalAverage = "%.2f" % round(player['goalAverage'],2)
        ps_tmp.append(ptmp)
    return ps_tmp

# Create your views here.
class PlayerList(APIView):
    def get(self, request, format=None):
        player = Player.objects.all()
        serializer = PlayerSerializer(player, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlayerSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GameList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GameSerializer(data=request.data, many=True)
        if serializer.is_valid():
            gamejson = JSONRenderer().render(serializer.data)
            new_rating = get_rating(gamejson)
            return Response(new_rating, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RatingList(APIView):
    def get(self, request, format=None):
        scrape_games()
        new_rating = get_rating()
        players = convert_to_player_model(new_rating)
        return render(request, 'rating.html', {'players': players})

class PreviousMonthRatingList(APIView):
    def get(self, request, format=None, month_count = "0", **kwargs):
        ### get month count from the URL
        month_from_fe = month_count 
        ###get all games from Kickerlytics
        #scrape_games()
        ### get the display month from current-month and month_from_fe
        ### TODO: get the year counter working
        display_month = get_current_month(month_from_fe) 
        print display_month
        new_rating = get_rating(True, display_month)
        players = convert_to_player_model(new_rating)
        return render(request, 'ratingMonth.html', {'players': players,'month': display_month})


def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})
