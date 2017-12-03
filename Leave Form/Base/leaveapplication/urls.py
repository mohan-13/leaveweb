from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns=[

    url(r'^$',views.index),
    url(r'^apply/', views.tester)
]

# Create your views here.
