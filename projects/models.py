from django.db import models
from User import models as User_models


# Create your models here.

class Category(models.Model):
    categories = models.CharField(max_length=300)


class Projects(models.Model):
    user_id = models.ForeignKey(User_models.User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=300)
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    total_target = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_featured = models.BooleanField(default=False)
    document = models.FileField(upload_to='projects/static/documents/')


class Comment(models.Model):
    user_id = models.ForeignKey(User_models.User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    no_report = models.IntegerField(null=True, default=0)


class Replies(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    no_report = models.IntegerField(default=0)

# class Reported_Comment(Comment):
#     dummy = models.IntegerField(null=True,default=1)
   
# class Reported_Project(Projects):
#     # project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
#     dummy = models.IntegerField(null=True, default=1)

# class Reported_Reply(Replies):
#     # reply_id = models.ForeignKey(Replies,on_delete=models.CASCADE)
#     dummy = models.IntegerField(null=True, default=1)

class Reported_Comment(models.Model):
    user_id = models.ForeignKey(User_models.User, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete = models.CASCADE)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    no_report = models.IntegerField(null=True, default=0)    

class Reported_Project(models.Model):
    user_id = models.ForeignKey(User_models.User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=300)
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    total_target = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_featured = models.BooleanField(default=False)
    document = models.FileField(upload_to='projects/static/documents/')

# class Reported_Reply(models.Model):
#     comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     reply_id = models.ForeignKey(Replies, on_delete = models.CASCADE)
#     text = models.CharField(max_length=200)
#     no_report = models.IntegerField(default=0)