from django.contrib import admin

# Register your models here.
from .models import Category, Projects, Comment, Replies
admin.site.register(Category)
admin.site.register(Projects)
admin.site.register(Comment)
admin.site.register(Replies)