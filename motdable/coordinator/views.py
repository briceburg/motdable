from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files import File

from api.models import Playbook, Host

import subprocess, sys, json, os


def index(request):
    return render(request, 'coordinator/index.html', 
                  {"app_name": "coordinator"})

def catchall(request):
    return redirect('catchall')


def execute(request):
    
    variables   = request.GET.get('variables','{}')
    playbook    = Playbook.objects.get(pk=request.GET['playbookId'])
    host        = Host.objects.get(pk=request.GET['hostId'])
    
    if hasattr(sys, 'real_prefix'): 
        
        # write a temporary inventory file
        with open(sys.prefix + '/tmp.inventory', 'w') as f:
            inventory_file = File(f)
            inventory_file.write("127.0.0.1\n" + host.hostname)
            
        # write a temporary playbook file
        with open(sys.prefix + '/tmp.playbook', 'w') as f:
            playbook_file = File(f)
            playbook_file.write(playbook.content)
        
        # create extravars
        extra_vars = json.loads(variables)
        extra_vars['host_group'] = host.hostname
        
        env_vars = dict(os.environ)
        env_vars['ANSIBLE_HOST_KEY_CHECKING'] = 'False'
        
        # @todo playbook execution should be a celery task / non-blocking call.
        process = subprocess.Popen([
            sys.prefix + '/bin/ansible-playbook',
            '--inventory-file=' + inventory_file.name,
            '--user=' + host.credential.username,
            '--private-key=' + host.credential.private_key_file.path,
            '--extra-vars=' + json.dumps(extra_vars),
            playbook_file.name
        
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
    
    