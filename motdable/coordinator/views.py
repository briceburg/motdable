from django.shortcuts import render

def index(request):
    return render(request, 'coordinator/index.html', 
                  {"app_name": "coordinator"})
