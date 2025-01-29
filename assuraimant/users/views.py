from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, FormView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from assuraimant.models import User, Prediction
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import CustomCreationForm, UserChangeForm, AccountChangeForm, Recherche
import cloudpickle
import pandas
from datetime import date
from django.shortcuts import redirect
from django.http import JsonResponse
import json
from django.contrib.messages.views import SuccessMessageMixin


def calculate_age(date_of_birth):
    today = date.today()
    #If date is received as string, transform it to Date
    if (type(date_of_birth) == str):
        date_of_birth = date(year=int(date_of_birth[0:4]), month=int(date_of_birth[5:7]), day=int(date_of_birth[8:10]))
    age = today.year - date_of_birth.year
    
    # Check to see if birthday is already passed
    if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
        age -= 1

    return age

class CreateUserViews(CreateView):
    model = User #spécifie le modèle
    form_class = CustomCreationForm
    template_name = 'users/signup.html' #spécifie le template
    # context_object_name='signup' #le nom utilisé dans le template
    success_url = reverse_lazy('login') #redirection après la création

class HomeView(TemplateView):
    template_name = 'users/home.html' #spécifie le template

class DisplayProfileView(LoginRequiredMixin, TemplateView):
    template_name='users/profile.html'
    login_url= "/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['predictions'] = self.request.user.prediction_set.all().filter(user_id=self.request.user.id)
        return context

class UserUpdateView(UpdateView, LoginRequiredMixin):
    model = User  # Le modèle que l'on souhaite mettre à jour
    form_class=UserChangeForm
    template_name = 'users/user_update.html'  # Le template à utiliser pour le formulaire
    success_url = reverse_lazy('display_profile')  # L'URL vers laquelle rediriger après la mise à jour réussie

class DeleteUserView(SuccessMessageMixin, DeleteView):
    model = User
    template_name= 'users/delete_user_confirm.html'
    success_message='Your account has been deleted'
    success_url = reverse_lazy('home_view')

class AccountUpdateView(UpdateView, LoginRequiredMixin):
    model = User  # Le modèle que l'on souhaite mettre à jour
    form_class=AccountChangeForm
    template_name = 'users/account_update.html'  # Le template à utiliser pour le formulaire
    success_url = reverse_lazy('display_profile')  # L'URL vers laquelle rediriger après la mise à jour réussie


class PredictionView(LoginRequiredMixin, TemplateView):
    template_name = "users/prediction.html"
    login_url= "/login/"
    
    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        region = "southeast" if user.region == 1 else "southwest" if user.region == 2 else "northeast" if user.region == 3 else "northwest"
        bmi = user.weight / (user.height)**2
        
        age = calculate_age(user.date_of_birth)
        client=[[age,user.sex, user.children,user.smoker, region, bmi]]
        client_array= pandas.DataFrame(client, columns=["age","sex","children","smoker","region","bmi"])
        
        model = cloudpickle.load(open("users/best_model.pkl", 'rb'))
        
        context["test"] = f"Bonjour, {user.first_name}. Voici votre prédiction de prime d'assurance : " 
        context["prediction"] = model.predict(client_array)[0].round(2)

        user.last_charge_prediction = context["prediction"]
        user.save()
        
        pred= Prediction()
        pred.height = user.height
        pred.weight = user.weight
        pred.region = user.get_region_display()
        pred.smoker = user.get_smoker_display()
        pred.sex = user.get_sex_display()
        pred.age = age
        pred.prediction = context['prediction']
        pred.user_id = user
        pred.save()

        return context


class HistoryView(ListView):
    model=Prediction
    template_name = 'users/history.html'
    context_object_name = 'predictions'
    def get_queryset(self):
        return self.request.user.prediction_set.all()
    
class AllPredictionsView(ListView, FormView):
    model = Prediction
    form_class = Recherche
    template_name = 'users/all_predictions.html'
    context_object_name = 'predictions'

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_staff:
            return redirect('/profile/')
        return super().dispatch(request, *args, **kwargs)


    def get_queryset(self):
        query_name = self.request.GET.get('search_by_user')
        query_date_year = self.request.GET.get('search_by_date_year')
        query_date_month = self.request.GET.get('search_by_date_month')
        query_date_day = self.request.GET.get('search_by_date_day')
        result = Prediction.objects.all()
        print("---------------------------------")
        print(query_name)
        print("---------------------------------")
        if query_name:
            result =  result.filter(user_id=query_name)
        if query_date_year:
            result = result.filter(prediction_date__year=int(query_date_year))
        if query_date_month:
            result = result.filter(prediction_date__month=int(query_date_month))
        if query_date_day:
            result = result.filter(prediction_date__day=int(query_date_day))
        return result



class SimulatePredictionView(TemplateView):
    template_name = 'users/simulate_pred.html'  # Le template à utiliser pour le formulaire
    
    
    def post(self, request, *args, **kwargs):
        try:
            # Récupérer les données JSON envoyées via fetch
            data = json.loads(request.body)  # Parse le corps de la requête en JSON
            # print("DATA : ", data)

            # Traiter les données
            if data:
                region = data["region"]
                bmi = float(data["weight"]) / ((float(data["height"])/100)**2)
                age = calculate_age(data["date_of_birth"])

                client = [[age, data["sex"], data["children"], data["smoker"], region, bmi]]
                client_array = pandas.DataFrame(client, columns=["age", "sex", "children", "smoker", "region", "bmi"])
                model = cloudpickle.load(open("users/best_model.pkl", 'rb'))
                prediction_ = model.predict(client_array).round(2)

                return JsonResponse({"prediction": prediction_[0], 'bmi':round(bmi,2)}, status=200)
            else:
                response_data = {
                    'message': "Aucune donnée reçue",
                    'status': 'error'
                }
                return JsonResponse(response_data, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    
    
    # def get(self, request, *args, **kwargs):
    #     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            
    #         data = {"prediction": self.prediction}
    #         return JsonResponse(data)  # Retourne une réponse JSON
    #     return super().get(request, *args, **kwargs)  # Charge le template HTML
    
class AboutUsView(TemplateView):
    
    template_name='users/about_us.html'


    
