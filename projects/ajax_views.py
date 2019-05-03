from User.models import User_rating
from User.models import User
from .models import Comment, Reported_Comment, Reported_Project
from .models import Projects
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponseRedirect,  HttpResponse
import json
from django.core import serializers

def rate(request, id):
    user = User.objects.get(pk=request.POST['user'])
    project = Projects.objects.get(pk=id)
    rating = request.POST['user_rating']
    current_rating = User_rating.objects.filter(project_id=project, user_id=user).update(rating=rating)
    if not current_rating:
        User_rating.objects.create(project_id=project, user_id=user, rating=rating)


def add_comment(request, id):
    user = User.objects.get(pk=request.POST['user'])
    project = Projects.objects.get(pk=id)

    if request.method == 'POST':
        comment = Comment.objects.create(user_id=user, project_id=project,
                                         text=request.POST['comment'])

        return JsonResponse({"id": comment.id, "text": comment.text, "user": user.username})

    else:
        return JsonResponse({'message': 'not post'})


def report_comment(request, id, cmid):
      user = User.objects.get(pk=request.GET['user'])  #user = request.user
#       user = serializers.serialize('json', user)
#       user = user["fields"]
#       return HttpResponse (user)
      if request.method == 'GET': 
        comment = Comment.objects.get(pk = cmid)
        # return HttpResponse(comment.text)
        if comment.project_id.id == id:
                Comment.objects.filter(pk=cmid).update(no_report = (comment.no_report+1))
                comment = Comment.objects.get(pk = cmid)
                if comment.no_report >= 5:
                   reported = Reported_Comment.objects.create(user_id = user, project_id = comment.project_id,
                                                         comment_id = comment, text = comment.text,
                                                         no_report = comment.no_report)
                   return JsonResponse({"user_id": reported.user_id, "project_id": reported.project_id,"comment_id": reported.comment_id, "text": reported.text,"no_report": reported.no_report})
                return HttpResponse(comment.no_report)
                
        else: 
                return JsonResponse({'message': 'this comment doesnt match the project id' })  
      else:
        return JsonResponse({'message': 'not get method' })    
                
def report_project(request, id):
      user = User.objects.get(pk=request.GET['user'])   #user = request.user
#       return HttpResponse (user)
      if request.method == 'GET': 
              proj = Projects.objects.get(pk=id)
              project = Projects.objects.filter(pk=id).update(no_report = (proj.no_report+1))
              proj = Projects.objects.get(pk=id)
              if proj.no_report >= 5:
                      reported = Reported_Project.objects.create(user_id=user,
                                                          title=proj.title,
                                                          project_id = proj.id,
                                                          details=proj.details,
                                                          total_target= proj.total_target,
                                                          start_date= proj.start_date,
                                                          end_date= proj.end_date,
                                                          document=proj.document,
                                                          category_id=proj.category_id,
                                                          is_featured = proj.is_featured,
                                                          )
                      return JsonResponse({

                                "user_id":user,
                                "title": reported.title,
                                "project_id": reported.id,
                                "details": reported.details,
                                "total_target": reported.total_target,
                                "start_date": reported.start_date,
                                "end_date": reported.end_date,
                                "document": reported.document,
                                "category_id": reported.category_id,
                                "is_featured": reported.is_featured
                      })
              return HttpResponse(proj.no_report) 
      else:
        return JsonResponse({'message': 'not get method' })        