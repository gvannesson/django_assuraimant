from django import forms
from assuraimant.models import User
from django.contrib.auth.forms import UserCreationForm





class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    
class CustomCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


# class CustomProfileForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['Birth Date', 'Weight', 'Height', 'Region', 'Smoker', 'Sex', 'Number of children']