from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_projects,name="list_projects"),
    path('add',views.model_form_upload,name='create_project'),
    path('home',views.home,name='home'),
    path('<int:id>',views.get_project,name="get_project"),
    path('',views.create_category)
]