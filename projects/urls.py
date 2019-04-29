from django.urls import path
from . import views
from . import ajax_views

urlpatterns = [
    path('', views.show_projects, name="list_projects"),
    path('add', views.model_form_upload, name='create_project'),
    path('<int:id>/donate', views.donate, name='donate'),
    path('<int:id>', views.get_project, name="get_project"),
    path('', views.create_category),
    path('<int:id>/rate', ajax_views.rate, name='rate'),
    path('<int:id>/comment', ajax_views.add_comment, name='comment'),
]
