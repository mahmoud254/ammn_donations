from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_projects),
    path('add',views.model_form_upload),
    path('',views.create_category)
]