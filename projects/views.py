from django.shortcuts import render, redirect
from projects.forms import DocumentForm
from User.models import UserContribution
from User.models import User_rating
from django.db.models import Sum
from User.models import User
from User.models import MultiTags
from .models import Category
from .models import Projects
from .models import Comment
from zipfile import ZipFile
import itertools
import os


####################helper functions##################
def get_projects_data(projects):
    raised_list = []
    ratio_list = []
    images = []
    for project in projects:
        sumation_donate = UserContribution.objects.filter(project_id=project).aggregate(Sum('donate'))["donate__sum"]
        if sumation_donate == None:
            sumation_donate = 0
        ratio = int((int(sumation_donate) / int(project.total_target)) * 100)
        raised_list.append(sumation_donate)
        ratio_list.append(ratio)
        images.append("documents/" + project.document.name.split("/")[3].split(".")[0] + "/" +
                      os.listdir("projects/static/documents/" + project.document.name.split("/")[3].split(".")[0])[0])
    return zip(projects, images, raised_list, ratio_list)


def extract_projects(query_object):
    return query_object.project_id


#####################################################
# Create your views here.
def home(request):
    return render(request, 'projects/home.html')


def rate(request, id):
    user = User.objects.get(pk=request.POST['user'])
    project = Projects.objects.get(pk=id)
    rating = request.POST['user_rating']
    current_rating = User_rating.objects.filter(project_id=project, user_id=user).update(rating=rating)
    if not current_rating:
        User_rating.objects.create(project_id=project, user_id=user, rating=rating)


def donate(request, id):
    donation = request.POST['donation']
    project = Projects.objects.get(pk=id)
    if UserContribution.objects.create(donate=donation, user_id=request.user, project_id=project):
        return redirect('list_projects')
    else:
        return render("500.html")


def show_projects(request):
    projects = Projects.objects.all()
    return render(request, 'projects/index.html', {
        'projects': get_projects_data(projects)
    })


def get_project(request, id):
    project = Projects.objects.get(pk=id)
    comments = Comment.objects.filter(project_id=id)
    projects_with_same_tags = []
    for tag in MultiTags.objects.filter(project_id=id):
        projects_of_this_tag = MultiTags.objects.select_related("project_id").filter(tag=tag.tag).only("project_id")
        projects_with_same_tags.append(projects_of_this_tag)
    similar_projects = list(itertools.chain(*projects_with_same_tags))

    def remove_current_project(project_object):
        if project_object == project:
            return False
        else:
            return True

    similar_projects = list(set(list(filter(remove_current_project, list(map(extract_projects, similar_projects))))))[
                       :5]

    try:
        user_rating = User_rating.objects.values('rating').filter(project_id=project, user_id=request.user)[0]["rating"]
    except:
        user_rating = 0
    sumation_donate = UserContribution.objects.filter(project_id=project).aggregate(Sum('donate'))["donate__sum"]
    if sumation_donate == None:
        sumation_donate = 0
    ratio = int((int(sumation_donate) / int(project.total_target)) * 100)
    images = []
    for img in os.listdir("projects/static/documents/" + project.document.name.split("/")[3].split(".")[0]):
        images.append("documents/" + project.document.name.split("/")[3].split(".")[0] + "/" + img)

    return render(request, 'projects/project.html', {
        'project': project, 'images': images, 'rating': user_rating, 'raised': sumation_donate, 'ratio': ratio,
        'comments': comments, 'similar_projects': get_projects_data(similar_projects)
    })


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        name = request.FILES["document"].name
        if form.is_valid():
            if name.endswith(".zip"):
                current_project = Projects.objects.create(user_id=request.user, title=request.POST['title'],
                                                          details=request.POST['details'],
                                                          total_target=request.POST['total_target'],
                                                          start_date=request.POST['start_date'],
                                                          end_date=request.POST['end_date'],
                                                          document=request.FILES['document'],
                                                          category_id=Category.objects.get(
                                                              pk=request.POST['category_id']))
                for tag in request.POST['tags'].split("#"):
                    MultiTags.objects.create(project_id=current_project, tag=tag)
                ############################################################
                # Create a ZipFile Object and load sample.zip in it
                with ZipFile("projects/static/documents/" + name, 'r') as zipObj:
                    # Extract all the contents of zip file in current directory
                    listOfFileNames = zipObj.namelist()
                    for fileName in listOfFileNames:
                        # Check filename endswith csv
                        if fileName.lower().endswith('.png') or fileName.lower().endswith(
                                '.jpg') or fileName.lower().endswith('.jpeg'):
                            # Extract a single file from zip
                            zipObj.extract(fileName, "projects/static/documents/{}".format(name.split(".")[0]))
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
        Category.objects.create(categories=request.POST['categories'])
