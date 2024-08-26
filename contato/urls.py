from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.contato, name='contato'),
    path('gravar/', views.gravar, name='gravar'),
    path('mostrar/', views.exibe, name='mostrar'),
]


