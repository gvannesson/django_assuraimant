from django.contrib import admin
from django.urls import path, include
from .views import HomeView, CreateUserViews

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('signup', CreateUserViews.as_view(), name='signup')
]
