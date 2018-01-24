from django.contrib import admin
from django.conf.urls import url
from . import views
from django.contrib.auth import views as view

urlpatterns=[

    url(r'^$', views.home),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', view.login, name='login'),
    url(r'^index/$', views.index, name='index'),
    url(r'^apply/$', views.apply, name='apply'),
    url(r'^details/$', views.details, name='details')
]

# Create your views here.
