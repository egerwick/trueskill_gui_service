import requests
import os
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from models import Game, GamePerformance, Player
from serializers import GameSerializer, GamePerformanceSerializer, PlayerSerializer
from django.utils.six import BytesIO
from trueskill.one_game_update import apply_trueskill
from rest_framework.renderers import JSONRenderer

# Create your views here.

class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def pre_save(self, obj):
        obj.owner = self.request.user

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
            #Note that they are not saved to the DB, merely 
            #send through the rating function
            #new_rating includes new mu and sigma for all of the players
            gamejson = JSONRenderer().render(serializer.data)
            new_rating = get_rating(gamejson)
            return Response(new_rating, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
