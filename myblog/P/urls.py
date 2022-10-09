from django.urls import path

from . import views

app_name = 'P'
urlpatterns = [
    path('HelloWorld/', views.index, name='index'),
    path('<int:tutorial_number>/', views.TN, name='TN'),
    path('', views.t, name='t'),
    path('detail/', views.detail, name='detail'),
    path('result/', views.result, name='result'),
    path('insert/', views.insert, name='insert'),
]