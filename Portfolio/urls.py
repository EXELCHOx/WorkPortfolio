from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('projects/', views.projects, name='projects'),
    path('home/', views.home, name='home')

]