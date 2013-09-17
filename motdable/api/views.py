from rest_framework import permissions
from rest_framework import viewsets

from api.models import Playbook, PlaybookVariable, Host, HostCredential
from api.serializers import HostSerializer, HostCredentialSerializer, PlaybookVariableSerializer, PlaybookSerializer, UserSerializer
from api.permissions import IsOwnerOrReadOnly

from django.contrib.auth.models import User



class PlaybookViewSet(viewsets.ModelViewSet):
    """
    This is a CRUD endpoint for Playbooks.
    
    Playbooks are Scripted Plays (aka Ansible Playbooks) that the Coordinator
    executes against a Host.
    
    Each Playbook consists of a title used to reference it, and content
    which must represent a valid yaml ansible playbook.
      ( http://www.ansibleworks.com/docs/playbooks.html )
      
    You may additionally pass variables to playbooks via PlaybookVariables .
    See the playbookvars endpoint in our Api Root for management.
      
    NOTE:  
      The ansible playbook MUST use $host_group as its hosts: variable; e.g.
      ---
      - hosts: $host_group
        vars: 
          ...
      @todo In the future this will be templated/validated
    """
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    
    queryset = Playbook.objects.all()
    serializer_class = PlaybookSerializer
    
    def pre_save(self, obj):
        obj.owner = self.request.user


class PlaybookVariableViewSet(viewsets.ModelViewSet):
    """
    This is a CRUD endpoint for PlaybookVariables.
    
    Ansible supports passing variables to playbooks via the --extra-vars 
    command argument.
    
    PlaybookVariables are passed to ansible playbooks using <title> as the 
    variable name and a <value> supplied by coordinator at runtime.
    
    E.g.
    
    If you create a PlaybookVariable with a title of "message", then...
    
    ansible-playbook playbook.yml --exta-vars="{message: 'supplied_value'}"
    """
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    
    queryset = PlaybookVariable.objects.all()
    serializer_class = PlaybookVariableSerializer
    
    def pre_save(self, obj):
        obj.owner = self.request.user
             

class HostViewSet(viewsets.ModelViewSet):
    """
    This is a CRUD endpoint for Hosts.
    
    Each Host consists of a hostname [or IP address] and a login credentials 
    used to access it.
    
    See the hostcredentials endpoint in our Api Root for management.
    """
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    
    def pre_save(self, obj):
        obj.owner = self.request.user
        
        
class HostCredentialViewSet(viewsets.ModelViewSet):
    """
    This is a CRUD endpoint for HostCredentials.
    
    A username + private_key used to login to Hosts.
    
    Uses a many-to-many relationship so we may share credentials amongst host(s)
    
    NOTE: Please ensure the public key equivalent is added to the user's
    authorized_keys file on your host(s).
    """
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    
    queryset = HostCredential.objects.all()
    serializer_class = HostCredentialSerializer
    
    def pre_save(self, obj):
        obj.owner = self.request.user
        
 
 
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This is a readonly endpoint for Django Users.
    """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer