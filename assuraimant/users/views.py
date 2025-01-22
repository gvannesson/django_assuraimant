from django.views.generic import TemplateView, ListView, FormView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.views import LogoutView
from assuraimant.models import User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomCreationForm



class CreateUserViews(CreateView):
    model = User #spécifie le modèle
    form_class = CustomCreationForm
    template_name = 'users/signup.html' #spécifie le template
    # context_object_name='signup' #le nom utilisé dans le template
    success_url = reverse_lazy('login') #redirection après la création


class HomeView(TemplateView):
    template_name = 'users/home.html' #spécifie le template

# class LogInView(TemplateView):
#     template_name = 'users/login.html' #spécifie le template

class DisplayProfileView(TemplateView):
    model=User
    template_name='users/profile.html'



# class CustomProfileView(TemplateView):
#     model = User
#     template_name = 'users/profile.html'