from django import forms
from assuraimant.models import User
from django.contrib.auth.forms import UserCreationForm



class CustomCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Year", "Month", "Day")))
    class Meta:
        model = User
        fields = ['date_of_birth','weight', 'height', 'region', 'smoker', 'sex', 'children']
