from django.views.generic import TemplateView, ListView, FormView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.views import LogoutView
from assuraimant.models import User
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import CustomCreationForm, UserChangeForm
from .forms import CustomCreationForm
import cloudpickle
import pandas


class CreateUserViews(CreateView):
    model = User #spécifie le modèle
    form_class = CustomCreationForm
    template_name = 'users/signup.html' #spécifie le template
    # context_object_name='signup' #le nom utilisé dans le template
    success_url = reverse_lazy('login') #redirection après la création

class HomeView(TemplateView):
    template_name = 'users/home.html' #spécifie le template

class DisplayProfileView(TemplateView):
    template_name='users/profile.html'

class UserUpdateView(UpdateView):
    model = User  # Le modèle que l'on souhaite mettre à jour
    form_class=UserChangeForm
    # fields = ['date'of'birth''weight', 'height', 'region', 'smoker', 'sex', 'children']  # Les champs que l'on souhaite afficher dans le formulaire
    template_name = 'users/user_update.html'  # Le template à utiliser pour le formulaire
    success_url = reverse_lazy('display_profile')  # L'URL vers laquelle rediriger après la mise à jour réussie

    # def form_valid(self, form):
    #     """If the form is valid, save the associated model."""
    #     self.object = form.save()
    #     # return super().form_valid(form)
    #     print(form)

# class LogInView(TemplateView):
#     template_name = 'users/login.html' #spécifie le template

class PredictionView(TemplateView):
    template_name = "users/prediction.html"
    
    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        region = "southeast" if user.region == 1 else "southwest" if user.region == 2 else "northeast" if user.region == 3 else "northwest"
        bmi = user.weight / (user.height)**2
        client=[[user.age,user.sex, user.children,user.smoker, region, bmi]]
        client_array= pandas.DataFrame(client, columns=["age","sex","children","smoker","region","bmi"])
        
        model = cloudpickle.load(open("users/best_model.pkl", 'rb'))
        
        context["test"] = f"Bonjour, {user.first_name}. Voici votre prédiction de prime d'assurance : " 
        context["prediction"] = model.predict(client_array).round(2)
        return context
    
