from django.db import models


class PlayCall(models.Model):
    """
    Scripted Plays (aka Ansible Playbooks) that the Coordinator
    executes against a Player
    """
    
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='playcalls')
    title = models.CharField(max_length=100, blank=True, default='')
    playbook = models.TextField()


class Player(models.Model):
    """
    A Player (aka Host, Machine, HostGroup, Server) that the Coordinator 
    targets with PlayCalls.  
    """
    
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='players')
    hostname = models.CharField(max_length=100, blank=True, default='')
    login_username = models.CharField(max_length=100, default='root')
    login_private_key = models.TextField()
    


class Meta:
    ordering = ('created',)
