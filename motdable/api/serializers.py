from rest_framework import serializers

from api.models import Player, PlayCall
from django.contrib.auth.models import User


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
   
    class Meta:
        model = Player
        fields = ('url', 'id', 'hostname', 'login_username', 'login_private_key', 'owner')
        

class PlayCallSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
   
    class Meta:
        model = PlayCall
        fields = ('url', 'id', 'title', 'playbook', 'owner')
        
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    #playcalls = serializers.PrimaryKeyRelatedField(many=True)
    playcalls = serializers.HyperlinkedRelatedField(many=True, view_name='playcall-detail')
    players = serializers.HyperlinkedRelatedField(many=True, view_name='player-detail')
    
    class Meta:
        model = User
        fields = ('url', 'username', 'playcalls', 'players')
        
        
        
    