from rest_framework import permissions
from rest_framework import viewsets

from api.models import PlayCall, Player, PlayCallOption
from api.serializers import PlayCallSerializer, PlayCallOptionSerializer, PlayerSerializer, UserSerializer
from api.permissions import IsOwnerOrReadOnly

from django.contrib.auth.models import User



class PlayCallViewSet(viewsets.ModelViewSet):
    """
    This is a CRUD endpoint for PlayCalls.
    
    PlayCalls are scripted Plays (aka Ansible Playbooks) that the Coordinator
    executes against a Player (aka Host).
    
    Each PlayCall consists of a title used to reference it, and a playbook
    which must conform to a valid yaml ansible playbook.
      ( http://www.ansibleworks.com/docs/playbooks.html )
      
    Additionally you can pass variables to playbooks via PlayCall Options.
    See the playcalloptions endpoint in our Api Root.
      
    NOTE:  
      The ansible playbook MUST use $host_group as its hosts: variable; e.g.
      ---
      - hosts: $host_group
        vars: 
          ...
      @todo In the future this will be templated/validated
    """
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    
    queryset = PlayCall.objects.all()
    serializer_class = PlayCallSerializer
    
    def pre_save(self, obj):
        obj.owner = self.request.user


class PlayCallOptionViewSet(viewsets.ModelViewSet):
    """
    This is a CRUD endpoint for PlayCall Options.
    
    Ansible supports passing variables to playbooks via the --extra-vars 
    command argument.
    
    PlayCall Options are passed to ansible playbooks using <title> as the 
    variable name and a <value> supplied by coordinator at runtime.
    
    E.g.
    
    If you create a PlayCall Option with a title of "message", then...
    
    ansible-playbook playbook.yml --exta-vars="{message: 'supplied_value'}"
    """
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    
    queryset = PlayCallOption.objects.all()
    serializer_class = PlayCallOptionSerializer
    
    def pre_save(self, obj):
        obj.owner = self.request.user
             

class PlayerViewSet(viewsets.ModelViewSet):
    """
    This is a CRUD endpoint for Players.
    
    PlayCalls target Players (aka Hosts).
    
    Each Player consists of a hostname and a login credentials 
    used to access it.
    
    Playbooks are executed as the login_username.
    
    NOTE:
      Players use ssh private keys for access. Please ensure these
      are appropriately setup for users on the target host.
    """
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    
    def pre_save(self, obj):
        obj.owner = self.request.user
        
 
 
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This is a readonly endpoint for Django Users.
    """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer