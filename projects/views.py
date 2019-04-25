from django.shortcuts import render
from .models import Category
# Create your views here.

def show_projects(request):
    return render(request, 'projects/index.html')

def create_category(request):
    if request.method == "POST":
        Category.objects.create(categories= request.POST['categories'])
    