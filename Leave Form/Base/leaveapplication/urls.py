from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns=[

    url(r'^$',views.home),
    url(r'^login/$',views.index,name='login'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^apply/$', views.tester,name='tester'),
    url(r'^details/$',views.details,name='details')
]

# Create your views here.
