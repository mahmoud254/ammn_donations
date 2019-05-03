
from django.urls import path, include 
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path('', views.index, name='index'),
    # path('signup/', views.SignUp.as_view(), name='signup'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^profile/$', views.view_profile, name='view_profile_with_pk'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^profile/change-password/$', views.change_password, name='change_password'),
    url(r'^profile/delete/$', views.user_delete, name='user_delete'),



]

