from django.shortcuts import render, redirect

def index(request):
    return render(request, 'coordinator/index.html', 
                  {"app_name": "coordinator"})

def catchall(request):
    return redirect('catchall')