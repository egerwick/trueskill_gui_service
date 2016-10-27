from django.contrib.auth.models import User, Group
from hello.models import Game
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        field = ('id','team1f','team1b','team2f','team2b')    
    