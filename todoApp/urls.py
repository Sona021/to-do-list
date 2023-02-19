from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('to-do-list/', views.todo),
    path('practice-ide', views.practice)
]