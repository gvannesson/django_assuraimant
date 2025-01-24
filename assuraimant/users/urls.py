from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import path, reverse_lazy
from .views import HomeView, CreateUserViews, DisplayProfileView, UserUpdateView
from .views import HomeView, CreateUserViews, PredictionView

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('signup/', CreateUserViews.as_view(), name='signup'),
    path('profile/', DisplayProfileView.as_view(), name='display_profile'),
    path ("logout/", LogoutView.as_view(), name="logout"),
    path ("<int:pk>/update/", UserUpdateView.as_view(), name="user_update"),
    path('password_change/', PasswordChangeView.as_view(success_url=reverse_lazy('login')), name='password_change'),
    path ("prediction/", PredictionView.as_view(), name="prediction")
]

