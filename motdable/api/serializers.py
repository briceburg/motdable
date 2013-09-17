from rest_framework import serializers

from api.models import Host, Playbook, PlaybookVariable
from django.contrib.auth.models import User


class HostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Host
        fields = ('url', 'id', 'hostname', 'login_username', 'private_key_file', 'owner')
        
        
class PlaybookVariableSerializer(serializers.HyperlinkedModelSerializer):
    
    playbooks = serializers.SlugRelatedField(many=True, slug_field='title', required=False)   
    
    class Meta:
        model = PlaybookVariable
        fields = ('url', 'id', 'title', 'playbooks', 'owner')
        

class PlaybookSerializer(serializers.HyperlinkedModelSerializer):
    
   variables = serializers.SlugRelatedField(many=True, slug_field='title', required=False)
    
   class Meta:
        model = Playbook
        fields = ('url', 'id', 'title', 'content', 'variables', 'owner')

        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ('url', 'username', 'playbooks', 'playbookvars', 'hosts')
        
        
        
    