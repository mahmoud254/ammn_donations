from django.shortcuts import render,redirect
from projects.forms import DocumentForm
from User.models import MultiTags
from .models import Category
from .models import Projects
from zipfile import ZipFile
import os
# Create your views here.

def show_projects(request):
    projects=Projects.objects.all()

    images=[]
    for q in Projects.objects.values():
        images.append("documents/"+q['document'].split("/")[3].split(".")[0]+"/"+os.listdir("projects/static/documents/"+q['document'].split("/")[3].split(".")[0])[0])
        print(images)
    return render(request, 'projects/index.html', {
        'projects': zip(projects,images)
    })

def get_project(request,id):
    project = Projects.objects.get(pk=id)
    images=[]
    for img in os.listdir("projects/static/documents/"+project.document.name.split("/")[3].split(".")[0]):
        images.append("documents/"+project.document.name.split("/")[3].split(".")[0]+"/"+img)

    return render(request, 'projects/project.html', {
        'project': project,'images':images
    })

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        name = request.FILES["document"].name
        if form.is_valid():
            if name.endswith(".zip"):
                current_project=Projects.objects.create(user_id=request.user,title= request.POST['title'],details= request.POST['details'],total_target=request.POST['total_target'],start_date=request.POST['start_date'],end_date=request.POST['end_date'],document=request.FILES['document'],category_id=Category.objects.get(pk=request.POST['category_id']))
                for tag in request.POST['tags'].split("#"):
                    MultiTags.objects.create(project_id=current_project,tag=tag)
############################################################
                # Create a ZipFile Object and load sample.zip in it
                with ZipFile("projects/static/documents/"+name, 'r') as zipObj:
                   # Extract all the contents of zip file in current directory
                    listOfFileNames = zipObj.namelist()
                    for fileName in listOfFileNames:
                       # Check filename endswith csv
                       if fileName.lower().endswith('.png') or fileName.lower().endswith('.jpg') or fileName.lower().endswith('.jpeg'):
                           # Extract a single file from zip
                           zipObj.extract(fileName,"projects/static/documents/{}".format(name.split(".")[0]))
#############################################################
                return redirect('list_projects')
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
    

