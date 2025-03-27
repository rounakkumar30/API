# apps/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),  
    path('add-app', views.add_app),
    path('get-app/<int:id>', views.get_app),
    path('delete-app/<int:id>', views.delete_app),
]
