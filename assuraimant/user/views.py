from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from assuraimant.models import User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from forms import UserForm
from django.contrib.auth.forms import UserCreationForm


class CreateUserViews(CreateView):
    model = User #spécifie le modèle
    form_class = UserForm
    template_name = 'signup/signup.html' #spécifie le template
    context_object_name='signup' #le nom utilisé dans le template



class HomeView(TemplateView):
    template_name = 'home/home.html' #spécifie le template
