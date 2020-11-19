from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.display, name='display'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('search', views.search, name='search')
]