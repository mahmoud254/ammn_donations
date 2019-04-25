from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserCreationForm(UserCreationForm):
    mobile_phone = forms.IntegerField()
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email' , 'mobile_phone')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email' , 'mobile_phone')