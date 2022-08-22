from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.get_quize, name='get_quize'),
    path('quiz/', views.quiz, name='quiz'),
]