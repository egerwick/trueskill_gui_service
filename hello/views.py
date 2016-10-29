import requests
import os
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from models import Game, GamePerformance, Player
from serializers import GameSerializer, GamePerformanceSerializer, PlayerSerializer
from rest_framework import generics
from django.utils.six import BytesIO
from trueskill.single_game_ranking import apply_trueskill
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
            #serializer.save()
            #get the new trueskill rating here and return
            #the player instances          
            json = JSONRenderer().render(serializer.data)
            new_game = apply_trueskill(json)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
