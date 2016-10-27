from hello.models import Game
from rest_framework import serializers

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        field = ('id','team1f','team1b','team2f','team2b')    
    