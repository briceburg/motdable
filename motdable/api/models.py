from django.db import models
from api.classes import PrivateKeyStorage


class PlayCall(models.Model):
    """
    Scripted Plays (aka Ansible Playbooks) that the Coordinator
    executes against a Player
    """
    
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='playcalls')
    title = models.CharField(max_length=100, blank=False, default='')
    playbook = models.TextField()
    
class PlayCallOption(models.Model):
    """
    Passed to ansible playbooks as extra-vars, using title as the variable
    name and a <value> supplied by coordinator at runtime.
    """
    
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='playcalloptions')
    title = models.CharField(max_length=100, blank=False, default='')
    playcalls = models.ManyToManyField(PlayCall, related_name='options')


class Player(models.Model):
    """
    A Player (aka Host, Machine, HostGroup, Server) that the Coordinator 
    targets with PlayCalls.  
    """
    
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='players')
    hostname = models.CharField(max_length=100, blank=True, default='')
    login_username = models.CharField(max_length=100, default='root')
    private_key_file = models.FileField(upload_to='keys', storage=PrivateKeyStorage())
    


class Meta:
    ordering = ('created',)
