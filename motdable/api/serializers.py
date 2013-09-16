from rest_framework import serializers

from api.models import Player, PlayCall, PlayCallOption
from django.contrib.auth.models import User


class PlayerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Player
        fields = ('url', 'id', 'hostname', 'login_username', 'login_private_key', 'owner')
        
        
class PlayCallSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = PlayCall
        fields = ('url', 'id', 'title', 'playbook', 'options', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ('url', 'username', 'playcalls', 'players')
        
        
        
    