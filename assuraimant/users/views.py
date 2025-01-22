from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from django.shortcuts import render
from assuraimant.models import User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomCreationForm
from django.contrib.auth import get_user_model



class CreateUserViews(CreateView):
    model = User #spécifie le modèle
    form_class = CustomCreationForm
    template_name = 'users/signup.html' #spécifie le template
    # context_object_name='signup' #le nom utilisé dans le template
    success_url = reverse_lazy('login') #redirection après la création

    # def get_queryset(self):
    #     password = self.request.GET.get('password')
    #     password = User.set_password(password)
    #     self.request.GET['password']=password
    #     return self.request



class HomeView(TemplateView):
    template_name = 'users/home.html' #spécifie le template

# class LogInView(TemplateView):
#     template_name = 'users/login.html' #spécifie le template
