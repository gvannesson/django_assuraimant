from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import path, reverse_lazy
from .views import HomeView, CreateUserViews, DisplayProfileView, UserUpdateView, AccountUpdateView, HistoryView
from .views import HomeView, CreateUserViews, PredictionView, AllPredictionsView, SimulatePredictionView, DeleteUserView, AboutUsView

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('signup/', CreateUserViews.as_view(), name='signup'),
    path('profile/', DisplayProfileView.as_view(), name='display_profile'),
    path ("logout/", LogoutView.as_view(), name="logout"),
    path ("history/", HistoryView.as_view(), name="history"),
    path ("<int:pk>/update/", UserUpdateView.as_view(), name="user_update"),
    path ("<int:pk>/acc_upadte/", AccountUpdateView.as_view(), name="account_update"),
    path('password_change/', PasswordChangeView.as_view(success_url=reverse_lazy('login')), name='password_change'),
    path ("prediction/", PredictionView.as_view(), name="prediction"),
    path ("all_prediction/", AllPredictionsView.as_view(), name="all_predictions"),
    path ("simulate_prediction/<int:pk>/", SimulatePredictionView.as_view(), name="simulate_pred"),
    path("delete_user/<int:pk>/", DeleteUserView.as_view(), name='delete_user'), 
    path("about_us/", AboutUsView.as_view(), name="about_us")
]

