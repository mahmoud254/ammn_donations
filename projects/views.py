from django.shortcuts import render
from projects.forms import DocumentForm
from .models import Category
from .models import Projects
# Create your views here.

def show_projects(request):
    return render(request, 'projects/index.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        name = request.FILES["document"].name
        if form.is_valid():
            if name.endswith(".zip"):
                Projects.objects.create(user_id=request.user,title= request.POST['title'],details= request.POST['details'],total_target=request.POST['total_target'],start_date=request.POST['start_date'],end_date=request.POST['end_date'],document=request.FILES['document'],category_id=Category.objects.get(pk=request.POST['category_id']))
                return render(request, 'projects/index.html')
            else:
                pass
        else:
            pass
    else:
        form = DocumentForm()
    return render(request, 'projects/model_form_upload.html', {
        'form': form
    })

def create_category(request):
    if request.method == "POST":
        Category.objects.create(categories= request.POST['categories'])
    

