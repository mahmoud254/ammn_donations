from django.urls import path
from . import views
from . import ajax_views

urlpatterns = [
    path('', views.show_projects, name="list_projects"),
    path('add', views.model_form_upload, name='create_project'),
    path('<int:id>/donate', views.donate, name='donate'),
    path('<int:id>', views.get_project, name="get_project"),
    path('<int:id>/rate', ajax_views.rate, name='rate'),
    path('<int:id>/comment', ajax_views.add_comment, name='comment'),
    path('<int:id>/comment/<int:cmid>/report', ajax_views.report_comment, name='report_comment'),
    path('<int:id>/report', ajax_views.report_project, name='report_project'),

]
