from django.shortcuts import render

# Create your views here.

def show_projects(request):
    return render(request, 'projects/index.html')
