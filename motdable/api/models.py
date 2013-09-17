from django.db import models
from api.classes import PrivateKeyStorage


class Playbook(models.Model):
    """
    Scripted Plays (aka Ansible Playbooks) that the Coordinator
    executes against a Host.
    """
    
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='playbooks')
    
    title = models.CharField(max_length=100, blank=False, default='')
    content = models.TextField()
    
class PlaybookVariable(models.Model):
    """
    Passed to Playbooks as extra-vars, using title as the variable
    name and a <value> supplied by Coordinator at runtime.
    """
    
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='playbookvars')
    
    title = models.CharField(max_length=100, blank=False, default='')
    playbooks = models.ManyToManyField(Playbook, related_name='variables')


class Host(models.Model):
    """
    A Host (aka Machine, Server) that the Coordinator executes
    Playbooks agains.  
    """
    
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='hosts')
    
    hostname = models.CharField(max_length=100, blank=True, default='')
    login_username = models.CharField(max_length=100, default='root')
    private_key_file = models.FileField(upload_to='keys', storage=PrivateKeyStorage())
    


class Meta:
    ordering = ('created',)
