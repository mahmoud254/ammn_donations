from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # email = models.EmailField()
    # password = models.CharField(max_length=10)
    mobile_phone = models.IntegerField(null=True)
    profile_pic = models.CharField(max_length=200)
    birth_date = models.DateField(null=True)
    fb_profile = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.email


class UserContribution(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey("projects.Projects", on_delete=models.CASCADE)
    donate = models.IntegerField()



class User_rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey("projects.Projects", on_delete=models.CASCADE)
    rating = models.IntegerField()


class MultiPics(models.Model):
    project_id = models.ForeignKey("projects.Projects", on_delete=models.CASCADE)
    pic = models.CharField(max_length=200)


class MultiTags(models.Model):
    project_id = models.ForeignKey("projects.Projects", on_delete=models.CASCADE)
    tag = models.CharField(max_length=200)
