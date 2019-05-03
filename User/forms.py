from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserCreationForm(UserCreationForm):
    
    
    # profile_pic = forms.ImageField() , 'profile_pic'
    class Meta(UserCreationForm):
        model = User
        fields = ('username','first_name', 'last_name' , 'mobile_phone' ,  'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email' )

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    mobile_phone= forms.RegexField(regex=r'^01[0125][0-9]{8}$',help_text='invalid phone number')
    profile_pic = models.ImageField()

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name' , 'mobile_phone' ,  'email','password1', 'password2','profile_pic')
