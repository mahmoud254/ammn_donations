from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_projects),
    path('',views.create_category)
]