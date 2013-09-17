from rest_framework import serializers

from api.models import Host, HostCredential, Playbook, PlaybookVariable
from django.contrib.auth.models import User


class HostSerializer(serializers.HyperlinkedModelSerializer):
    
    credential = serializers.SlugRelatedField(slug_field='username', required=True)
    
    class Meta:
        model = Host
        fields = ('url', 'id', 'hostname', 'credential', 'owner')

        
class HostCredentialSerializer(serializers.HyperlinkedModelSerializer):
    
    hosts = serializers.SlugRelatedField(many=True, slug_field='hostname', required=False)

    class Meta:
        model = HostCredential
        fields = ('url', 'id', 'username', 'private_key_file', 'hosts', 'owner')
        
        
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
        
        
        
    