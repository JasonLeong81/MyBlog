from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'NLP'
urlpatterns = [
    path('',views.index,name='index'),
    path('Tutorial/',views.Tutorial,name='Tutorial'),
]