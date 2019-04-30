"""ammn_donations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.i18n import JavaScriptCatalog
from projects import views, ajax_views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('projects/', include('projects.urls')),
    path('home', views.home, name='home'),
    path('myprojects', views.my_projects, name='my_projects'),
    path('mydonations', views.my_donations, name='my_donations'),
    path('category/<int:id>', views.get_category, name="category"),
    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment_process', TemplateView.as_view(template_name="projects/payment_done.html"), name='payment_done'),
    path('payment_done', TemplateView.as_view(template_name="projects/payment_canceled.html"), name='payment_canceled'),

]
