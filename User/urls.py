
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
]

