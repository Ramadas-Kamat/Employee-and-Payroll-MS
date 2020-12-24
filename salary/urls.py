from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.display, name='display'),
    #path('editsal',views.edit_sal,name='editsal')
]