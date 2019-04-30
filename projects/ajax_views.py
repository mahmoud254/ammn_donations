from User.models import User_rating
from User.models import User
from .models import Comment
from .models import Projects
from django.http import JsonResponse
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
