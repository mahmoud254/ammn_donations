
from django.urls import path, include 
from . import views


urlpatterns = [
    
    path('', views.index, name='index'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
