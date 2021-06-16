from django.contrib import admin
from django.urls import path
from .views import HomeView, UserCreationView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', UserCreationView.as_view(), name='register')
]