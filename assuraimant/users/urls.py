from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import HomeView, CreateUserViews, DisplayProfileView, UserUpdateView
from .views import HomeView, CreateUserViews, PredictionView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('signup/', CreateUserViews.as_view(), name='signup'),
    path('profile/', DisplayProfileView.as_view(), name='display_profile'),
    path ("logout/", LogoutView.as_view(), name="logout"),
    path ("user/<int:pk>/update/", UserUpdateView.as_view(), name="user_update"),
    path ("prediction/", PredictionView.as_view(), name="prediction")
]

