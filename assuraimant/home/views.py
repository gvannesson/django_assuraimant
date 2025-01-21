from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy




class HomeView(TemplateView):
    template_name = 'home/home.html' #spécifie le template
