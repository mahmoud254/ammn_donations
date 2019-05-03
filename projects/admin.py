from django.contrib import admin

# Register your models here.
from .models import Category, Projects, Comment, Replies, Reported_Comment, Reported_Project
admin.site.register(Category)
admin.site.register(Projects)
admin.site.register(Comment)
admin.site.register(Replies)
admin.site.register(Reported_Comment)
admin.site.register(Reported_Project)
