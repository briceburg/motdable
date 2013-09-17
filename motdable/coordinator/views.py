from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.utils import simplejson
import subprocess

def index(request):
    return render(request, 'coordinator/index.html', 
                  {"app_name": "coordinator"})

def catchall(request):
    return redirect('catchall')


def execute(request):
    
    options     = request.GET.get('options',[])
    playcall    = request.GET['playcallId']
    player      = request.GET['playerId']
    
    # @todo playbook execution should be a celery task / non-blocking call.
    mock_output = subprocess.check_output(["ls", "-l"]) 
    
    
    result = {
              "options": options,
              "playcall": playcall, 
              "player": player, 
              "output": mock_output
    }
    
    
    return HttpResponse(simplejson.dumps(result), 
                        mimetype='application/json')
    
    
    