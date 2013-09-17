from __future__ import print_function

from django.shortcuts import render, redirect
from django.http import HttpResponse
from api.models import PlayCall, Player

import subprocess, sys, json, os


def index(request):
    return render(request, 'coordinator/index.html', 
                  {"app_name": "coordinator"})

def catchall(request):
    return redirect('catchall')


def execute(request):
    
    options     = request.GET.get('options','{}')
    playcall    = PlayCall.objects.get(pk=request.GET['playcallId'])
    player      = Player.objects.get(pk=request.GET['playerId'])
    
    if hasattr(sys, 'real_prefix'): 
        
        # write a temp inventory file, @todo: one-liner?
        inventory_file = sys.prefix + '/tmp.inventory' 
        f = open(inventory_file,'w')
        print('127.0.0.1', file=f)
        print(player.hostname, file=f)
        f.close()
        
        # write a temp playbook file, @todo: one-liner?
        playbook_file = sys.prefix + '/tmp.playbook' 
        f = open(playbook_file,'w')
        print(playcall.playbook, file=f)
        f.close() 
        
        # create extravars
        extra_vars = json.loads(options)
        extra_vars['host_group'] = player.hostname
        
        env_vars = dict(os.environ)
        env_vars['ANSIBLE_HOST_KEY_CHECKING'] = 'False'
        
        # @todo playbook execution should be a celery task / non-blocking call.
        process = subprocess.Popen([
            sys.prefix + '/bin/ansible-playbook',
            '--inventory-file=' + inventory_file,
            '--user=' + player.login_username,
            '--private-key=' + player.private_key_file.path(),
            '--extra-vars=' + json.dumps(extra_vars),
            playbook_file
        
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env_vars)
        
        stdout, stderr = process.communicate()
        output = stderr if stderr else stdout
        
    else:
        # note: it's irrelevant if we're within a virtualenv or not,
        #  I am just using as an indicator that the ansible dependencies
        #  have been installed as per installation instructions requirements.
        #    ++ as a programming exercise to detect a virtual environment.
        output  = 'Failed to execute. Django not running in a virtualenv.'
            

    return HttpResponse(json.dumps({"output": output}),
                        mimetype='application/json')
    
    