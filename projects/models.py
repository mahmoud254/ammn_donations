from django.db import models
from User import models as User


# Create your models here.

class Category(models.Model):
    categories = models.CharField(max_length=300)


class Project(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=300)
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    total_target = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    no_report = models.IntegerField()


class Replies(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    no_report = models.IntegerField()

