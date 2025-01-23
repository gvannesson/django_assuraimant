from django import forms
from assuraimant.models import User
from django.contrib.auth.forms import UserCreationForm
from datetime import date


class CustomCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


class UserChangeForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Year", "Month", "Day"), years=[x for x in range(date.today().year-17, 1900, -1)]))
    class Meta:
        model = User
        fields = ['date_of_birth','weight', 'height', 'region', 'smoker', 'sex', 'children']
