# Register your models here.

# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin

from django.contrib import admin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

# class CustomUserAdmin(admin.ModelAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = User
#     fields = ('username','first_name', 'last_name' , 'mobile_phone' ,  'email', 'password')
#     # list_display = ['email', 'username',]

# admin.site.register(User, CustomUserAdmin)



@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
