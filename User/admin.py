from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from django.contrib import admin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    fields = ('username','first_name', 'last_name' , 'mobile_phone' ,  'email', 'password')
    # list_display = ['email', 'username',]

admin.site.register(User, CustomUserAdmin)