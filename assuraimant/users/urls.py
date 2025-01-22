from django.contrib.auth.views import LoginView
from django.urls import path, include
from .views import HomeView, CreateUserViews
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    # path('signup/', CreateUserViews.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('login/', views.sign_in, name='login'),
    # path('logout/', views.sign_out, name='logout'),
    path('signup/', CreateUserViews.as_view(), name='signup'),
]

