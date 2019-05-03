from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # email = models.EmailField()
    # password = models.CharField(max_length=10)
    username = models.CharField(max_length=30, unique=False)
    mobile_phone = models.IntegerField(null=True)
    profile_pic = models.ImageField(upload_to='images/')
    birth_date = models.DateField(null=True)
    fb_profile = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)

    USERNAME_FIELD = 'email'
    email = models.EmailField(_('email address'), unique=True)
    REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS
    objects = UserManager()

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
