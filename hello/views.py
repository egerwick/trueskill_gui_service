import requests
import os
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from models import Game, GamePerformance, Player, Greeting, RatingList
from serializers import GameSerializer, GamePerformanceSerializer, PlayerSerializer, RatingListSerializer
from django.utils.six import BytesIO
from trueskill.one_game_update import get_rating
from rest_framework.renderers import JSONRenderer

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
        #scrape the entire json file from Kickerlytics
        #scraped_games = scrape_games()
        #all_ratings = games_in_trueskill(scraped_games)
        all_games = 1
        all_ratings = 1
        return Response(all_ratings)

    def post(self, request, format=None):
        pass

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    #get all of the games
    #update the ratings
    #display the rating list
    return render(request, 'db.html', {'greetings': greetings})
