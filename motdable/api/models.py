from django.db import models
from api.classes import PrivateKeyStorage


class Playbook(models.Model):
    """
    Scripted Plays (aka Ansible Playbooks) that the Coordinator
    executes against a Host.
    """
    owner = models.ForeignKey('auth.User', related_name='playbooks')
    
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False, default='')
    content = models.TextField()
    
    
class PlaybookVariable(models.Model):
    """
    Passed to Playbooks as extra-vars, using title as the variable
    name and a <value> supplied by Coordinator at runtime.
    """
    owner = models.ForeignKey('auth.User', related_name='playbookvars')
    playbooks = models.ManyToManyField(Playbook, related_name='variables')
    
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False, default='')
    
    
class Host(models.Model):
    """
    A Host (aka Machine, Server) that the Coordinator executes
    Playbooks agains.  
    """
    owner = models.ForeignKey('auth.User', related_name='hosts')
    credential = models.ForeignKey('HostCredential', related_name='hosts')
    
    created = models.DateTimeField(auto_now_add=True)
    hostname = models.CharField(max_length=100, blank=True, default='')
    
    
class HostCredential(models.Model):
    """
    A username + private_key used to login to Hosts
    """
    owner = models.ForeignKey('auth.User', related_name='hostcredentials')

    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, default='root')
    private_key_file = models.FileField(upload_to='keys', storage=PrivateKeyStorage())
    

class Meta:
    ordering = ('created',)
